#!/usr/bin/env python3

# Include path to modules Library
import platform
import sys

import platform
import sys
Platform = platform.system()
if ('CYGWIN_NT' in Platform): # type: ignore
    sys.path.append('/usr/local/Lib/Python')
elif ('Windows' in Platform): # type: ignore
    sys.path.append("C:\\Lib\\Python")
elif ('Linux' in Platform): # type: ignore
    sys.path.append('/usr/local/Lib/Python')

from COLORS import RED, GREEN, YELLOW, WHITE # type: ignore

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

HelpLines= \
[  ' ',
   YELLOW + '---------------------------------------------------------------------------', 
   'CAT <' + GREEN + 'File' + WHITE + '>            ' + \
      RED + '# Unix type cat <' + GREEN + 'File' + RED + '> to terminal ',
   'CD <' + GREEN + 'Path' + WHITE + '>             ' + \
      RED + '# Change Directory <' + GREEN + 'Path' + RED + '> to new location ',
   'File Sys Clear ' + '       ' + \
      RED + '# Reset the File Extentions internals  ',
   'DIR                   ' + \
      RED + '# Output the ' + GREEN + 'Directory listing ' + RED + 'to terminal ',
   'LS                    ' + \
      RED + '# List the current ' + GREEN + 'Directory Contents' + RED + ' to the terminal ',
   'PWD                   ' + \
      RED + '# Print the ' + GREEN + 'Current Working Directory' + RED + ' to the terminal ',
   'ENV                   ' + \
      RED + '# print the ' + GREEN + 'environment' + RED + ' to the terminal ',
   'File Sys Help         ' + \
      RED + '# Print this command list to the terminal ', 
   YELLOW + '---------------------------------------------------------------------------', 
   ' ']

#**************************************************************************
#
#**************************************************************************
class Help:
   def __init__(self):
      pass

   #**************************************************************************
   #
   #**************************************************************************
   @classmethod
   def Usage(self, Args=None):
      for Line in HelpLines:
         print(Line)

   #**************************************************************************
   #
   #**************************************************************************
   @property
   def getHelp(self):
      return HelpLines
