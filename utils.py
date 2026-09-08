#!/usr/bin/env python3

# ============================================================================
# import global/system modules ect
import binascii
import os
import sys
import termios

# ===============================================================================================
# MEtADAtA
# ===============================================================================================
__author__ = "Greg Montgomery"
__version__ = "1.0.0"
__status__ = "Development"


""" 
============================================================================
 Class Utilities
 
 Provides: a set of miscellaneous methods and enhanced functionality
           for python 3 classes and modules
           
============================================================================
"""

class Utilities:
   def __init__(self):
      self.__Scratch=0
      self.__Mask=0
      self.__Result=0
      self.__xLocal=0
      self.__yLocal=0
      self.__LineLen=0
                  
   #=========================================================================
   @classmethod
   def pHexify(self, Message, Buffer):
      x=binascii.hexlify(Buffer)
      print(Message, x)

   #=========================================================================
   @classmethod
   def pHexify_(self, Message, Buffer):
      x=binascii.hexlify(Buffer)
      print(Message, x, end='')

   #=========================================================================
   @classmethod
   def Hexify(self, Buffer):
      __Scratch__=binascii.hexlify(Buffer)
      return __Scratch__.decode("utf-8")

   #=========================================================================
   @classmethod
   def byteAnd(self, data, mask):
      Results=B'\x00'
      if not type(data).__name__ == 'bytes':
         raise self.typeError( "Wrong Type: (%s) expected type: (bool)" % __name__)
      else:
         if not type(mask).__name__ == 'bytes':
            raise self.typeError( "Wrong Type: (%s) expected type: (bool)" % __name__)
         else:
            self.__Scratch = int.from_bytes(data,'little')
            self.__Mask = int.from_bytes(mask,'little')
            self.__Result = self.Scratch & self.Mask
            Results=bytes([self.__Result])
      return Results
   
   #=========================================================================
   @classmethod
   def byteOr(self, data, mask):
      Results=B'\x00'
      if not type(data).__name__ == 'bytes':
         raise self.typeError( "Wrong Type: (%s) expected type: (bool)" % __name__)
      else:
         if not type(mask).__name__ == 'bytes':
            raise self.typeError( "Wrong Type: (%s) expected type: (bool)" % __name__)
         else:
            self.__Scratch = int.from_bytes(data,'little')
            self.__Mask = int.from_bytes(mask,'little')
            self.__Result = self.__Scratch | self.__Mask
            Results=bytes([self.__Result])
      return Results
   
   #=========================================================================
   @classmethod
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
         key = os.read(fd, 3)
      finally:
         termios.tcsetattr(fd, termios.TCSAFLUSH, old)
      
      return key
