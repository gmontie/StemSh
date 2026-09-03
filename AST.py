
#!/usr/bin/python3

# Include path to modules Library
import platform
import sys
Platform = platform.system()
if ('CYGWIN_NT' in Platform):  # type: ignore
    sys.path.append('/usr/local/Lib/Python')
elif ('Windows' in Platform): # type: ignore
    sys.path.append("C:\\Lib\\Python")
elif ('Linux' in Platform): # type: ignore
    sys.path.append('/usr/local/Lib/Python')

from math import factorial
from math import log10
from math import log2
from math import log
from math import pow
from math import comb
from math import perm

# ============================================================================
# Local module/classes imported from here down.
from BTree import BTree
from CmdVars import Vars
from MathOps import MathOps
from COLORS import WHITE, RED, YELLOW, BOLD, BLUE, GREEN, CYAN, MAGENTA, BLACK   # type: ignore
from Colorizer import Colorizer # type: ignore

#import time
import datetime
import math as math
import sympy as sp
import numpy as np

#class ForC(Enum):
FOR=0
VAR=1
EQL=2
STRT=3
TO_=4
END=5

# ===============================================================================================
# MEtADAtA
# ===============================================================================================
__author__ = "Greg Montgomery"
__version__ = "1.0.0"
__status__ = "Development"

""" 
============================================================================
 Class 
 
          
============================================================================
"""

cprint = Colorizer().cprint
addStr = Colorizer().addStr
isColor = Colorizer().isColor

