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
 
          
============================================================================
"""

HelpLines= \
[  ' ',
   YELLOW + '---------------------------------------------------------------------------', 
   '<' + GREEN + 'program save' + WHITE +'> <'+YELLOW+'Name'+ WHITE+'><' + GREEN + '.' + WHITE + '><' + YELLOW + \
      'Extension' + WHITE+ '>      ' + \
      RED+'# Where '+YELLOW+'Name'+GREEN+'.' + YELLOW + 'Extension' + RED + ' is the ' + YELLOW + 'File Name' + RED + ' that program in memory will be saved to',
   '<' + GREEN + 'program load' + WHITE +'> <' + YELLOW + 'Name' + WHITE + '><' + GREEN + '.' + WHITE + '><' + YELLOW + \
      'Extension' + WHITE+ '>      '+\
      RED + '# Where ' + YELLOW + 'Name' + GREEN + '.' + YELLOW + 'Extension' + RED + ' is a ' + YELLOW + 'File Name' + RED + ' that program code will be loaded from',
   '  ',
   '<' + GREEN + 'save' + WHITE +'> <' + YELLOW + 'Name' + WHITE + '><' + GREEN + '.' + WHITE + '><' + YELLOW + \
      'Extension' + WHITE + '>              ' + \
      RED + '# Where ' + YELLOW + 'Name' + GREEN + '.' + YELLOW + 'Extension' + RED + ' is a ' + YELLOW + \
          'File Name' + RED + ' that all variables in memory will be saved to',
   '<' + GREEN + 'load' + WHITE + '> <' + YELLOW + 'Name' + WHITE + '><' + GREEN + '.' + WHITE + '><' + YELLOW + \
      'Extension' + WHITE + '>              ' + \
      RED + '# Where ' + YELLOW + 'Name' + GREEN + '.' + YELLOW + 'Extension' + RED + ' is a ' + YELLOW + 'File Name' + RED + ' that variables will be loaded from',   
   '                                                            ',
   '<' + YELLOW + 'NUMBER' + WHITE + '>  {' + GREEN + 'any command' + WHITE + '}' + \
      '                  ' + \
      RED + '# Is a how a ' + YELLOW +'line' + RED + ' of ' + GREEN + 'programming code' + RED+' is entered',
   '                                                            ',
   '<' + GREEN + 'list' + WHITE + '>                                   ' +\
      RED + '# Lists all ' + GREEN + 'programming ' + YELLOW + 'lines' + RED + ' in memory',
   '<' + GREEN + 'list' + WHITE + '><' + YELLOW + "vars" + WHITE + ">                             " + \
      RED + '# Lists all ' + GREEN + 'variables ' + RED + ' in memory',
   '<' + GREEN + 'list' + WHITE + '><' + YELLOW + "ext" + WHITE + ">                              " + \
      RED + '# Lists all ' + GREEN + 'current extension or plugin\'s ' + YELLOW + 'currently' + RED + ' existing in memory',
   '  ',  
   '<' + GREEN + 'run' + WHITE +'>                                    '+\
      RED+'# Runs the program currently in memory',
   '<' + GREEN + 'run' + WHITE + '> <' + YELLOW + 'Name' + WHITE + '><' + GREEN + '.' + WHITE + '><' + YELLOW + \
   'Extension' + WHITE+ '>               '+\
      RED + '# Where ' + YELLOW + 'Name' + GREEN + '.' + YELLOW + 'Extension' + RED + ' is a ' + YELLOW + 'File Name' + RED + ' that contains program code',
  RED + '                                         # to be loaded into memory.',
   '                                                            ',
   'wait <' + GREEN + 'time' + WHITE + '>                              ' + \
      RED + '# Delay <' + GREEN + 'time' + RED + '> before executing the next line of code or delaying the next user input',
  '  ',
  '<' + GREEN + 'var' + WHITE +'> = <' + GREEN + 'value' + WHITE + '>                          ' + RED + '# Set variable <' + GREEN + 'var' + RED + '> to <' + GREEN + 'value' + RED + '>',
  '<' + GREEN + 'var' + WHITE +'> = <' + GREEN + 'expression' + WHITE + '>                     ' + RED + '# Set variable <' + GREEN + 'var' + RED + '> to the results of evaluating <' + GREEN + 'expression' + RED + '>',
  '  ',  
  '<' + GREEN + 'ren' + WHITE +'>                                    ' + RED + '# Renumber all of the lines of the current program which is in memory',
  '  ',  
   '?                                        ' + RED + '# Print this help list',
   '                                                            ',
   'quit                                     ' + RED + '# Quit/Exit program',
   '!                                        ' + RED + '# Quit/Exit program',
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
