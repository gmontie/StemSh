from argparse import FileType
import platform
import sys
Platform = platform.system()
if ('CYGWIN_NT' in Platform): #-10.0-22631'):
    sys.path.append('/usr/local/Lib/Python')
    from msPrompt import KeyboardPrompt
elif ('Windows' in Platform):
    sys.path.append("C:\\Lib\\Python")
    from msPrompt import KeyboardPrompt
elif ('Linux' in Platform):
    sys.path.append('/usr/local/Lib/Python')
    from Prompt import KeyboardPrompt

import os
import mimetypes

# Include the Colorizer and COLORS Objects
from COLORS import BOLD, GREEN, RED, BLUE, YELLOW, WHITE, RESET # type: ignore
from Colorizer import Colorizer # type: ignore

# Inport the Extention class
from Extensions import Extension

#│▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
#│▒                                                                              ▒│
#│▒          MetAdATa                                                            ▒│
#│▒                                                                              ▒│
#│▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
__author__ = "Greg Montgomery"
__version__ = "2.0.0"
__status__ = "Development"

cprint = Colorizer().cprint
addStr = Colorizer().addStr

#*****************************************************************************
# FileSys Extention
#*****************************************************************************
class FileSys(Extension):
    def __init__(cls, 
                 Name="Operations", 
                 Version=__version__, 
                 Author=__author__, 
                 Status=__status__):
        cls.Debug=True

        cls.Ops={
            'ENV':cls.PrintENV,
            'DIR':cls.Dir,
            'PWD':cls.Pwd,
            'CD':cls.ChangeDir,
            'CAT':cls.Cat,         
            'LS':cls.Ls,
            'CLEAR': cls.ClearScreen,
            'CLS': cls.ClearScreen, 
            'FILE':cls.FileInfo,
         }  

    #*****************************************************************************
    # Cat for a File
    #*****************************************************************************
    @property
    def Table(cls):
        return cls.Ops

    #*****************************************************************************
    # Change Directory
    #*****************************************************************************
    @classmethod
    def Execute(cls, Line):
        pass
        # TokenList = cls.Tokenizer.tokenize(Line)
        # cls.Parser.Clear()
        # cls.Parser.SetLine(Line)
        # aCmd = cls.Parser.parse( TokenList )
        # return aCmd
    
    #*****************************************************************************
    # Change Directory
    #*****************************************************************************
    @classmethod
    def ChangeDir(cls, Args=None):
        if Args:
            cls.Cd(Args)
        else:
            cls.Cd()

   #*****************************************************************************
   # Display the Environment.
   #*****************************************************************************
    @classmethod
    def PrintENV(cls, Args=None):
        print(Platform)

    #*****************************************************************************
    # Clear the Screen
    #*****************************************************************************
    @classmethod
    def ClearScreen(cls, Args=None):
       print(chr(27) + "[2J")

    #*****************************************************************************
    # Cat for a File
    #*****************************************************************************
    @classmethod
    def FileInfo(cls, Args):
      FileName = Args[0]
      MimeType, encoding = mimetypes.guess_type(FileName)
      if MimeType is None:
          MimeType = "Unknown"
      cprint(BOLD, BLUE, FileName, WHITE, " is of type ", GREEN, MimeType)
    
    #*****************************************************************************
    # Cat for a File
    #*****************************************************************************
    @classmethod
    def Cat(cls, Args):
        FileName = Args[0]
        try:
            Fin = open(FileName, 'r')
            Lines = Fin.readlines()
            Fin.close()
            Lst = [Line.replace('\n', '') for Line in Lines]
            Lines = Lst
            for Line in Lines:
                cprint(BOLD, WHITE, Line)
        except Exception as e:
            Msg = addStr(RED, "Error:", WHITE, " Was not able to CAT file -->")
            Msg = addStr(Msg, BLUE, FileName, WHITE, "<--")
            cprint(Msg)
            Msg = str(e)
            cprint(RED, Msg)  

    #*****************************************************************************
    # Print the Directory Contents
    #*****************************************************************************
    @classmethod
    def Dir(cls, Args=None):
        Pwd = os.getcwd()
        flList = os.listdir(Pwd)
        Dirs = [d for d in flList if os.path.isdir(Pwd+'/'+d)]
        for Dir in Dirs:
            cprint(BOLD, BLUE, Dir)
        Files = [f for f in flList if os.path.isfile(Pwd+'/'+f)]
        for File in Files:
            cprint(BOLD, WHITE, File)

    #*****************************************************************************
    # Print the Directory Contents
    #*****************************************************************************
    @classmethod
    def Ls(cls, Args=None):
        Pwd = os.getcwd()
        flList = os.listdir(Pwd)
        Dirs = [d for d in flList if os.path.isdir(Pwd+'/'+d)]
        Msg = ''
        for Dir in Dirs:
            Msg = addStr(Msg, BOLD, BLUE, Dir, '  ')
        Files = [f for f in flList if os.path.isfile(Pwd+'/'+f)]
        for File in Files:
            Msg = addStr(Msg, BOLD, WHITE, File, '  ')
        cprint(Msg)

    #*****************************************************************************
    # Print the Current Working Directory. 
    #*****************************************************************************
    @classmethod
    def Pwd(cls, Args=None):
        Msg = os.getcwd()
        cprint(BOLD, GREEN, Msg) 

    #*****************************************************************************
    # Change Directory
    #*****************************************************************************
    @classmethod
    def Cd(cls, Args=None):
        Pwd = os.getcwd()
        try:
            os.chdir(Args[0])
        except Exception as e:
            cprint(RED, 'Was not able to CD to ', WHITE, Args)
            cprint(BOLD, WHITE, e)

    #*****************************************************************************
    # return Name of Extention
    #*****************************************************************************
    @property
    def Name(cls):
        return cls.__class__.__name__
    
    #*****************************************************************************
    # Return True because this Extention is implemented
    #*****************************************************************************
    @property
    def Implemented(cls):
        return True

    #*****************************************************************************
    # Return Help Text/String
    #*****************************************************************************
    @property
    def Help(cls):
        Msg = addStr(BOLD, BLUE, "FileSys Extention Help")
        Msg = addStr(Msg, WHITE, " Provides basic file system operations")
        Msg = addStr(Msg, WHITE, " Available Operations:")
        for Op in cls.Ops:
            Msg = addStr(Msg, GREEN, "  ", Op)
        return Msg   
