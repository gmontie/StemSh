#!/usr/bin/env python3

# Include path to modules Library
import platform
import sys

Platform = platform.system()
if ('CYGWIN_NT' in Platform):  # type: ignore
    sys.path.append('/usr/local/Lib/Python')
    from msPrompt import KeyboardPrompt # type: ignore
elif ('Windows' in Platform): # type: ignore
    sys.path.append("C:\\Lib\\Python")
    from msPrompt import KeyboardPrompt # type: ignore
elif ('Linux' in Platform): # type: ignore
    sys.path.append('/usr/local/Lib/Python')
    from Prompt import KeyboardPrompt # type: ignore

import datetime
import importlib
from importlib.metadata import metadata
import pathlib

# Colorizer to colorize output
from Colorizer import Colorizer # type: ignore
from COLORS import BOLD, GREEN, RED, BLUE, YELLOW, WHITE, MAGENTA, CYAN, RESET # type: ignore

from sortedcontainers import SortedDict
from time import sleep

# Shell and Interpreter Classes
from CmdVars import Vars # type: ignore
from CmdHlp import Help # type: ignore
from AST import AST # type: ignore
from SlyLexer import Tokenize # type: ignore
from SlyParse import theParser # type: ignore
from ExtentionUnit import ExtentionUnit # type: ignore

from FileSys import FileSys # type: ignore
from MathOps import MathOps # type: ignore

# ===============================================================================================
# MetAdATa
# ===============================================================================================
__author__ = "Greg Montgomery"
__version__ = "2.0.0"
__status__ = "Development"

# =================================================================================================
# Constants
# =================================================================================================

EXIT=1
IMMEDIATE=2
RUN=3
PROGRAM=4

Modes={'quit':EXIT,'IMMEDIATE':IMMEDIATE,'RUN':RUN,}

Debug=True

cprint = Colorizer().cprint

