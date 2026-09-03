#!/usr/bin/python3
import platform
import sys

Platform = platform.system()
if ('CYGWIN_NT' in Platform):  # type: ignore
    sys.path.append('/usr/local/Lib/Python')
elif ('Windows' in Platform): # type: ignore
    sys.path.append("C:\\Lib\\Python")
elif ('Linux' in Platform): # type: ignore
    sys.path.append('/usr/local/Lib/Python')

import code
import os

from colorama import init
from colorama import Fore

PRMT='\r\n'
GREEN=Fore.GREEN
YELLOW=Fore.YELLOW
WHITE=Fore.WHITE
RED=Fore.RED
BLUE=Fore.BLUE
MAGENTA=Fore.MAGENTA
CYAN=Fore.CYAN
BLACK=Fore.BLACK

ColorsToVT200={
        'RED':"\001" + RED + "\002",
        'BLUE':"\001" + BLUE + "\002",
        'YELLOW':"\001" + YELLOW + "\002",
        'MAG':"\001" + MAGENTA + "\002",
        'MAGENTA':"\001" + MAGENTA + "\002",
        'GREEN':"\001" + MAGENTA + "\002",
        'CYN':"\001" + CYAN + "\002",
        'CYAN':"\001" + CYAN + "\002",
        'WHITE':"\001" + WHITE + "\002",
        'BLACK':"\001" + BLACK + "\002"
        }

#=============================================================================
class KeyboardPrompt(code.InteractiveConsole):
    def __init__(self, Prmt, pColor=None, filename="<console>", HistFile=os.path.expanduser("~/.history")):
        init(autoreset=True)
        if pColor != None:
            if pColor in ColorsToVT200.keys():
                _Color=ColorsToVT200[pColor.upper()]
            else:
                print("Unknown Color for Prompt -->",pColor)
                print("Program exiting")
                exit( 0 )
        else:
           _Color=ColorsToVT200['WHITE']
        self._prompt=_Color + Prmt + WHITE
        code.InteractiveConsole.__init__(self, locals, filename)

    #=========================================================================
    @classmethod
    def on_press(self, key):
        print( '{0} pressed'.format(key) )

    #=========================================================================
    @classmethod
    def on_release(self, key):
        print( '{0} release'.format( key ) )
        if key == Key.esc:
            # Stop listener
            return False

    #=========================================================================
    @classmethod
    def OnKeyPress(self, key):
        Results = key
        return Results

    #=========================================================================
    @classmethod
    def onKeyRelease(self, key):
        print('{0} release'.format(key))
        if key == Key.esc:
            # Stop listener
            return False

    #=========================================================================
    @classmethod
    def getKey(self):
        # Collect events until released
        with Listener( on_press = self.OnKeyPress, on_release = self.onKeyRelease) as listener:
            listener.join()

        return key

    #=========================================================================
    def Prompt(self, Fin=None):
        Line=""
        if Fin != None:
            cprint(YELLOW, self._prompt, WHITE )
            for Line in sys.stdin:
                pass
        else:
            Line = input(self._prompt)
        return Line

    #=========================================================================
    @classmethod
    def asyncPrompt(self, Fin=None):
        Line=""
        if Fin != None:
            cprint(self.Color, self._prompt, WHITE, end='' )
            Line=yield from Fin.readline()
        else:
            Line=yield from input(self._prompt)
        return Line

    #=========================================================================
    @classmethod
    def Echo(self, Str):
        print('\n',Str)

    #=========================================================================
    @property
    def Prmt(self):
        return self._prompt
