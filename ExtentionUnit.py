#!/usr/bin/env python3

# Include path to modules Library
import platform
import sys
from typing import Callable

Platform = platform.system()

if ('CYGWIN_NT' in Platform): #-10.0-22631'):
    sys.path.append('/usr/local/Lib/Python')
    from msPrompt import KeyboardPrompt # type ignore 
elif ('Windows' in Platform):
    sys.path.append("C:\\Lib\\Python")
    from msPrompt import KeyboardPrompt # type: ignore
elif ('Linux' in Platform):
    sys.path.append('/usr/local/Lib/Python')
    from Prompt import KeyboardPrompt # type: ignore

import os
import importlib as LoadMod

from functools import wraps
from typing import Any, Dict, Callable, List, Tuple, Union

# Colorizer to colorize output
from Colorizer import Colorizer # type: ignore
from COLORS import BOLD, GREEN, RED, BLUE, YELLOW, WHITE, MAGENTA, CYAN, RESET # type: ignore

#type Command = dict[str, Callable] 
#type Extention = dict[str, Command]

# ===============================================================================================
# MetAdATa
# ===============================================================================================
__author__ = "Greg Montgomery"
__version__ = "1.0.0"
__status__ = "New Development"

cprint = Colorizer().cprint
addStr = Colorizer().addStr

Command={}
Extention={}

#*****************************************************************************
# ExtentionUnit Class
#*****************************************************************************
class ExtentionUnit:
    def __init__(self): #, **kwargs):
        self.Tables={}
        self.Extentions={}
        self.JumpTable={}
        self.FnMap = {}
        self.Loaded = {}

    #*****************************************************************************
    # Load an Extention
    #*****************************************************************************
    def LoadExtention(self, Name, Table):
        if self.JumpTable:
            self.Extentions = self.JumpTable | Table
            self.JumpTable = self.Extentions
            self.Tables[ Name ] = Table
        else:
            self.JumpTable = Table
            self.Tables[ Name ] = self.JumpTable
                    
        Keys = self.JumpTable.keys()
        for Key in Table.keys():
            self.FnMap[ Key ] = Name
        return self.JumpTable        

    #*****************************************************************************
    # Check if an Extention is Loaded
    #*****************************************************************************
    def ExtentionLoaded(self, Name):
        return (Name in self.Extentions.keys())
       
    #*****************************************************************************
    # Get a list of Loaded Extentions
    #*****************************************************************************
    def GetExtentions(self, Name):
        return self.Tables[Name]
        
    #*****************************************************************************
    # Get the List of Loaded Extentions
    #*****************************************************************************
    def ListExtentions(self, args=None):
        cprint(BOLD, GREEN, "Loaded Extentions:")
        for Name in self.Tables.keys():
            A = list(self.Tables[Name].keys())
            cprint(WHITE, Name, "  ", BOLD, YELLOW, A)
        return list(self.Tables.keys()) 

    #*****************************************************************************
    # 
    #*****************************************************************************
    def Which(self, Arg):
        return self.FnMap[Arg]
    
    #*****************************************************************************
    # 
    #*****************************************************************************
    # @property
    # def Ops(self):
    #     return self.JumpTable

    #*****************************************************************************
    # 
    #*****************************************************************************
    @property
    def Loaded(self):
        return self.Ops
    @Loaded.setter
    def Loaded(self, Value):
        self.Ops = Value
