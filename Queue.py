# Include path to modules Library
import sys
#import os
import platform
Platform = platform.system()
if ('CYGWIN_NT' in Platform):
    sys.path.append('/usr/local/Lib/Python')
elif ('Windows' in Platform):
    sys.path.append("C:\\Lib\\Python")
elif ('Linux' in Platform):
    sys.path.append('/usr/local/Lib/Python')

import copy

# ============================================================================
# Local module/classes imported from here down.

# Colorizer to colorize output
from Colorizer import Colorizer # type: ignore
from COLORS import BOLD, GREEN, RED, BLUE, YELLOW, WHITE, MAGENTA, CYAN, RESET # type: ignore

# ===============================================================================================
# MEtADAtA
# ===============================================================================================
__author__ = "Greg Montgomery"
__version__ = "1.0.0"
__status__ = "Development"

""" 
============================================================================
 Class 
        Stack
          
============================================================================
"""

cprint = Colorizer().cprint

#*****************************************************************************
# Stack Class
#*****************************************************************************
class Queue(object):
    def __init__(self, items = None):
        self.q = []
        self.Count = 0
        self.Index = 0
        if items is not None:            
          if type(items).__name__ == 'list':
            self.q.append(items.copy()) 
          else:
            print("Queue.py:57 Type --> ",type(items).__name__)
  
    #*****************************************************************************
    # Add an element to the end of the Queue
    #*****************************************************************************
    def Enqueue(self, Element):
        self.Count += 1
        self.q.insert(0, Element)

    #*****************************************************************************
    # Remove an element from the front of the Queue
    #*****************************************************************************
    def Dequeue(self):
        self.Count -= 1
        return self.q.pop(-1)
  
    #*****************************************************************************
    # Clear the Queue
    #*****************************************************************************
    def Clear(self):
        self.q = []

    #*****************************************************************************
    # Return the next element in the Queue
    #*****************************************************************************
    def Next(self):
        Result = None
        if self.Count > 0:
            Result = self.q[-1]
        return Result

    #*****************************************************************************
    # Return true if the Queue is empty
    #*****************************************************************************
    @property
    def isEmpty(self):
        return self.q == []
  
    #*****************************************************************************
    # Return the number of elements in the Queue
    #*****************************************************************************
    @property
    def Size(self):
        return self.Count
    
    #*****************************************************************************
    # Return the representation for the queue
    #*****************************************************************************
    @property
    def getList(self):
        return copy.deepcopy(self.q)
