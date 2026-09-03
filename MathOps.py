
#!/usr/bin/python3

# Include path to modules Library
import platform
import sys
Platform = platform.system()
if ('CYGWIN_NT' in Platform): #-10.0-22631'):
    sys.path.append('/usr/local/Lib/Python')
elif ('Windows' in Platform):
    sys.path.append("C:\\Lib\\Python")
elif ('Linux' in Platform):
    sys.path.append('/usr/local/Lib/Python')

from Extentions import Extention
from math import factorial
from math import log10
from math import log2
from math import log
from math import pow
from math import comb
from math import perm
import datetime
import sympy as sp
import numpy as np
import math as math

from COLORS import WHITE, RED, YELLOW, BOLD, BLUE, GREEN, CYAN, MAGENTA, BLACK   # type: ignore
from Colorizer import Colorizer # type: ignore

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
#addStr = Colorizer().addStr

#*****************************************************************************
# The Execute the actions encoded by the Binary Tree
#*****************************************************************************
class MathOps(Extention):
    def __init__(cls, 
                 Name="MathOps", 
                 Version=__version__, 
                 Author=__author__, 
                 Status=__status__):
        cls.Ops={
            '+':cls.Add,
            '-':cls.Add,
            '~':cls.Tilde,
            '^':cls.Carot,
            '*':cls.Mult,
            '/':cls.Div,
            'xOr':cls.XOr,
            '&':cls.And,
            '|':cls.Or,
            '!':cls.Fact,
            'LOG':cls.Log,
            'LOG2':cls.Log2,
            'LN':cls.ln,
            'nPr':cls.Permute,
            'nCr':cls.Choose,
            '>>':cls.ShftLeft,
            '<<':cls.ShftRght,
            'TIME':cls.Time,
            '=':cls.Assn,
        }

    #*****************************************************************************
    # Print the help information for the extension.
    #*****************************************************************************
    @classmethod
    def Help(cls):
        cprint(BOLD, BLUE, "MathOps Extension Help")
        cprint(WHITE, " Provides basic mathematical and variable operations")
        cprint(WHITE, " Available Operations:")
        for Op in cls.Ops:
            cprint(GREEN, "  ", Op)

    #*****************************************************************************
    # Return the table of operations for the extension.
    #*****************************************************************************
    @property
    def Table(cls):
        return cls.Ops

    #*****************************************************************************
    # Preform the Add Method.
    #*****************************************************************************
    @classmethod
    def Add(cls, ValLf, ValRt): # Add '+'
        Rslt = ValLf + ValRt
        return Rslt

    #*****************************************************************************
    # Preform the Subtract Method.
    #*****************************************************************************
    @classmethod
    def Sub(cls, ValLf, ValRt): # Sub '-'
        Rslt=ValLf - ValRt
        return Rslt

    #*****************************************************************************
    # Preform the Tilde Method.
    #*****************************************************************************
    @classmethod
    def Tilde(cls, ValLf=None, ValRt=None): # Tilde '~'
        if ValRt:            
            Rslt= ~ValRt # Right side is a Value
        elif ValLf:
            Rslt= ~ValLf # Left side is a Variable
        else:
            cprint(BOLD, RED, "Error: No argument for Tilde opererand for '~' operator")
            Rslt=None
        return Rslt

    #*****************************************************************************
    # Preform the Power or raise to the power Method.
    #*****************************************************************************
    @classmethod
    def Carot(cls, ValLf, ValRt):# Carot '^'
        Rslt= ValLf ** ValRt
        return Rslt

    #*****************************************************************************
    # Preform the Multiply Method.
    #*****************************************************************************
    @classmethod
    def Mult(cls, ValLf, ValRt): # Mult '*'
        Rslt= ValLf * ValRt
        return Rslt

    #*****************************************************************************
    # Preform the Divide Method.
    #*****************************************************************************
    @classmethod
    def Div(cls, ValLf, ValRt): # Div '/'
        if ValRt:
            if ValRt != 0:
                Rslt=ValLf / ValRt
            else:
                cprint(BOLD, RED, "Error: ", WHITE, "Division by zero")
                Rslt=None   
        else:
            cprint(BOLD, RED, "Error: No divisor")
            Rslt=None
        return Rslt

    #*****************************************************************************
    # Preform the Exclusive OR Method.
    #*****************************************************************************
    @classmethod
    def XOr(cls, ValLf, ValRt):# XOr 'xOr'
        Rslt = np.bitwise_xor(ValLf, ValRt)
        return Rslt        

    #*****************************************************************************
    # Preform the And Method.
    #*****************************************************************************
    @classmethod
    def And(cls, ValLf, ValRt): # And '&'
        Rslt = np.bitwise_and(ValLf, ValRt)
        return Rslt

    #*****************************************************************************
    # Preform the Or Method.
    #*****************************************************************************
    @classmethod
    def Or(cls, ValLf, ValRt): # Or '|'
        Rslt = np.bitwise_or(ValLf, ValRt)
        return Rslt

    #*****************************************************************************
    # Preform the Factorial Method.
    #*****************************************************************************
    @classmethod
    def Fact(cls, ValLf, ValRt=None): # Fact '!'
        Rslt=math.factorial(ValLf)
        return Rslt

    #*****************************************************************************
    # Preform the Log base 10 Method.
    #*****************************************************************************
    @classmethod
    def Log(cls, ValLf, ValRt=None): # Log 'LOG'
        Rslt=np.log10(ValLf)
        return Rslt

    #*****************************************************************************
    # Preform the Log base 2 Method.
    #*****************************************************************************
    @classmethod
    def Log2(cls, ValLf, ValRt=None): # Log2 'LOG2'
        Rslt=np.log2(ValLf)
        return Rslt

    #*****************************************************************************
    # Preform the Natural Log Method.
    #*****************************************************************************
    @classmethod
    def ln(cls, ValLf, ValRt=None): # ln 'LN'
        Rslt=np.log(ValLf)
        return Rslt

    #*****************************************************************************
    # Preform the Statistical Permutations Method.
    #*****************************************************************************
    @classmethod
    def Permute(cls, ValLf, ValRt): # Permute 'nPr'
        Rslt=perm(ValLf, ValRt)
        return Rslt

    #*****************************************************************************
    # Preform the Statistical Combinations Method.
    #*****************************************************************************
    @classmethod
    def Choose(cls, ValLf, ValRt): # Choose 'nCr'
        Rslt=comb(ValLf, ValRt)
        return Rslt

    #*****************************************************************************
    # Preform the Shift Left Method.
    #*****************************************************************************
    @classmethod
    def ShftLeft(cls, ValLf, ValRt): # ShftLeft '>>'
        Rslt=ValLf >> ValRt
        return Rslt

    #*****************************************************************************
    # Preform the Shift Right Method.
    #*****************************************************************************
    @classmethod
    def ShftRght(cls, ValLf, ValRt): # ShftRght '<<'
        Rslt=ValRt << ValLf
        return Rslt

    #*****************************************************************************
    # Preform the Time Method.
    #*****************************************************************************
    @classmethod
    def Time(cls, ValLf=None, ValRt=None): # Time 'TIME'
        Rslt=datetime.datetime.now()
        return Rslt

    #*****************************************************************************
    # Preform the Assignment Method.
    #*****************************************************************************
    @classmethod
    def Assn(cls, ValLf, ValRt, V): # Assn '='
        V.Set(ValLf, ValRt)

    #*****************************************************************************
    # return Name of Extention
    #*****************************************************************************
    @property
    def Name(cls):
        return cls.__class__.__name__
    