#*****************************************************************************
#
#*****************************************************************************
class ExecuteUnit:
    def __init__(self, Args=None):
        self.Kbd = KeyboardPrompt('>>','YELLOW')
        self.Mode = Modes['IMMEDIATE']   # Set the mode to IMMEDIATE
        self.lineCount = 0
        self.ExtDir = {}
        self.Programed = {}
        self.Help=Help()
        self.Extentions=ExtentionUnit()
        self.Vars = Vars()        
        self.Tokenizer = Tokenize()
        self.Parser = theParser(Vars=self.Vars, args=Args)
        self.Cmds={}
        self.Ops={
               'BUILTIN':self.listBuiltIn,
               'EXIT':self.Exit,
               'NOW':self.Now,
               'TIME_NOW':self.TimeNow,
               "LIST_VARS":self.Vars.List,
               'LIST_EXTENTIONS':self.Extentions.ListExtentions,
               'LIST':self.programList,
               'LoadProgram':self.LoadProgram,
               'SaveProgram':self.SaveProgram,
               'LoadExtention':self.LoadExtention,
               'LoadVars':self.LoadVars,
               'RUN':self.SetMode,
               'REN':self.ReNumber,
               'NEW':self.NewProgram,
               'HELP':self.Help.Usage,
               'WAIT':self.Wait,
               '?':self.Help.Usage
        }

        self.ExtDir[ "BuiltIn" ] = self.Extentions.LoadExtention("BuiltIn", self.Ops)
        self.Fs = FileSys()
        self.ExtDir[ self.Fs.Name ] = self.Extentions.LoadExtention(self.Fs.Name, self.Fs.Table)
        self.MathOps = MathOps()
        self.ExtDir[ self.MathOps.Name ] = self.Extentions.LoadExtention(self.MathOps.Name, self.MathOps.Table)

        self.Extentions.Loaded=self.ExtDir
        self.ExtKeys = self.ExtDir.keys()
        self.AST = AST(Vars=self.Vars, Value=self.Extentions)

        print(sys.version)
        #print(sys.version_info)
        #print(platform.python_version())

    #*****************************************************************************
    # 
    #*****************************************************************************
    def getLine(self, Kbd):
        Line = ''
        while Line == '':
            Line = Kbd.Prompt()
        return Line
   
    #*****************************************************************************
    # Execute a Line of Code <IMMEDIATE> Mode
    #*****************************************************************************
    def ProcessInput(self):
        while self.Mode != EXIT:
            if self.Mode == IMMEDIATE: # Execute a single line of code
                Input=self.getLine(self.Kbd)
                self.Execute(Line=Input, InQuestion = Input.split(" ", 1),IsLineNumber=Input.split(" ", 1)[0].isdigit())
            elif self.Mode == RUN: # Execute a list of lines of code
                if self.Programed:
                    cprint(BOLD, GREEN, 'Running Program')
                    for Key, v in self.Programed.items():
                        # cprint(BLUE, Key, " ", BOLD, YELLOW, v)
                        if v[1]: # REM Statement? Yes: Skip, NO: Since there is an AST tree, walk it
                            if type(v).__name__ == 'str':
                                self.Execute(Line=v.strip(), InQuestion = False ,IsLineNumber=False)
                            elif type(v).__name__ == 'list':
                                self.AST.Walk(v[1])
                            else:
                                print("ExecUnit: Line 137--> ", type(v).__name__)
                        else:
                            self.Execute(Line=v[0], InQuestion = False ,IsLineNumber=False)
                else:
                    print("No Program to Run")
                self.Mode = IMMEDIATE


    #*****************************************************************************
    # Evaluate a Line of Code <IMMEDIATE> Mode
    #*****************************************************************************
    def Execute(self, **KwArgs):
        IsLineNumber = KwArgs['IsLineNumber']
        Line = KwArgs['Line']
        InQestion = KwArgs['InQuestion']

        if not Line.upper().startswith('REM'):
            #-----------------------------------------
            TokenList = self.Tokenizer.tokenize(Line)
            self.Parser.Clear()
            self.Parser.SetLine(Line)
            aCmd = self.Parser.parse( TokenList )
            #-----------------------------------------
            if IsLineNumber:
                if aCmd[2][0] != 'REM':
                    #print(InQestion)
                    self.Programed[int(InQestion[0])] = [InQestion[1], None]
                elif aCmd[2][0] == 'BTree':
                    Tree = aCmd[2][1]
                    self.Programed[int(InQestion[0])] = [InQestion[1], Tree]               
            elif aCmd != None:
                if(type(aCmd).__name__ == 'tuple'):
                    if(aCmd[0] == 'BuiltIn'):
                        args = aCmd[2:] # This could be args = aCmd[2:], but leaving it along 
                        Extention = self.Extentions.Which(aCmd[1]) # Lookup
                        self.ExtDir[ Extention ][aCmd[1]](args)
                    elif(aCmd[0] == 'BTree'):
                        Rtn = self.AST.Walk(aCmd[1])
                        if self.Parser.OutPut and Rtn:
                            print(Rtn)
                    elif(aCmd[0] == 'SOLVE'):
                        self.AST.Solve(aCmd[1],aCmd[2])
                    else:
                        print("Unimplemented yet")
                else:
                    print("Tuple not returned")
            else:
                print("Parcer returned Nothing")
    
    # Type, ArgsLst = Args
    # if Type == 'FOR':
    #    EndValue = ArgsLst[1] - 1
    #    Var = ArgsLst[0]
    #    Value = self.Vars.Value(Var)
    #    SubList = self.SliceLines(Lines, Key, 'NEXT')
    #    while Value < EndValue:
    #       Value += 1
    #       self.Run( SubList)                  
    #       self.Vars.Set(Var, Value)
    # elif Type == 'NEXT':
    #    pass
    # elif Type == 'LIST':
    #    self.ProgramedList()

    #*****************************************************************************
    #                                                              
    #*****************************************************************************
    def SliceLines(self, OrderdDiction, Key, Value):
        NewLines = {}       
        Start = False
        Found = False
        for k,v in OrderdDiction.items():
            if k > Key:
                if Value not in v:
                    Tuple = (k, v)
                    NewLines = self.addSubLine(Tuple, NewLines)
                else:
                    break
                    #print(YELLOW+"-----------------------------------------")
                    #print(NewLines)
                    #print(YELLOW+"-----------------------------------------")
        return NewLines 

    #*****************************************************************************
    # Add a line of Programming code to some type of sub list of programming lines
    #*****************************************************************************
    def addSubLine(self, Tuple, Prg):
        Number, Line=Tuple
        if type(Line).__name__!='str':
            Line=str(Line)

        LineNumber=None
        Program = {}
        if type(Number).__name__=='int':
            LineNumber = Number
        elif type(Number).__name__=='str':
            LineNumber = int(Number)
        Prg[LineNumber] = Line
        Program = SortedDict( sorted(Prg.items()) )
        Prg=Program
        return Prg
         
    #*****************************************************************************
    # Add a line of Programming code to the list of program lines
    #*****************************************************************************
    def addLine(self, Tuple):
        Number, Line=Tuple
        #print("addLine:",Tuple)
        if type(Line).__name__!='str':
            Line=str(Line)
        LineNumber=None
        Program={}
        if type(Number).__name__=='int':
            LineNumber=Number
        elif type(Number).__name__=='str':
            LineNumber=int(Number)
        self.Programed[LineNumber]=Line
        Program = SortedDict( sorted(self.Programed.items()) )
        self.Programed = Program
               
    #*****************************************************************************
    # Get the Dictionary List of lines of code comprising the program
    #*****************************************************************************
    def getProgram(self, Args=None):
        return self.Programed
   
    #*****************************************************************************
    # Load a program into memory
    #*****************************************************************************
    def LoadProgram(self, Args):
        FileName = Args[0]
        if self.Programed:
            self.NewProgram()
        try:
            Fin = open(FileName,'r')
            Lines = Fin.readlines()
            for Line in Lines:
                Line = Line.replace('\n', '')    # remove '\n' only
                Lst = Line.split(' ')
                Nbr = Lst[0]
                Lst = Lst[1:]
                #print("Nbr:",Nbr," Type:",type(Nbr).__name__)
                #print(" Line:",Lst, " Type:",type(Lst).__name__)
                if Lst:
                    Str=''
                    for Elmnt in Lst:
                        Str+=(Elmnt + ' ')
                    Tuple=(Nbr, Str)
                    #print('Tuple:', Tuple)
                    self.addLine(Tuple)
            Fin.close()
            if '\\' in FileName:
                FileName = FileName.split('\\')[-1]
            cprint(BOLD, GREEN, "Loaded Program : ", CYAN, FileName)
        except FileNotFoundError:
            cprint(BOLD, RED, "Error: ", WHITE, "File ", CYAN, FileName, WHITE, " not found.")
        except Exception as e:
            cprint(BOLD, RED, "Error: ", WHITE, "Could not load program: ", CYAN, FileName)
            cprint(BOLD, RED, "Error: ", WHITE, e)

    #*****************************************************************************
    # Save a program from memory to Disk
    #*****************************************************************************
    def SaveProgram(self, Args):
        FileName = Args[0]
        if self.Programed:
            with open(FileName, 'w') as Fout:
            #Keys = self.Program.keys()
                for Line in self.Programed:
                    wLine = str(Line) + ' ' + self.Programed[Line][0] + '\n'
                    Fout.write(wLine)
                Fout.close()
        else:
            print("No program Lines to save")
    # if self.Programed:
        #     with open(FileName, 'w') as Fout:
        #         for k, v in self.Programed.items(): 
        #             if type(v).__name__ == 'str':
        #                 print(k, v)
        #                 Line = str(Line) + ' ' + self.Programed[Line] + '\n'
        #                 Fout.write(str(Line) + " " + self.Programed[Line] + "\n")
        #             elif type(v).__name__ == 'list':
        #                 print(k,v[0])
        #             else:
        #                 print(type(v).__name__)
        # else:
        #     print('No program to print?!')
        # if len(self.Programed) > 0:
        #     Fout = open(FileName,'w')
        #     Keys = self.Programed.keys()
        #     for Line in self.Programed:
        #         wLine = str(Line) + ' ' + self.Programed[Line] + '\n'
        #         Fout.write(wLine)
        #     Fout.close()
        # else:
        #     print("No program Lines to save")

    #*****************************************************************************
    # Parser --> 'LoadExtention':self.LoadExtention,
    #*****************************************************************************
    def LoadExtention(self, Args):
        ExtName = Args[0]        
        theExtention = importlib.import_module(ExtName)
        importlib.reload(theExtention)
        ExtInstance = theExtention.CmdPi()

        # Create an instance of the extension class so @property access returns values
        ExtInstance.Print('This is a test to see this work')
        
        cprint(RED,"Module Name: ",WHITE, theExtention.__name__)
        # Use instance properties, not class descriptors
        PinConfig = ExtInstance.PinConfiguations
        print(PinConfig)

        What = ExtInstance.Name
        print(What)

        Lst = ExtInstance.Table
        print(Lst)

        value = ExtInstance.Implemented
        print(value)

        self.ExtDir[ ExtInstance.Name ] = self.Extentions.LoadExtention(ExtInstance.Name, ExtInstance.Table)
        self.Extentions.Loaded=self.ExtDir
        self.ExtKeys = self.ExtDir.keys()
        self.AST = AST(Vars=self.Vars, Value=self.Extentions)
        print("  ")

    #*****************************************************************************
    # Parser --> 'LoadVars':self.LoadVars,
    #*****************************************************************************
    def LoadVars(self, Args):
        FileName = Args[0]
        try:
            self.Vars.Load(FileName)
        except:
            cprint(BOLD, "Unable to load ", YELLOW, "Vars",WHITE," from ",RED, FileName)

    #*****************************************************************************
    # Get the next line from the user
    #*****************************************************************************
    def listBuiltIn(self, Args=None):
        Keys = self.BltIn.keys()
        for Key in Keys:
            if Key != 'BUILTIN' and Key != 'self':
                cprint(BOLD, BLUE, Key.lower())

    #*****************************************************************************
    # List the current program from memory
    #*****************************************************************************
    def programList(self, Args=None):
        if self.Programed:
            for k, v in self.Programed.items(): 
                if type(v).__name__ == 'str':
                    cprint(BOLD, BLUE, k, RESET, " ", v)
                elif type(v).__name__ == 'list':
                    cprint(BOLD, BLUE, k, RESET, " ", v[0])
                else:
                    print(type(v).__name__)
        else:
            cprint(BOLD, YELLOW, "WARNING: ", RED, 'No program to print!')
         
    #*****************************************************************************
    # Built In Commands below
    #*****************************************************************************
    def ReNumber(self, Args=None):
        self.AltProg = {}
        lineCounter = 10
        if self.Programed:
            for k, v in self.Programed.items():
                self.AltProg[lineCounter] = v 
                lineCounter += 10
            Program = SortedDict( sorted( self.AltProg.items() ) )
            self.Programed = Program
        else:
            cprint(BOLD, YELLOW, "WARNING: No program to renumber!")
        
    
    #*****************************************************************************
    # Start a new program.. reset self.Programed
    #*****************************************************************************
    def NewProgram(self, Args=None):
        self.Programed = {}

    #*****************************************************************************
    # Pause program execution for 
    #*****************************************************************************
    def Wait(self, Args):
        Time = Args[0] #/ 1000
        sleep(Time)

    #*****************************************************************************
    # Print the current Time and save it to the internal Time variable
    #*****************************************************************************
    def Now(self, Args=None):
        Now=datetime.datetime.now()
        cprint(CYAN, f"{Now:%B %d, %Y %H:%M:%S}")
        self.Vars.Set('Time', Now)
        return Now

    #*****************************************************************************
    # Return the time right now
    #*****************************************************************************
    def TimeNow(self, Args=None):
        __Now=datetime.datetime.now()
        return __Now

    #*****************************************************************************
    # Exit the shell
    #*****************************************************************************
    def Exit(self, Args=None):
        self.Mode = Modes['quit']

    #*****************************************************************************
    # Change the Mode of Operation for the shell
    #*****************************************************************************
    def SetMode(self, Args):
        self.Mode = Modes[Args[0]]

    #*****************************************************************************
    # Predicate to tell if a program is in memory or not
    #*****************************************************************************
    def programed(self):
        if self.Programed:
            return True
        else:
            return False
