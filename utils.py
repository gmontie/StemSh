#!/usr/bin/env python3

# ============================================================================
# import global/system modules ect
#import crc16
import struct
import binascii
import os
import sys
import termios
import serial, glob
 
# ===============================================================================================
# MEtADAtA
# ===============================================================================================
__author__ = "Greg Montgomery"
__version__ = "0.1.0"
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
   def pHexify(self, Message, Buffer):
      x=binascii.hexlify(Buffer)
      print(Message, x)

   #=========================================================================
   def pHexify_(self, Message, Buffer):
      x=binascii.hexlify(Buffer)
      print(Message, x)

   #=========================================================================
   def Hexify(self, Buffer):
      __Scratch__=binascii.hexlify(Buffer)
      return __Scratch__.decode("utf-8")

   #=========================================================================
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
   def scan(self):
      # scan for available ports. return a list of device names.
      return glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*')

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
         key = os.read(fd, 3)
      finally:
         termios.tcsetattr(fd, termios.TCSAFLUSH, old)

      return key

   #=========================================================================
   # CRC
   #def CRC(self, data):
   #   crc = crc16.crc16xmodem(data)
   #   return crc, struct.pack('<H', crc)
