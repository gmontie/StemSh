#!/usr/bin/env python3

# ============================================================================
# import global/system modules ect
from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style

BLACK=Fore.BLACK 
RED=Fore.RED 
GREEN=Fore.GREEN 
YELLOW=Fore.YELLOW 
BLUE=Fore.BLUE 
MAGENTA=Fore.MAGENTA 
CYAN=Fore.CYAN 
WHITE=Fore.WHITE
BOLD=Style.BRIGHT
RESET=Style.RESET_ALL
DIM=Style.DIM

# ==========================================================================================
# MetAdATa
# ==========================================================================================
__author__ = "Greg Montgomery"
__version__ = "3.2.0"
__status__ = "Development"

class Colorizer(object):
    def __init__(self):
        pass
    
    #============================================================================================
    # """ addStr is at the hart of cprint. It will transform several different types into strings """
    #============================================================================================
    """ addStr is at the hart of cprint. It will transform 
        several different types into strings """
    def addStr(self, *Args):
        return self.ConvertToStr(*Args)

    # =========================================================================================
    # Color Print
    # =========================================================================================
    def cprint(self, *Args):
        print(self.ConvertToStr(*Args))

    #==========================================================================================
    # Convert various types to string
    #==========================================================================================
    def ConvertToStr(self, *Args):
        Msg=''
        for Item in Args:
            theType = type(Item).__name__
            if theType == 'str':
                Msg += Item
            elif theType == 'int' or \
                theType == 'float' or \
                theType == 'complex':
                Msg += str(Item)
            elif theType == 'list':
                Msg += '[ '
                for Element in Item:
                    Msg += (self.ConvertToStr(Element) + ' ,')
                Msg += ' ]'
            elif theType == 'dict':
                Keys = Item.keys()
                #if len(Keys) > 0:
                Msg += '{'
                for Key in Keys:
                    Msg += self.ConvertToStr(Key)
                    Msg += ' : '
                    Msg += self.ConvertToStr(Item[Key])
                    Msg += ' ,'
                Msg += ' }'
            elif theType == 'tuple':
                Msg += '( '
                for Element in Item:
                    Msg += (self.ConvertToStr(Element) + ' ,')
                Msg += ' )'
            elif theType == 'bytes':
                Lst = []
                for Bt in Item:
                    if((Bt < 0x20) or ( 0x7F < Bt)):
                        Lst+=' '
                    else:
                        Lst = Bt.decode("utf-8")
                Msg += self.ConvertToStr(Lst) 
            elif theType == 'bytearray':
                Msg += bytes(Item).decode('utf-8')
            elif theType == 'bool':
                if Item == True:
                    Msg += "Bool - True"
                else:
                    Msg += "Bool - False"
            else:
                print(type(Item).__name__)
                Msg += str(Item)
                Str = ">" + type(Item).__name__ + "<"
                Msg += Str
        return Msg

    # ===============================================================================
    #
    # ===============================================================================
    def PrntAt(self, Where = 0, What=''):
        Spaces=Where
        Length=len(What)
        if Length < Spaces:
            Spaces -= Length
        return f"{self.addSpace(Spaces)}{What}"

    # =============================================================================
    # 
    # =============================================================================
        """ Add space will subtract the length of the Str pass in from the desired 
            location to print the next piece of output indicated by Nbr """
    def addSpaces(self, Where = 0, What=''):
        Results = ""
        Length = len(What)
        if Length < Where:
            Where -= Length
            Results = self.addSpace(Where)
        return Results

    # =============================================================================
    # 
    # =============================================================================
        """ Add space will subtract the length of the Str pass in from the desired 
            location to print the next piece of output indicated by Nbr """
    def addSpce(self, Nbr, Str):
        Results = ""
        Length = len(Str)
        if Length < Nbr:
            Nbr -= Length
            for i in range(Nbr):
                Results += ' '
        return Results

    
    # =============================================================================
    # 
    # =============================================================================
        """ Add space will subtract the length of the Str pass in from the desired 
            location to print the next piece of output indicated by Nbr """
    def addSpace(self, Nbr):
        Results = ""
        for i in range(Nbr):
            Results += ' '
        return Results

    # =============================================================================
    # 
    # =============================================================================
        """ Return true if the item 'Color' is a defined Color from above """
    def isColor(self, Color):
        if Color in ['BOLD','RESET','DIM','BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE']:
            return True
        else:
            return False

