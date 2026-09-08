#!/usr/bin/python3

# Include path to modules Library
import sys

from Stack import Stack

from COLORS import BOLD, GREEN, RED, BLUE, YELLOW, WHITE, RESET # type: ignore
from Colorizer import Colorizer # type: Ignore


#│▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
#│▒                                                                              ▒│
#│▒          MetAdATa                                                            ▒│
#│▒                                                                              ▒│
#│▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
__author__ = "Greg Montgomery"
__version__ = "2.0.0"
__status__ = "Development"

cprint = Colorizer().cprint
addStr = Colorizer().addStr

#*****************************************************************************
# Binary Tree Class
# *****************************************************************************
class BTree:
    def __init__(self, Type, NewValue=None):
        self.Value=NewValue
        self.Type=Type
        self.Left=None
        self.Right=None
        self.Stack = Stack()

    #*****************************************************************************
    # Action: Print the Binary Tree
    #*****************************************************************************
    def Print(self, Tree, Level=0):
        if Tree != None:
            String = addStr("Type:", Tree.Type, "  Value:", Tree.Value)
            self.Stack.Push(String)
            String = [" / "," \\"] # type: ignore
            self.Stack.Push(String)
            if Tree.Left != None:
                self.Print(Tree.Left, Level + 1)
            if Tree.Right != None:

                self.Print(Tree.Right, Level + 1)
            print("Level ", Level)
            if Level == 0:
                Lst = self.Stack.getList
                for Item in Lst:
                    print(Item)

    #*****************************************************************************
    # Return or Set the left child of the node
    # *****************************************************************************
    @property
    def left(self):
        return self.Left
    @left.setter
    def left(self, value):
        self.Left=value

    #*****************************************************************************
    # Return or Set the right child of the node
    # *****************************************************************************
    @property
    def right(self):
        return self.Right
    @right.setter
    def right(self, value):
        self.Right=value

    #*****************************************************************************
    # Return the Trees Value
    # *****************************************************************************
    @property
    def value(self):
        return self.Value

    #*****************************************************************************
    # Return the Trees Type
    # *****************************************************************************
    @property
    def type(self):
        return self.Type
