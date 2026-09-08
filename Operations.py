
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

import datetime
import sympy as sp
import numpy as np
from math import factorial
from math import log10
from math import log2
from math import log
from math import pow
from math import comb
from math import perm
import math as math

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

#*****************************************************************************
# The Execute the actions encoded by the Binary Tree
#*****************************************************************************
class Ops(object):
    def __init__(cls):
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

    @property
    def Table(cls):
        return cls.Ops

    @classmethod
    def Add(cls, ValLf, ValRt): # Add '+'
        Rslt = ValLf + ValRt
        return Rslt

    @classmethod
    def Sub(cls, ValLf, ValRt): # Sub '-'
        Rslt=ValLf - ValRt
        return Rslt

    @classmethod
    def Tilde(cls, ValLf=None, ValRt=None): # Tilde '~'
        Rslt= ~ ValRt
        return Rslt

    @classmethod
    def Carot(cls, ValLf, ValRt):# Carot '^'
        Rslt= ValLf ** ValRt
        return Rslt

    @classmethod
    def Mult(cls, ValLf, ValRt): # Mult '*'
        Rslt= ValLf * ValRt
        return Rslt

    @classmethod
    def Div(cls, ValLf, ValRt): # Div '/'
        Rslt=ValLf / ValRt
        return Rslt

    @classmethod
    def XOr(cls, ValLf, ValRt):# XOr 'xOr'
        Rslt = np.bitwise_xor(ValLf, ValRt)
        return Rslt        

    @classmethod
    def And(cls, ValLf, ValRt): # And '&'
        Rslt = np.bitwise_and(ValLf, ValRt)
        return Rslt

    @classmethod
    def Or(cls, ValLf, ValRt): # Or '|'
        Rslt = np.bitwise_or(ValLf, ValRt)
        return Rslt

    @classmethod
    def Fact(cls, ValLf, ValRt=None): # Fact '!'
        Rslt=math.factorial(ValLf)
        return Rslt

    @classmethod
    def Log(cls, ValLf, ValRt=None): # Log 'LOG'
        Rslt=np.log10(ValLf)
        return Rslt

    @classmethod
    def Log2(cls, ValLf, ValRt=None): # Log2 'LOG2'
        Rslt=np.log2(ValLf)
        return Rslt

    @classmethod
    def ln(cls, ValLf, ValRt=None): # ln 'LN'
        Rslt=np.log(ValLf)
        return Rslt

    @classmethod
    def Permute(cls, ValLf, ValRt): # Permute 'nPr'
        Rslt=perm(ValLf, ValRt)
        return Rslt

    @classmethod
    def Choose(cls, ValLf, ValRt): # Choose 'nCr'
        Rslt=comb(ValLf, ValRt)
        return Rslt

    @classmethod
    def ShftLeft(cls, ValLf, ValRt): # ShftLeft '>>'
        Rslt=ValLf >> ValRt
        return Rslt

    @classmethod
    def ShftRght(cls, ValLf, ValRt): # ShftRght '<<'
        Rslt=ValRt << ValLf
        return Rslt

    @classmethod
    def Time(cls, ValLf=None, ValRt=None): # Time 'TIME'
        Rslt=datetime.datetime.now()
        return Rslt

    @classmethod
    def Assn(cls, ValLf, ValRt, V): # Assn '='
        V.Set(ValLf, ValRt)
