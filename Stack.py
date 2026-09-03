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

# from COLORS import RED
# from COLORS import WHITE
# from COLORS import YELLOW
# from COLORS import GREEN
# from Colorizer import Colorizer # type: ignore


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


#*****************************************************************************
# Stack Class
#*****************************************************************************
class Stack(object):
    """
    Last in first out (LIFO) stack implemented using array.
    """
    def __init__(self, Capacity=400):
        """
        Initialize an empty stack array with default Capacity of 4.
        """
        self.Items = []
        self.Capacity = Capacity
        self.Count = 0
        self.Top  = -1

    #*****************************************************************************
    # Push method
    #*****************************************************************************
    def Push(self, Value):
        """
        Add a Value to the Top.
        """
        if self.Top < self.Capacity:
            self.Items.append(Value)
            self.Top += 1

    #*****************************************************************************
    # Pop method
    #*****************************************************************************
    def Pop(self):
        """
        Return and remove Element from the Top.
        """
        Results = None
        if not self.Empty:
            Results = self.Items.pop()
            self.Top -= 1
        return Results

    #*****************************************************************************
    # 
    #*****************************************************************************
    @property
    def Copy(self):
        return copy.deepcopy(self.Items)

    #*****************************************************************************
    # Peek at the top of the stack
    #*****************************************************************************
    @property
    def Peek(self):
        """
        Return Element at the Top.
        """
        Results = None
        if not self.Empty:
            Results = self.Items[ -1 ]
        return Results

    #*****************************************************************************
    # Return the size of the Stack
    #*****************************************************************************
    @property
    def Size(self):
        """
        Return the number of items present.
        """
        return len(self.Items)
    
    #*****************************************************************************
    # Return true if the Stack is empty
    #*****************************************************************************
    @property
    def Empty(self):
        """
        Return true if the Size of stack is zero.
        """
        Results = False
        if len(self.Items) == 0:
            Results = True
        return Results

    #*****************************************************************************
    # Return true if the Stack is full
    #*****************************************************************************
    @property
    def Full(self):
        """
        Return true if the Size has reached Capacity.
        """
        Results = False
        if len(self.Items) >= self.Capacity:
            Results = True
        return Results  
    
    #*****************************************************************************
    # Return the representation for the stack
    #*****************************************************************************
    @property
    def getList(self):
        return self.Items