#*****************************************************************************
# The Execute the actions encoded by the Binary Tree
#*****************************************************************************
class AST(object):
    def __init__(self, Vars, Value):
        self.Vars=Vars
        self.Extentions=Value
        self.ExtDir=self.Extentions.Loaded

    #*****************************************************************************
    # Action: Walk the Binary Tree
    #*****************************************************************************
    def Walk(self, Tree, Depth=0):
        ValRt=None
        ValLf=None
        Rslt=None
        Results = None
        TreeType = Tree.Type

        if Tree.Left != None:
            ValLf=self.Walk(Tree.Left, Depth + 1)         
        if Tree.Right != None:
            ValRt=self.Walk(Tree.Right, Depth + 1)

        if TreeType=='VAL':
            Rslt = Tree.Value
            Results = Rslt
        elif TreeType=='As_Var':
            Rslt = Tree.Value
            Results = Rslt
        elif TreeType=='BuiltIn':
            #print(self.ExtDir.keys())
            Extention = self.Extentions.Which(Tree.Value) # Lookup
            #Value = self.ExtDir[ Extention ]
            #print(type(Value).__name__)
            #print(Value)
            args = None
            #Extention = self.Extentions.Which(TreeType) # Lookup
            Results = self.ExtDir[ Extention ][Tree.Value](args)
            #Results = self.ExtDir[ Tree.Value ]()
        elif TreeType == 'FnDecl':
            Rslt = False
            Fn = Tree.Value
            FnType = Fn['Type']
            print(FnType)
            if FnType == 'Declaration' and self.CheckFuntion(Fn):
                Rslt = Fn                
            Results = Rslt
        elif TreeType=='FnCall':
            Lst1 = ValLf['Args'].getList
            Lst2 = ValRt.getList
            Vars = dict(zip(Lst1, Lst2))
            Results = self.Func(Vars, ValLf['Body'], Depth=0)
            #print ("Results: ", Results)
        elif TreeType=='STRING':
            Rslt = Tree.Value
            Results =  Rslt
        elif TreeType=="St":
            if Tree.Value == "PRINT":
               Results = self.getPrintLine(ValLf)
               self.Print(Results)
            elif Tree.Value == "SOLVE":
                self.Print(ValLf)
                self.Print(ValRt)
                self.Print(Tree.Value)
                self.print("Not completely Implemented")
                #Rslt = np.linalg.solve( np.array(self.Vars.Value( Tokens[2].value)), np.array(self.Vars.Value( Tokens[4].value))))
        elif TreeType=='VAR':
            if self.Vars.VariableNotDefined(Tree.Value):
                self.Vars.Set(Tree.Value, 0)
            Rslt=self.Vars.Value(Tree.Value)
            Results =  Rslt
        elif TreeType =='Assign':
           self.Vars.Set(ValLf, ValRt)
        elif TreeType=='Op':
            Extention = self.Extentions.Which(Tree.Value) # Lookup
            Rslt = self.ExtDir[ Extention ][Tree.Value](ValLf, ValRt)
            Results =  Rslt
        else:
            print("   ")
        return Results

    #*****************************************************************************
    # Eveluate a function encoded by the Binary Tree
    #*****************************************************************************
    def Func(self, Vars, Args, Depth=0):
        ValRt=None
        ValLf=None
        Rslt=None
        Tree = None

        if type(Args).__name__ == 'BTree':
            TreeType = Args.Type
            Tree = Args

        if Tree.Left != None:
            ValLf=self.Func(Vars, Tree.Left, Depth + 1)         
        if Tree.Right != None:
            ValRt=self.Func(Vars, Tree.Right, Depth + 1)
        if TreeType=='VAL':
            Rslt = Tree.Value
            return Rslt
        if TreeType=='VAR':
            Rslt = Vars[Tree.Value]
            return Rslt
        elif TreeType=='Op':
            TreeVal = Tree.Value
            Extention = self.Extentions.Which(Tree.Value) # Lookup
            Rslt = self.ExtDir[ Extention ][Tree.Value](ValLf, ValRt)
            #Rslt = self.OpTable[Tree.Value](ValLf, ValRt)
            return Rslt
        else:
            print("   ")

    #*****************************************************************************
    # Action: Define a Fucntion
    #*****************************************************************************
    def defineFUNC(self, Tokens):
        Results=None
        Debug = True
        Cmd=''
        functionDef=''
        if Debug:
            print("In defineFunction(self...")
            self.Dump(Tokens)

        if Tokens[0].type == 'STRING':
            FunName = Tokens[0].value
        if Tokens[1].type == 'LBRACK' and Tokens[2].type == 'STRING':
            setVariable = Tokens[2].value
        if Tokens[3].type == 'RBRACK' and Tokens[4].type=='ASSIGN':
            for Token in Tokens[5:]:
                if type(Token.value).__name__ == "str":
                   functionDef += Token.value
                elif type(Token.value).__name__ == "int":
                   functionDef += str(Token.value)
                else:
                   print("Token Value: ",type(Token.value).__name__)
                   Results = False
      
        if not Results:
             self.Vars.Set(FunName, {'FUNC_NAME':FunName, 'FUNCTION':functionDef, "SET_VAR":setVariable} )
        return Cmd, Results

    #*****************************************************************************
    # Action: Evaluate Function
    #*****************************************************************************
    def evalFunc(self, fnDefinition, Value):
        Results = 0
        SetVariable = sp.symbols( fnDefinition['SET_VAR'] )
        Fn = sp.sympify( fnDefinition['FUNCTION'] )
        Results = Fn.subs( SetVariable, Value ) # <--
        print(fnDefinition['FUNC_NAME'], "(", Value, ") =",  fnDefinition['FUNCTION'])
        sp.pprint(Results)
        return Results

    #*****************************************************************************
    # Solve Lenear Equations
    #*****************************************************************************
    def Solve(self, A, B):
        a = self.Vars.Value( A )
        b = self.Vars.Value( B )
        if type(a).__name__ != 'ndarray':
            A = np.array(a)
        else:
            A = a
        if type(b).__name__ != 'ndarray':
            B = np.array(b)
        else:
            B = b
        Results = np.linalg.solve( A , B )
        print(Results)
        return Results

    #*****************************************************************************
    # Make sure the function definition uses each and every argument 
    # in the function body
    #*****************************************************************************
    def CheckFuntion(self, Fn):
        Results = True
        print(Fn)
        q = Fn['Args']
        Lst = q.getList
        Str = Fn['Line']
        for Arg in Lst:
            if Arg not in Str:
                Results = False
                cprint(BOLD, RED, "Error: ",WHITE, "Argument(", CYAN, Arg, WHITE, ") not used in function body: ", CYAN, Fn['Line'])
        return Results
    
    #*****************************************************************************
    # Action: Construct abstract represnetation for the For construct
    #*****************************************************************************
    # def ForLoop(self, Tokens):
    #    EndValue=0
    #    Results=None
    #    Error=False
    #    Cmd=''    
    #    StartVar=''
      
    #    if Tokens[VAR].type=='STRING' and Tokens[EQL].type=='EQUL':
    #       Var=Tokens[VAR].value
    #       if Tokens[STRT].type=='STRING':
    #          Value=self.Vars.Value( Tokens[STRT].value )
    #          if Value != None:               
    #             self.Vars.Set(Var, Value)
    #          else:
    #             #print(RED, end='')
    #             cprint(BOLD, RED, "In ForLoop:", WHITE, StartVar, RED, " is Not Defined")
    #             Error=True
    #       elif Tokens[STRT].type=='NUMBER':
    #          self.Vars.Set(Var, Tokens[STRT].value )
    #    else:
    #       cprint(RED,end='')
    #       cprint("IN ForLoop: Syntax Error")
    #       Error=True
    #    if Tokens[TO_].type=='TO':
    #       if Tokens[END].type=='STRING':
    #          EndValue=self.Vars.Value( Tokens[END].value )
    #          if EndValue==None:
    #             cprint(RED, end='')
    #             cprint("In ForLoop:", StartVar, " is Not Defined")
    #             Error=True
    #       elif Tokens[END].type=='NUMBER':
    #          EndValue=Tokens[END].value
    #    else:
    #       cprint("Syntax Error")
    #       Error=True
    #    if not Error:
    #       Cmd='PROG_CNTL' 
    #       Results=('FOR', [Var, EndValue])
    #    return Cmd, Results
   
    #*****************************************************************************
    # Action: Construct abstract representation for the If Then construct
    #*****************************************************************************
    # def IfThen(self, Tokens):
    #    Results=None
    #    Cmd=''      
      
    #    if Tokens[VAR].type=='STRING':
    #       pass
      
    #    return Cmd, Results

    #**************************************************************************
    # def Sub(self, Tokens):
    #    Cmd=''
    #    Results=None
    #    if Tokens[0].value.upper()=='DIFF':
    #       Var1=Tokens[1].value
    #       Var2=Tokens[2].value
    #       Var3=Tokens[3].value
    #       Val1=self.Vars.Value(Var1)
    #       Val2=self.Vars.Value(Var2)
    #       Val3=Val1 - Val2
    #       self.Vars.Set(Var3,Val3)
    #       #self.Vars.Dump()
    #    return Cmd, Results
    #    return Tokens[0].value.upper() , Val3


    #*****************************************************************************
    # Action: do Print Statemennt
    #*****************************************************************************
    def getPrintLine(self, Queue):
        Line = " "
        if type(Queue).__name__ != "Queue":
            print("AST 338 Queue: ",type(Queue).__name__)
            print("AST 338 Queue: ",Queue)
        else:
            Lst = Queue.getList
            Line = " "
            for Each in Lst:
                if type(Each).__name__ == 'str':
                    if isColor(Each):
                        Each = Color(Each)
                    Line = addStr(Line, Each)
                elif type(Each).__name__ == 'BTree':
                    Val = self.Walk(Each)
                    Line = addStr(Line, Val)
                else:
                    Line = addStr(Line, Each)
        return Line
    
    #*****************************************************************************
    # Action: do Print Statemennt
    #*****************************************************************************
    def Print(self, Line):
        cprint(Line)
        
