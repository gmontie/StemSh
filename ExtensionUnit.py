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

#│▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
#│▒                                                                              ▒│
#│▒          MetAdATa                                                            ▒│
#│▒                                                                              ▒│
#│▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
__author__ = "Greg Montgomery"
__version__ = "1.0.0"
__status__ = "New Development"

cprint = Colorizer().cprint
addStr = Colorizer().addStr

Command={}
Extension={}

#*****************************************************************************
# ExtensionUnit Class
#*****************************************************************************
class ExtensionUnit:
    def __init__(self): #, **kwargs):
        self.Tables={}
        self.Extensions={}
        self.JumpTable={}
        self.FnMap = {}
        self.Loaded = {}

    #*****************************************************************************
    # Load an Extension
    #*****************************************************************************
    def LoadExtension(self, Name, Table):
        if self.JumpTable:
            self.Extensions = self.JumpTable | Table
            self.JumpTable = self.Extensions
            self.Tables[ Name ] = Table
        else:
            self.JumpTable = Table
            self.Tables[ Name ] = self.JumpTable
                    
        Keys = self.JumpTable.keys()
        for Key in Table.keys():
            self.FnMap[ Key ] = Name
        return self.JumpTable        

    #*****************************************************************************
    # Check if an Extension is Loaded
    #*****************************************************************************
    def ExtensionLoaded(self, Name):
        return (Name in self.Extensions.keys())
       
    #*****************************************************************************
    # Get a list of Loaded Extensions
    #*****************************************************************************
    def GetExtensions(self, Name):
        return self.Tables[Name]
        
    #*****************************************************************************
    # Get the List of Loaded Extensions
    #*****************************************************************************
    def ListExtensions(self, args=None):
        cprint(BOLD, GREEN, "Loaded Extensions:")
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
    @property
    def Loaded(self):
        return self.Ops
    @Loaded.setter
    def Loaded(self, Value):
        self.Ops = Value
