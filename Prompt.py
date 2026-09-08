#!/usr/bin/python3
import platform
import sys

Platform = platform.system()
if ('CYGWIN_NT' in Platform):  # type: ignore
    sys.path.append('/usr/local/Lib/Python')
elif ('Windows' in Platform):  # type: ignore
    sys.path.append("C:\\Users\\greg.montgomery\\Development\\Lib\\Python")
elif ('Linux' in Platform):  # type: ignore
    sys.path.append('/usr/local/Lib/Python')

import os
import readline
import atexit 
import code
import termios

# Colorizer to colorize output
from Colorizer import Colorizer # type: ignore
from COLORS import BOLD, BLACK, GREEN, RED, BLUE, YELLOW, WHITE, MAGENTA, CYAN, RESET # type: ignore

cprint = Colorizer().cprint
addStr = Colorizer().addStr

class KeyboardPrompt(code.InteractiveConsole):
   def __init__(self, Prmt, pColor=None, filename="<console>", HistFile=os.path.expanduser("~/.history")):
      #init(autoreset=True)
      if pColor != None:
         Color=pColor.upper()
         if Color=='RED':
            _Color="\001" + RED + "\002"
         elif Color=='BLUE':
            _Color="\001" + BLUE + "\002"
         elif Color=='YELLOW':
            _Color="\001" + YELLOW + "\002"
         elif Color=='MAG' or Color=='MAGENTA':
            _Color="\001" + MAGENTA + "\002"
         elif Color=='GREEN':
            _Color="\001" + GREEN + "\002"
         elif Color=='CYN' or Color=='CYAN':
            _Color="\001" + CYAN + "\002"
         elif Color=='WHITE':
            _Color=="\001" + WHITE + "\002"
         elif Color=='BLACK':
            _Color="\001" + BLACK + "\002"
         else:
            print("Unknown Color for Prompt -->",pColor)
            print("Program exiting")
            exit( 0 )
      else:
         Color=WHITE
      self._prompt=_Color + Prmt + WHITE
      self.HistFile=HistFile
      self.History=[]
      self.HistoryCount=0
      self.readling=None
      code.InteractiveConsole.__init__(self, locals, filename)
      self.init_history(self.HistFile)

   #=========================================================================
   def init_history(self, histfile):
      self.readling=readline
      readline.parse_and_bind("tab: complete")
      if hasattr(readline, "read_history_file"):
         try:
             readline.read_history_file(histfile)
         except FileNotFoundError:
             pass
         atexit.register(self.save_history, histfile)

   #=========================================================================
   def save_history(self, histfile):
      readline.set_history_length(100)
      readline.write_history_file(histfile)

  #=========================================================================
   def getKey(self):
      fd = sys.stdin.fileno()
      old = termios.tcgetattr(fd)
      new = termios.tcgetattr(fd)
      new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
      new[6][termios.VMIN] = 1
      new[6][termios.VTIME] = 0
      termios.tcsetattr(fd, termios.TCSANOW, new)
      key = None

      try:
         key = os.read(fd, 1)
      finally:
         termios.tcsetattr(fd, termios.TCSAFLUSH, old)

      return key

   #=========================================================================
   def ClearHist(self):
      self.readling.clear_history()

   #=========================================================================
   def PrntHist(self):
      Counter=readline.get_current_history_length()
      #self.History=readline.history_get()
      for i in range(Counter):
         Entry=readline.get_history_item(i)
         print(i,') ',Entry)

   #=========================================================================
   def Prompt(self, Fin=None):
      GettingLine=True
      HistoryIndex=self.HistoryCount
      Line=""
      if Fin != None:
         print(self._prompt, end='' )
         Line=Fin.readline()
      else:
         Line=input(self._prompt)
      return Line

   #=========================================================================
   def asyncPrompt(self, Fin=None):
      GettingLine=True
      HistoryIndex=self.HistoryCount
      Line=""
      if Fin != None:
         print(self._prompt, end='' )
         Line=yield from Fin.readline()
      else:
         Line=yield from input(self._prompt)
      return Line

  #=========================================================================
   def Echo(self, Str):
      print('\n',Str)

  #=========================================================================
   @property
   def Prmt(self):
      return self._prompt
