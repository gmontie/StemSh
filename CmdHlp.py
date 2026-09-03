#!/usr/bin/env python3

# Include path to modules Library
import platform
import sys

import platform
import sys
Platform = platform.system()
#print("Platform: ", Platform)
if ('CYGWIN_NT' in Platform): #-10.0-22631'):
    sys.path.append('/usr/local/Lib/Python')
elif ('Windows' in Platform):
    sys.path.append("C:\\Lib\\Python")
elif ('Linux' in Platform):
    sys.path.append('/usr/local/Lib/Python')


from COLORS import RED, GREEN, YELLOW, WHITE # type: ignore

# =================================================================================================
# Constants
# =================================================================================================
PRMT='\r\n'

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
   'wait <' + GREEN + 'time' + WHITE + '>                              ' + \
      RED + '# Delay <' + GREEN + 'time' + RED + '> before executing the ',
   '                                                            ',
   '<' + GREEN + 'var' + WHITE +'> = <' + GREEN + 'value' + WHITE +\
      '>                          ' + RED + '# Set variable <' + GREEN +\
      'var' + RED + '> to <' + GREEN + 'value' + RED + '>',
   '<' + GREEN + 'list vars' + WHITE + '>   ' + RED +\
      '                           # list all '+ GREEN + 'variables' + RED + ' in memory',
   '<' + GREEN + 'save' + WHITE +'> <'+YELLOW+'Name'+ WHITE+'><'+GREEN+'.'+WHITE+'><'+YELLOW+\
      'Extension' + WHITE + '>              ' + \
      RED + '# Where ' + YELLOW + 'Name' + GREEN + '.' + YELLOW + 'Extension' + RED + ' is a',
   '                                         ' + RED + '# ' + YELLOW + 'File Name' + RED + ' that all variables in memory will be saved to',
   '  ',
   '<' + GREEN + 'load' + WHITE +'> <'+YELLOW+'Name'+ WHITE+'><'+GREEN+'.'+WHITE+'><'+YELLOW+\
      'Extension' + WHITE + '>              ' + \
      RED + '# Where ' + YELLOW + 'Name' + GREEN + '.' + YELLOW + 'Extension' + RED + ' is a' + YELLOW + 'File Name' + RED + ' that variables will be loaded from',   
   '                                                            ',
   '<' + YELLOW + 'NUMBER' + WHITE + '>  {' + GREEN + 'any command' + WHITE + '}' + \
      '                  ' + \
      RED + '# Is a how a ' + YELLOW +'line' + RED + ' of ' + GREEN + 'programming code' + RED+' is entered',
   '  ',  
   '<' + GREEN + 'list' + WHITE + '>                                   ' +\
      RED + '# Lists all '+GREEN+'programming '+YELLOW+'lines'+RED+' in memory',
   '<' + GREEN + 'list' + WHITE + '><' + YELLOW + "vars" + WHITE + ">                             "+\
      RED + '# Lists all '+GREEN+'variables '+RED+' in memory',
   '<' + GREEN + 'list' + WHITE + '><' + YELLOW + "ext" + WHITE + ">                              "+\
      RED + '# Lists all '+GREEN+'current extension or plugin\'s '+YELLOW+'currently'+RED+' existing in memory',
   '  ',  
   '<' + GREEN + 'program save' + WHITE +'> <'+YELLOW+'Name'+ WHITE+'><' + GREEN + '.' + WHITE + '><' + YELLOW + \
      'Extension' + WHITE+ '>      ' + \
      RED+'# Where '+YELLOW+'Name'+GREEN+'.' + YELLOW + 'Extension' + RED + ' is the ' + YELLOW + 'File Name' + RED + ' that program in memory',
   '                                         ' + RED + '# will be saved to',
   '  ',
   '<' + GREEN + 'program load' + WHITE +'> <' + YELLOW + 'Name' + WHITE + '><' + GREEN + '.' + WHITE + '><' + YELLOW + \
      'Extension' + WHITE+ '>      '+\
      RED + '# Where ' + YELLOW + 'Name' + GREEN + '.' + YELLOW + 'Extension' + RED + ' is a ' + YELLOW + 'File Name' + RED + ' that program',
   '                                         '+RED+'# code will be loaded from',
   '  ',
   '<' + GREEN + 'run' + WHITE +'>                                    '+\
      RED+'# Runs the program currently in memory',
   '<' + GREEN + 'run' + WHITE +'> <'+YELLOW+'Name'+ WHITE+'><'+GREEN+'.'+WHITE+'><'+YELLOW+\
   'Extension' + WHITE+ '>               '+\
      RED + '# Where '+YELLOW+'Name'+GREEN+'.'+YELLOW+'Extension'+RED+' is a',
   '                                         '+RED+'# '+YELLOW+'File Name'+RED+' that program',
   '                                         '+RED+'# code will be loaded into',   
   '                                         '+RED+'# memory from and then executed',
   '                                                            ',
   'help                                     ' + RED +\
      '# Print this help list',
   '?                                        ' + RED +\
      '# Print this help list',
   '                                                            ',
   'quit                                     ' + RED +\
      '# Quit/Exit program',
   '!                                        ' + RED +\
      '# Quit/Exit program',
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
