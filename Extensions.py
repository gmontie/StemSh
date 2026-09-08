#!/usr/bin/env python3

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

from abc import ABCMeta, abstractmethod
import importlib

#│▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
#│▒                                                                              ▒│
#│▒          MetAdATa                                                            ▒│
#│▒                                                                              ▒│
#│▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
__author__ = "Greg Montgomery"
__version__ = "1.0.0"
__status__ = "New Development"

#*****************************************************************************
#  Abstract Base Class for Extentions
#  This is an abstract base class that defines the interface for extensions.
#  It includes methods for getting the call list, commands, and help information.
#  The class is designed to be subclassed by concrete extension classes.
#*****************************************************************************
class Extension(metaclass=ABCMeta):
    def __init__(cls, **kwargs):
        if 'Name' in kwargs:
            cls.__Name__ = kwargs['Name']
        else:
            cls.__Name__ = "Unset"

        if 'Version' in kwargs:
            cls.__Version__ = kwargs['Version']
        else:
            cls.__Version = "Unset"

        if 'Author' in kwargs:
            cls.__Author__ = kwargs['Author']
        else:
            cls.__Author__ = "Unset"

        if 'Status' in kwargs:
            cls.__Status__ = kwargs['Status']
        else:
            cls.__Status__ = "Unset"

    #*****************************************************************************
    # Return the table of operations for the extension.
    #*****************************************************************************
    @classmethod
    @abstractmethod
    def Table(cls):
        pass

    #*****************************************************************************
    # Print the help information for the extension.
    #*****************************************************************************
    @classmethod
    @abstractmethod
    def Help(cls):
        pass
      
    #*****************************************************************************
    # Return the name of the extension.
    #*****************************************************************************
    @property
    def Name(cls):
        # Prefer explicit __Name__ if set, else fallback to class name
        if hasattr(cls, '__Name__') and getattr(cls, '__Name__') is not None:
            return cls.__Name__
        return cls.__class__.__name__
    
    #*****************************************************************************
    # Return the version of the extension.
    #*****************************************************************************
    @property
    def Version(cls):
        if hasattr(cls, '__Version__') and getattr(cls, '__Version__') is not None:
            return cls.__Version__
        return cls.__class__.__name__

    #*****************************************************************************
    # Return the author of the extension.
    #*****************************************************************************
    @property
    def Author(cls):
        return cls.__Author__    

    #*****************************************************************************
    # Return the status of the extension.
    #*****************************************************************************
    @property
    def Status(cls):
        return cls.__Status__
