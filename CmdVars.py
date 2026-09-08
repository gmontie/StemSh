#!/usr/bin/python3

# Include path to modules Library
import platform
Platform = platform.system()

import sys
if ('CYGWIN_NT' in Platform): # type: ignore
    sys.path.append('/usr/local/Lib/Python')
elif ('Windows' in Platform): # type: ignore
    sys.path.append("C:\\Lib\\Python")
elif ('Linux' in Platform): # type: ignore
    sys.path.append('/usr/local/Lib/Python')

import datetime
import numpy as np

# ========================================================================
# Local module/classes imported from here down.
#from Device import Device
#from BTree import BTree

from COLORS import BOLD, WHITE, RED, YELLOW, GREEN # type: ignore
from Colorizer import Colorizer # type: ignore

#│▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
#│▒                                                                              ▒│
#│▒          MetAdATa                                                            ▒│
#│▒                                                                              ▒│
#│▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
__author__ = "Greg Montgomery"
__version__ = "1.0.0"
__status__ = "Development"

""" 
============================================================================
 Class 
        Vars
          
============================================================================
"""

Variables={} # The list of variables for this module
cprint = Colorizer().cprint
addStr = Colorizer().addStr

#*****************************************************************************
# The Parser and it's actions
#*****************************************************************************
class Vars(object):
    def __init__(cls, Prmt=None, args=None, **kwargs):
        cls.pArgs=args
        cls.Prmt=Prmt
      
    #*************************************************************************
    # Load Variables from file to memory
    #*************************************************************************
    @classmethod
    def Load(cls, FileName):
        Fin=open(FileName,'r')
        Lines=Fin.readlines()
        for Line in Lines:
            Var, Value=Line.split('=')
            Value = Value.replace('\n', '')    # remove '\n' only
            #print('Var: ',Var, ' Value: ',Value)
            Variables[Var]=Value
        Fin.close()

    #***********************************************************************
    # Save the variables from memory to file
    #***********************************************************************
    @classmethod
    def Save(cls, FileName):
        if len(Variables) > 0:
            Fout=open(FileName,'w')
            for Variable in Variables:
                if type(Variables[Variable]).__name__ == 'str':
                    OutString= Variable + '=' + Variables[Variable]
                elif type(Variables[Variable]).__name__ == 'int':
                    OutString = Variable + '=' + str(Variables[Variable])
                else:
                    print("CmdVars.py: 83: Variable is type(", type(Variables[Variable]).__name__, ") ")
                Fout.write(OutString)
                Fout.write('\n')
        else:
            OtString=RED+'No'+WHITE+' varialbes to save'
            print(OtString)
        Fout.close()

    #*************************************************************************
    # List all the variables in memory
    #*************************************************************************
    @classmethod
    def List(cls, Args=None):
        Value=None
        Found=True
        #Str=''
        #print(Variables)
        cprint(BOLD, RED, "List of Variables:")
        Keys=list(Variables.keys())
        Keys.sort()
        for Var in Keys:
            try:
                if Variables[ Var ] != None:
                    #print("Type:",type( Variables[ Var ] ).__name__)
                    if type( Variables[ Var ] ).__name__ == 'str':
                        Value = Variables[ Var ]
                    elif type( Variables[ Var ] ).__name__ == 'int':
                        Value = Variables[ Var ]
                    elif type( Variables[ Var ] ).__name__ == 'float':
                        Value =  Variables[ Var ]
                    elif type( Variables[ Var ] ).__name__ == 'float64':
                        Value =  Variables[ Var ]
                    elif type( Variables[ Var ] ).__name__ == 'bool':
                        if Variables[ Var ]:
                            Value='True'
                        else:
                            Value='False'
                    elif type( Variables[ Var ] ).__name__ == 'list':
                        Value = Variables[ Var ]
                    elif type( Variables[ Var ] ).__name__ == 'dict':
                        Value = Variables[ Var ]
                    elif type( Variables[ Var ] ).__name__ == 'tuple':
                        v = Variables[ Var ]
                        if v[0] == 'FUNCTION':
                            Value = {"Body":v[1]['Line'], "Type":'FUNCTION'}
                        else:
                            Value = Variables[ Var ]
                    elif type( Variables[ Var ] ).__name__ == 'bytes':
                        Value = Variables[ Var ]
                    elif type( Variables[ Var ] ).__name__ == 'bytearray':
                        Value = Variables[ Var ]
                    elif type( Variables[ Var ] ).__name__ == 'datetime':
                        Value =  Variables[ Var ]
                    elif type( Variables[ Var ] ).__name__=='timedelta':
                        Value = Variables[ Var ]
                    else:
                        Found=False
                        print( type( Variables[ Var ] ).__name__ )
            except Exception as e:
                if type(Variables[ Var ]) is np.ndarray:
                    Value=Variables[ Var ]
                    Found=True
                else:
                    Found=False
                    print("Error getting variable:", Var, " Error:", e)

            if Found :
                try:
                    if Value == None:
                        if type(Var).__name__=='str':
                            prntLn=YELLOW + Var + WHITE + ' ==> ' + YELLOW + "None"
                        else:
                            print('Var',Var)
                    elif type(Value).__name__ == 'dict':
                        #print(Value)
                        #prntLn=YELLOW + Var + WHITE + ' ==> ' + YELLOW + Value["Body"] + WHITE + " {" + GREEN + Value["Type"] + WHITE + "}"
                        prntLn=YELLOW + Var + WHITE + ' ==> ' + YELLOW + Value["Line"] + WHITE + " {" + GREEN + "Function" + WHITE + "}"
                        print(prntLn)
                    else:
                        if type(Var).__name__=='str':
                            prntLn=YELLOW + Var + WHITE + ' ==> ' + YELLOW + "None"
                        else:
                            print('Var',Var)
                        print((addStr(YELLOW + Var)), end='')
                        print((addStr(WHITE + ' ==> ')),end='')
                        #print(YELLOW + Var + WHITE)
                        prntLn=type(Value).__name__
                        if type(Value).__name__ != 'str':
                            Value=str(Value)
                            prntLn=YELLOW + Value + WHITE + " {" + GREEN + prntLn + WHITE + "}"
                            print(prntLn)
                        else:
                            prntLn=YELLOW + Value + WHITE + " {" + GREEN + prntLn + WHITE + "}"
                            print(prntLn)
                except Exception as e:
                    if type(Variables[ Var ]) is np.ndarray:
                        print((addStr(YELLOW + Var)), end='')
                        print((addStr(WHITE + ' ==> ')),end='')
                        prntLn=type(Variables[ Var ]).__name__
                        Value = str(Variables[ Var ].tolist())
                        #Value=str(Variables[ Var ])
                        prntLn=YELLOW + Value + WHITE + " {" + GREEN + prntLn + WHITE + "}"
                        print(prntLn)
                    else:
                        print(RED + "Error printing variable: " + WHITE + Var + RED + " Error: " + WHITE + str(e))
            else:
                print(RED + "Variable: " + WHITE + Var + RED + " is of unsupported type: " + WHITE + type(Variables[ Var ]).__name__)
       
    #*****************************************************************************
    # Debug Dump the variables to the screen
    #*****************************************************************************
    @classmethod
    def Dump(cls):
        print(Variables)
      
    #*****************************************************************************
    # Set a variable
    #*****************************************************************************
    @classmethod
    def Set(cls, Name, Value):
        #print(type(Name).__name__)
        if type(Name).__name__ == 'str':
            Variables[Name]=Value
        else:
            cprint(RED, "Error: ", WHITE,"-->", Name, "<---is not a string ",YELLOW,' CmdVars.py: Set()')
            cprint(RED, "Veriable Value Not Set")
   
    #*****************************************************************************
    # Get a variable
    #*****************************************************************************
    @classmethod
    def Value(cls, InQuestion):
        Results=None
        if InQuestion in Variables.keys():
            Results=Variables[InQuestion]
        return Results
   
    #*****************************************************************************
    # Is the variable defined
    #*****************************************************************************
    @classmethod
    def VariableDefined(cls, InQuestion):
        return InQuestion in Variables.keys()

    #*****************************************************************************
    # Is the variable defined
    #*****************************************************************************
    @classmethod
    def VariableNotDefined(cls, InQuestion):
        return InQuestion not in Variables.keys()
    
    #*****************************************************************************
    # Is there any variables defined
    #*****************************************************************************
    @property
    def VariablesDefined(cls):
        Results=False
        if Variables:
            Results=True
        return Results
