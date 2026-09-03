#!/usr/bin/python3

# Include path to modules Library
from datetime import datetime
import platform
Platform = platform.system()
import sys
if ('CYGWIN_NT' in Platform): # type: ignore
    sys.path.append('/usr/local/Lib/Python')
elif ('Windows' in Platform): # type: ignore
    sys.path.append("C:\\Lib\\Python")
elif ('Linux' in Platform): # type: ignore
    sys.path.append('/usr/local/Lib/Python')

import sympy as sp
import numpy as np
import operator
import datetime
import time

# ============================================================================
# Local module/classes imported from here down.
# ============================================================================
from SlyLexer import Tokenize
from BTree import BTree
from sly import Parser
from Queue import Queue
from Stack import Stack

from COLORS import BOLD, RESET, WHITE, RED, YELLOW, BLUE, GREEN, CYAN, MAGENTA  # type: ignore
from Colorizer import Colorizer # type: ignore

# ===============================================================================================
# MEtADAtA
# ===============================================================================================
__author__ = "Greg Montgomery"
__version__ = "1.0.0"
__status__ = "Development"

""" 
============================================================================
 Class The Parser
 
          
============================================================================
"""
cprint = Colorizer().cprint
addStr = Colorizer().addStr
isColor = Colorizer().isColor

class theParser(Parser):
    debugfile = 'parser.out'
    tokens = Tokenize.tokens

    precedence = (
            ('left', 'ADD_OP', 'SUB_OP'),
            ('left', 'ADD_ASGN', 'SUB_ASGN'),
            ('left', 'MUL_ASGN', 'DIV_ASGN'),
            ('left', 'MUL_OP', 'BACKSLASH_OP'), 
            ('left', 'POW_OP'),
            ('right', 'UTILDE'),
            ('right', 'UMINUS'),
            ('left', 'SHFT_LEFT', 'SHFT_RIGHT'),
            ('left', 'BANG'),
            )

    # ========================================================================#
    #                                                                         #
    # ========================================================================#
    #def __init__(self, Prmt=None, Vars=None, args=None, **kwargs):
    def __init__(self, Vars=None, args=None, **kwargs):
        super().__init__()
        self.pArgs=args
        self.Vars=Vars
        self.Lines=[]
        self.PArgs=[]
        self.Stack=Stack()
        self.Queue=Queue()
        self.Line=''
        self.OpAsnMap = {"+=":"+",
                         "-=":"-",
                         "*=":"*",
                         "/=":"/"}
        self.Space = "                                                                                                                                         "
        self.Queue = Queue()
        self.prntLn = False
        self.TimeNow = datetime.datetime.now()
    
    # ========================================================================#
    #                                                                         #
    # ========================================================================#
    def Clear(self):
        self.prntLn = True
        if self.Stack.Size > 0:
            self.Stack = Stack()
        if self.Queue.Count > 0:
            self.Queue = Queue()

    # ========================================================================#
    #                                                                         #
    # ========================================================================#
    @property
    def OutPut(self):
        return self.prntLn
    
    # ========================================================================#
    #                                                                         #
    # ========================================================================#
    def SetLine( self, Line ):
        if '=' in Line:
            self.Line = Line.split('=')[1].strip()
        else:
            self.Line = Line
    
    # ========================================================================#
    # Error handling rule                                                     #
    # ========================================================================#
    def error(self, t):
        Token = ""
        Msg = addStr(RED, "Syntax Error: ")
        print(Msg, "@ -->", t, "<--\n")
        
        if t != None:
            Token = t
            while Token != None:
                Msg = addStr(YELLOW, "Token: ")
                print(Msg, Token)
                Token = next(self.tokens, None) # Get the next token 
#        exit(0)

    # ========================================================================#
    #                                                                         #
    # ========================================================================#
    def unrollP(self, p, Msg=None):
        if Msg:
            print(Msg)        
        for i in range(len(p)):
            Str = "p[" + str(i) + "]"
            print(Str, p[i], ";", end=' ')
        print(" ")

    # ========================================================================#
    #                                                                         #
    # ========================================================================#
    @_('Statement',  # type: ignore
       'empty',
       'Built_In',
       'Line')
    def TOP_LEVEL(self, p):
        Results = None
        # self.unrollP(p)
        if type(p[0]).__name__ == 'BTree':
            Results = p[0]
        elif type(p[0]).__name__ == 'list':
            Results = tuple(p[0])
        elif type(p[0]).__name__ == "tuple":
            Results = p[0]
        elif type(p[0]).__name__ == 'str':
            Results = p[0]
        else:
            print("Top Leve Undefined")
            self.unrollP(p)
            Results = p
        return Results
    
    @_('') # type: ignore
    def empty(self, p):
        return "Done"
 
    # Imediate Operations
    @_('List_BuiltIn','list_vars',  # type: ignore
       'list_prog', 'List_Extentions',
       'NEW','REN','ENV','NOW','Quit',
       'HELP', '?','CLEAR')
    def Built_In(self, p):
        p="BuiltIn", p[0].upper()
        return p

    @_('RUN') # type: ignore
    def Built_In(self, p): # BuiltIn, Command=RUN, Argument=RUN
        return "BuiltIn", "RUN", 'RUN'

    @_('CAT QualifiedFileName','FILE QualifiedFileName') # type: ignore
    def Built_In(self, p):
        #self.unrollP(p)
        return "BuiltIn", p[0].upper(), p[1]

    @_('loadProgram','saveProgram', # type: ignore
       'loadExtention','loadVars','Info') 
    def Built_In(self, p):
        #self.unrollP(p)
        Lst = ["BuiltIn"]
        for Elem in p[0]:
            #print(Elem)
            Lst.append(Elem)
        return Lst 
    
    @_('DIR', 'PWD', 'LS') # type: ignore
    def Built_In(self, p):
        if type(p[0]).__name__ == 'tuple':
            p="BuiltIn",p[0][0].upper(),p[0][1].upper()
        else:
            p="BuiltIn",p[0].upper()
        return p

    @_('WAIT Term') # type: ignore
    def Built_In(self, p):
        p = "BuiltIn", "WAIT", p[1]
        return p

    @_('PROGRAM LOAD QualifiedFileName') # type: ignore
    def loadProgram(self, p):
        #self.unrollP(p)
        return ["LoadProgram", p[2]]
    
    @_('PROGRAM SAVE QualifiedFileName') # type: ignore
    def saveProgram(self, p):
        #self.unrollP(p)
        return ["SaveProgram", p[2]]

    @_('EXTENTION LOAD ALPHA_NUMERIC') # type: ignore
    def loadExtention(self, p):
        self.unrollP(p)
        return ["LoadExtention", p[2]]

    @_('LOAD VARS QualifiedFileName') # type: ignore
    def loadVars(self, p):
        #self.unrollP(p)
        return ["LoadVars", p[2]]

    @_('LIST VARS') # type: ignore
    def list_vars(self, p):
        return "LIST_VARS"

    @_('LIST EXT') # type: ignore
    def List_Extentions(self, p):
        return "LIST_EXTENTIONS"

    @_('LIST ALPHA_NUMERIC') # type: ignore
    def List_BuiltIn(self, p):
        #self.unrollP(p)
        return "BUILTIN"

    @_('LIST') # type: ignore
    def list_prog(self, p):
        return "LIST"

    @_('INFO','INFO ALPHA_NUMERIC') # type: ignore
    def Info(self, p):
        # self.unrollP(p)
        return "Info"

    @_('Path \\ FileName','ALPHA_NUMERIC \\ FileName','FileName','ALPHA_NUMERIC') # type: ignore
    def QualifiedFileName(self, p):
        Str = ''
        #self.unrollP(p)
        for Elem in p:
            Str += Elem
        return Str

    @_('ALPHA_NUMERIC DOT ALPHA_NUMERIC','LETTER DOT ALPHA_NUMERIC','LETTER DOT LETTER') # type: ignore
    def FileName(self, p):
        Str = ''
        #self.unrollP(p)
        for Elem in p:
            Str += Elem
        return Str

    @_('CD UpPath', # type: ignore
       'CD Path',
       'CD Drive',
       'CD Drive Path',
       'CD ALPHA_NUMERIC')
    def Built_In(self, p):
        CDPath = ''
        p[0] = "CD"
        #self.unrollP(p)
        for i in range(1,len(p)):
            CDPath += p[i]
        print(CDPath)
        return "BuiltIn", p[0], CDPath

    @_('Path \\ ALPHA_NUMERIC') # type: ignore
    def Path(self, p):
        Str = ''
        #self.unrollP(p)
        for Elem in p:
            Str += Elem
        return Str

    @_('\\ ALPHA_NUMERIC') # type: ignore
    def Path(self, p):
        Str = ''
        #self.unrollP(p)
        for Elem in p:
            Str += Elem
        return Str
    
    @_('LETTER COLON') # type: ignore
    def Drive(self, p):
        Str=''
        for Elem in p:
            Str += Elem
        return Str
    
    @_('DOUBLEDOT') # type: ignore
    def UpPath(self, p):
        p = '..'
        return p

    @_('Expr') # type: ignore
    def Statement(self, p):
        return "BTree", p[0]
    
    @_('NUMBERED_LINE Statement', # type: ignore
       'NUMBERED_LINE Built_In')
    def Line(self, p):
        #self.unrollP(p)
        return 'Line', p[0],p[1]

    @_('Variable ASSIGN Expr', # type: ignore
       'Variable ASSIGN STRING')
    def Statement(self, p):
        # self.unrollP(p)
        self.prntLn = False
        Tree = BTree('Assign','=')
        Tree.left = BTree('As_Var', p[0])
        if(type(p[2]).__name__ == 'BTree'):
            Tree.right = p[2]
        else:
            Tree.right = BTree('VAL', p[2])
        return "BTree", Tree

    @_('Variable ASSIGN NOW') # type: ignore
    def Statement(self, p):
        # self.unrollP(p)
        self.prntLn = False
        Tree = BTree('Assign','=')
        Tree.left = BTree('As_Var', p[0])
        Tree.right = BTree("BuiltIn", p[2].upper())
        return "BTree", Tree
    
    @_('Variable ASSIGN TIME') # type: ignore
    def Statement(self, p):
        # self.unrollP(p)
        self.prntLn = False
        Tree = BTree('Assign','=')
        Tree.left = BTree('As_Var', p[0])
        Tree.right = BTree("BuiltIn", p[2].upper())
        return "BTree", Tree

    @_('Variable ASSIGN LogicStatement', # type: ignore
       'Variable ASSIGN Logic',
       'Variable ASSIGN Vector',
       'Variable ASSIGN Matrix')
    def Statement(self, p):
        self.prntLn = False
        Tree = BTree('Assign','=')
        Tree.left = BTree('As_Var', p[0])
        if(type(p[2]).__name__ == 'BTree'):
            Tree.right = p[2]
        else:
            Tree.right = BTree('VAL', p[2])
        return "BTree", Tree

    @_('Variable ADD_ASGN Expr', # type: ignore
       'Variable SUB_ASGN Expr',
       'Variable MUL_ASGN Expr',
       'Variable DIV_ASGN Expr') 
    def Statement(self, p):
        # self.unrollP(p)
        self.prntLn = False
        Op = self.OpAsnMap[p[1]]
        SubTree = BTree('Op',Op)
        SubTree.left = BTree('VAR', p[0])
        if(type(p[2]).__name__ == 'BTree'):
            SubTree.right = p[2]
        else:
            SubTree.right = BTree('VAL', p[2])
        Tree = BTree('Assign','=')
        Tree.left = BTree('As_Var', p[0])
        Tree.right = SubTree
        return "BTree", Tree

    @_('PrintStatement')  # type: ignore
    def Statement(self, p):
        self.prntLn = False
        return "BTree", p[0]

    @_('REM') # type: ignore
    def Statement(self, p):
        # self.unrollP(p)
        Lst = p[0].split(" ", 2)
        return 'Line', Lst[0], (Lst[1], Lst[2])

    @_('FnDecl ASSIGN Expr', # type: ignore
       'FnDecl ASSIGN MixdArgs')  # type: ignore
    def Statement(self, p):
        # Msg = addStr(BOLD, RED, "FnDef",WHITE," <-- ",YELLOW,"FnDecl ASSIGN Expr | Variable")
        # self.unrollP(p, Msg)
        self.prntLn = False
        Fn=p[0]
        Tree = BTree('Assign','=')
        Tree.left = BTree('As_Var', Fn[0])        
        Tree.right = BTree('FnDecl', {"Type":"Declaration", "Name": Fn[0], "Args": Fn[1], "Body":p[2], "Line" : self.Line })
        return "BTree", Tree

    @_('Variable ( VarsArgsList )') # type: ignore
    def FnDecl(self, p):
        # Msg = addStr(BOLD, RED, "FnDecl",WHITE," <-- ",YELLOW,"Variable ( VarsArgsList )")
        # self.unrollP(p, Msg)
        return p[0], p[2]
    
    @_('Variable ASSIGN FnCall') # type: ignore
    def Statement(self, p):
        # Msg = addStr(BOLD, RED, "Statement",WHITE," <-- ",YELLOW,"FnCall")
        # self.unrollP(p, Msg)
        Fn=p[0]
        Tree = BTree('Assign','=')
        Tree.left = BTree('As_Var', Fn[0]) 
        Fn=p[2]
        # Return the Function as Function Call Operation
        Tr = BTree('FnCall',Fn[1])
        Tr.left = BTree('VAR', Fn[0])
        Tr.right = BTree('VAL', Fn[1])
        Tree.right = Tr
        return "BTree", Tree

    @_('FnCall') # type: ignore
    def Statement(self, p):
        # Msg = addStr(BOLD, RED, "Statement",WHITE," <-- ",YELLOW,"FnCall")
        # self.unrollP(p, Msg)
        Fn=p[0]
        # Return the Function as Function Call Operation
        Tree = BTree('FnCall',Fn[1])
        Tree.left = BTree('VAR', Fn[0])
        Tree.right = BTree('VAL', Fn[1])
        return "BTree", Tree

    @_('Variable ( ArgsList )')  # type: ignore
    def FnCall(self, p):
        # Msg = addStr(BOLD, RED, "FnCall",WHITE,"<--",YELLOW,"Variable ( ArgsList )")
        # self.unrollP(p, Msg)
        return p[0], p[2]

    @_('PRINT ( ArgsListStatement ) ') # type: ignore
    def PrintStatement(self, p):
        Tree = BTree('St','PRINT')
        Tree.left = BTree('VAL', p[2])
        return Tree

    @_('Variable', # type: ignore
       'Variable COMMA ArgsListStatement')
    def ArgsListStatement(self, p):
        # Msg = addStr(BOLD, RED, "ArgsListStatement",WHITE," <-- ",YELLOW,"STRING, | Expr, | COLOR,")
        # self.unrollP(p, Msg)
        Val = self.Vars.Value(p[0])
        self.Queue.Enqueue(Val)
        return p

    @_('STRING', # type: ignore
       'STRING COMMA ArgsListStatement',
       'Expr',
       'Expr COMMA ArgsListStatement',
       'COLOR',
       'COLOR COMMA ArgsListStatement') # type: ignore
    def ArgsListStatement(self, p):
        # Msg = addStr(BOLD, RED, "ArgsListStatement",WHITE," <-- ",YELLOW,"STRING, | Expr, | COLOR,")
        # self.unrollP(p, Msg)
        if type(p[0]).__name__ == 'str':
            Str = p[0]
            if "\"" in Str:
                p = Str[1:-1]
            else:
                p = Str
            self.Queue.Enqueue(p)
            p=self.Queue
        elif type(p[0]).__name__ == 'int' or type(p[0]).__name__ == 'float':
            #print("Expr: ", p[0])
            self.Queue.Enqueue(p[0])
            p=self.Queue
        elif type(p[0]).__name__ == 'BTree':
            self.Queue.Enqueue(p[0])
            p=self.Queue
        else:
            print("Type: ", type(p[0]).__name__)
            p=p[0]
        return p

    @_('EXIT') # type: ignore
    def Quit (self, p):
        p='EXIT'
        return p

    @_('Expr LEQ Expr') # type: ignore
    def LogicStatement(self, p):
        Tree = BTree('Op','<=')
        if type(p[0]).__name__ == 'int' or type(p[0]).__name__ == 'float':
            Tree.left = BTree('VAL',p[0])
        else:
            Tree.left = p[0]
        if type(p[2]).__name__ == 'int' or type(p[2]).__name__ == 'float':
            Tree.right = BTree('VAL',p[2])
        else:
            Tree.right = p[2]
        return Tree

    @_('Expr GEQ Expr') # type: ignore
    def LogicStatement(self, p):
        Tree = BTree('Op','>=')
        if type(p[0]).__name__ == 'int' or type(p[0]).__name__ == 'float':
            Tree.left = BTree('VAL',p[0])
        else:
            Tree.left = p[0]
        if type(p[2]).__name__ == 'int' or type(p[2]).__name__ == 'float':
            Tree.right = BTree('VAL',p[2])
        else:
            Tree.right = p[2]
        return Tree
    
    @_('Expr LT Expr') # type: ignore
    def LogicStatement(self, p):
        Tree = BTree('Op','<')
        if type(p[0]).__name__ == 'int' or type(p[0]).__name__ == 'float':
            Tree.left = BTree('VAL',p[0])
        else:
            Tree.left = p[0]
        if type(p[2]).__name__ == 'int' or type(p[2]).__name__ == 'float':
            Tree.right = BTree('VAL',p[2])
        else:
            Tree.right = p[2]
        return Tree
    
    @_('Expr GT Expr') # type: ignore
    def LogicStatement(self, p):
        Tree = BTree('Op','>')
        if type(p[0]).__name__ == 'int' or type(p[0]).__name__ == 'float':
            Tree.left = BTree('VAL',p[0])
        else:
            Tree.left = p[0]
        if type(p[2]).__name__ == 'int' or type(p[2]).__name__ == 'float':
            Tree.right = BTree('VAL',p[2])
        else:
            Tree.right = p[2]
        return Tree
    
    @_('Expr NEQ Expr') # type: ignore
    def LogicStatement(self, p):
        Tree = BTree('Op','!=')
        if type(p[0]).__name__ == 'int' or type(p[0]).__name__ == 'float':
            Tree.left = BTree('VAL',p[0])
        else:
            Tree.left = p[0]
        if type(p[2]).__name__ == 'int' or type(p[2]).__name__ == 'float':
            Tree.right = BTree('VAL',p[2])
        else:
            Tree.right = p[2]
        return Tree
    
    @_('Expr EQ Expr') # type: ignore
    def LogicStatement(self, p):
        Tree = BTree('Op','==')
        if type(p[0]).__name__ == 'int' or type(p[0]).__name__ == 'float':
            Tree.left = BTree('VAL',p[0])
        else:
            Tree.left = p[0]
        if type(p[2]).__name__ == 'int' or type(p[2]).__name__ == 'float':
            Tree.right = BTree('VAL',p[2])
        else:
            Tree.right = p[2]
        return Tree
    
    @_('HexNumber XOR_OP HexNumber', # type: ignore
       'Integer XOR_OP Integer')
    def Logic(self, p):
        # self.unrollP(p)
        Tree = BTree('Op', 'Xor')
        Left = type(p[0]).__name__
        Right = type(p[2]).__name__
        if Left == 'int' or Left == 'HEX':
            Tree.left = BTree('VAL',p[0])
        if Right == 'int' or Right == 'HEX':
            Tree.right = BTree('VAL',p[2])

    @_('HexNumber AND_OP HexNumber', # type: ignore
       'Integer AND_OP Integer')
    def Logic(self, p):
        # self.unrollP(p)
        Tree = BTree('Op', p[1])
        Left = type(p[0]).__name__
        Right = type(p[2]).__name__
        if Left == 'int' or Left == 'HEX':
            Tree.left = BTree('VAL',p[0])
        if Right == 'int' or Right == 'HEX':
            Tree.right = BTree('VAL',p[2])

    @_('HexNumber OR_OP HexNumber', # type: ignore
       'Integer OR_OP Integer')
    def Logic(self, p):
        # self.unrollP(p)
        Tree = BTree('Op', p[1])
        Left = type(p[0]).__name__
        Right = type(p[2]).__name__
        if Left == 'int' or Left == 'HEX':
            Tree.left = BTree('VAL',p[0])
        if Right == 'int' or Right == 'HEX':
            Tree.right = BTree('VAL',p[2])

    @_('Term')  # type: ignore
    def Expr(self,p):
        #Msg = addStr(BOLD, RED, "Expr",WHITE,"<--",YELLOW,"Term")
        #self.unrollP(p, Msg)
        return p[0]

    @_('Term ADD_OP Factor', # type: ignore
       'Term SUB_OP Factor',
       'Term ADD_OP Variable',
       'Term SUB_OP Variable',
       'Variable ADD_OP Factor',
       'Variable SUB_OP Factor',
       'Variable ADD_OP Variable',
       'Variable SUB_OP Variable') 
    def Term(self,p):
        # Msg = addStr(BOLD, RED, "Term",WHITE," <-- ",YELLOW,"Term ",str(p[1])," Term")
        # self.unrollP(p, Msg)
        # print("Type p[0]: " , type(p[0]).__name__)
        # print("Type p[1]: " , type(p[2]).__name__)
        Tree = BTree('Op',p[1])
        if type(p[0]).__name__ == 'int' or type(p[0]).__name__ == 'float':
            Tree.left = BTree('VAL',p[0])
        elif type(p[0]).__name__ == 'str':
            Tree.left = BTree('VAR',p[0])
        else:
            Tree.left = p[0]

        if type(p[2]).__name__ == 'int' or type(p[2]).__name__ == 'float':
            Tree.right = BTree('VAL',p[2])
        elif type(p[2]).__name__ == 'str':
            Tree.right = BTree('VAR',p[2])
        else:
            Tree.right = p[2]
        return Tree

    @_('Term POW_OP Factor') # type: ignore
    def Term(self,p):
        # Msg = addStr(BOLD, RED, " Term <-- Term ^ Factor")
        # self.unrollP(p, Msg)
        Tree = BTree('Op','^')
        if type(p[0]).__name__ == 'int' or type(p[0]).__name__ == 'float':
            Tree.left = BTree('VAL',p[0])
        else:
            Tree.left = p[0]
        if type(p[2]).__name__ == 'int' or type(p[2]).__name__ == 'float':
            Tree.right = BTree('VAL',p[2])
        else:
            Tree.right = p[2]
        return Tree

    @_('Term MUL_OP Factor', # type: ignore
       'Term BACKSLASH_OP Factor',
       'Term MUL_OP Variable',
       'Term BACKSLASH_OP Variable',
       'Variable MUL_OP Factor',
       'Variable BACKSLASH_OP Factor',
       'Variable MUL_OP Variable',
       'Variable BACKSLASH_OP Variable') 
    def Term(self,p):
        # Str = str(p[1])
        # Msg = addStr(BOLD, RED, "Term",WHITE," <-- ",YELLOW,"Term ",Str, " Term")
        # self.unrollP(p, Msg)
        # print("Type:" ,type(p[0]).__name__)
        # print("Type:" ,type(p[2]).__name__)
        Tree = BTree('Op',p[1])
        if type(p[0]).__name__ == 'int' or type(p[0]).__name__ == 'float':
            Tree.left = BTree('VAL',p[0])
        elif type(p[0]).__name__ == 'str':
            Tree.left = BTree('VAR',p[0])
        elif type(p[0]).__name__ == 'BTree':
            if p[0].Value == '+' or p[0].Value == '-':
                Val = p[0].right
                Tree.left = Val
                p[0].right = Tree
                self.Stack.Push(p[0])                
            else:
                Tree.left = p[0]

        if type(p[2]).__name__ == 'int' or type(p[2]).__name__ == 'float':
            Tree.right = BTree('VAL',p[2])
        elif type(p[0]).__name__ == 'str':
            Tree.right = BTree('VAR',p[2])
        else:
            Tree.right = BTree('VAR',p[2])
        if self.Stack.Size > 0:
            Tree = self.Stack.Pop()
        return Tree

    @_('Term MUL_OP Vector', # type: ignore
       'Term MUL_OP Matrix') 
    def Term(self,p):
        Tree = BTree('Op','Vect*')
        if type(p[0]).__name__ == 'int' or type(p[0]).__name__ == 'float':
            Tree.left = BTree('VAL',p[0])
        else:
            Tree.left = p[0]
        if type(p[2]).__name__ == 'Vector' or type(p[2]).__name__ == 'Matrix':
            Tree.right = BTree('VAL',p[2])
        else:
            Tree.right = p[2]
        return Tree 

    @_('Factorial') # type: ignore
    def Term(self,p):
        return p[0]

    @_('Term SHFT_LEFT Integer') # type: ignore
    def Term(self,p):
        Tree = BTree('Op','<<')
        if type(p[0]).__name__ == 'int' or type(p[0]).__name__ == 'float':
            Tree.left = BTree('VAL',p[0])
        else:
            Tree.left = p[0]
        if type(p[2]).__name__ == 'int' or type(p[2]).__name__ == 'float':
            Tree.right = BTree('VAL',p[2])
        else:
            Tree.right = p[2]
        return Tree
    
    @_('Term SHFT_RIGHT Integer') # type: ignore
    def Term(self,p):
        Tree = BTree('Op','>>')
        if type(p[0]).__name__ == 'int' or type(p[0]).__name__ == 'float':
            Tree.left = BTree('VAL',p[0])
        else:
            Tree.left = p[0]
        if type(p[2]).__name__ == 'int' or type(p[2]).__name__ == 'float':
            Tree.right = BTree('VAL',p[2])
        else:
            Tree.right = p[2]
        return Tree
    
    @_('LOG ( Term )') # type: ignore
    def Term(self,p):
        Tree = BTree('Op','LOG')
        if type(p[2]).__name__ == 'int' or type(p[2]).__name__ == 'float':
            Tree.left = BTree('VAL',p[2])
        else:
            Tree.left = p[2]
        Tree.right = None
        return Tree

    @_('LOG2 ( Term )') # type: ignore
    def Term(self,p):
        Tree = BTree('Op','LOG2')
        if type(p[2]).__name__ == 'int' or type(p[2]).__name__ == 'float':
            Tree.left = BTree('VAL',p[2])
        else:
            Tree.left = p[2]
        Tree.right = None
        return Tree

    @_('LN ( Term )') # type: ignore
    def Term(self,p):
        Tree = BTree('Op','LN')
        if type(p[2]).__name__ == 'int' or type(p[2]).__name__ == 'float':
            Tree.left = BTree('VAL',p[2])
        else:
            Tree.left = BTree('VAR',p[2])
        Tree.right = None
        return Tree
    
    @_('Term ( Expr )') # type: ignore
    def Term(self,p):
        Tree = BTree('Op','*')
        if type(p[0]).__name__ == 'int' or type(p[0]).__name__ == 'float':
            Tree.left = BTree('VAL',p[0])
        else:
            Tree.left = p[0]
        if type(p[2]).__name__ == 'int' or type(p[2]).__name__ == 'float':
            Tree.right = BTree('VAL',p[2])
        else:
            Tree.right = p[2]
        return Tree

    @_('SOLVE ( Variable COMMA Variable  ) ','SOLVE (  Matrix COMMA Vector ) ') # type: ignore
    def Built_In(self, p):
        # Msg = addStr(BOLD, RED, "Built_In",WHITE," <-- ",YELLOW,"SOLVE ( Variable , Variable ) | SOLVE ( Matrix , Vector )")
        # self.unrollP(p, Msg)
        return "SOLVE", p[2],p[4]

    @_('LBRACKET Vectors RBRACKET') # type: ignore
    def Matrix(self, p):
        Matix0 = []
        Size = self.Stack.Size
        for i in range(Size):
            Ary = self.Stack.Pop()
            Matix0.append(Ary)
        self.Stack = Stack()
        p = np.array(Matix0)
        return p

    @_('Vector COMMA Vector','Vectors COMMA Vector') # type: ignore
    def Vectors(self, p):
        return p[1]

    @_('LBRACKET Factors RBRACKET') # type: ignore
    def Vector(self, p):
        self.Stack.Push(p[1])
        return p[1]

    @_('Variable COMMA Variable', # type: ignore
       'Variable COMMA Number',
       'Number COMMA Variable',
       'Number COMMA Number',
       'Factors COMMA Variable',
       'Factors COMMA Number')
    def Factors(self, p):
        # self.unrollP(p)
        if type(p[0]).__name__ != 'list':
            Vec0 = []
            Vec0.append(p[0])
        else:
            Vec0 = p[0]
        Vec0.append(p[2])
        return Vec0

    @_('Factor') # type: ignore
    def Term(self,p):
        # Msg = addStr(BOLD, RED, "Term",WHITE," <-- ",YELLOW,"Factor")
        # self.unrollP(p, Msg)
        return p[0]
    
    @_('nCr','nPr') # type: ignore
    def Term(self,p):
        # Msg = addStr(BOLD, RED, "Term",WHITE," <-- ",YELLOW,"nCr | nPr")
        # self.unrollP(p, Msg)
        return p[0]

    @_('Number') # type: ignore
    def Factor(self, p):
        return p[0]

    @_('Integer BANG') # type: ignore
    def Factorial(self,p):
        Tree = BTree('Op','!') # type: ignore
        Tree.left = BTree('VAL',p[0])
        Tree.right = None
        return Tree

    @_('Integer LETTER',  # type: ignore
       'Real LETTER')
    def Term(self,p):
        #self.unrollP(p)
        Tree = BTree('Op','*') # type: ignore
        if type(p[0]).__name__ == 'int' or type(p[0]).__name__ == 'float':
            Tree.left = BTree('VAL',p[0])
        else:
            Tree.left = p[0]
        if type(p[1]).__name__ == 'int' or type(p[1]).__name__ == 'float':
            Tree.right = BTree('VAL',p[1])
        else:
            Tree.right = BTree('VAR',p[1])
        return Tree

    @_('CHOOSE ( Integer COMMA Integer )') # type: ignore
    def nCr(self,p):
        Tree = BTree('Op','nCr')
        if type(p[2]).__name__ == 'int' or type(p[2]).__name__ == 'float':
            Tree.left = BTree('VAL',p[2])
        else:
            Tree.left = p[2]
        if type(p[4]).__name__ == 'int' or type(p[4]).__name__ == 'float':
            Tree.right = BTree('VAL',p[4])
        else:
            Tree.right = p[4]
        return Tree

    @_('PERMUT ( Integer COMMA Integer )') # type: ignore
    def nPr(self,p):
        Tree = BTree('Op','nPr')
        if type(p[2]).__name__ == 'int' or type(p[2]).__name__ == 'float':
            Tree.left = BTree('VAL',p[2])
        else:
            Tree.left = p[2]
        if type(p[4]).__name__ == 'int' or type(p[4]).__name__ == 'float':
            Tree.right = BTree('VAL',p[4])
        else:
            Tree.right = p[4]
        return Tree

    @_('~ Integer %prec UTILDE',  # type: ignore
       '~ Variable %prec UTILDE')
    def Factor(self, p):
        #self.unrollP(p)
        Tree = BTree('Op','~')
        if type(p[1]).__name__ == 'int':
            Tree.right = BTree('VAL',p[1])
        else:
            Tree.right = BTree('VAR',p[1])
        Tree.left = None
        return Tree

    # Terminals
    @_('Variable', # type: ignore
       'Variable COMMA MixdArgs',
       'NegedVariable',
       'NegedVariable COMMA MixdArgs') # type: ignore
    def MixdArgs(self, p):
        # Msg = addStr(BOLD, RED, "MixdArgs",WHITE," <-- ",YELLOW,"NegVar | NegVar , FnArgsList")
        # self.unrollP(p, Msg)
        # print(type(p[-1]).__name__)
        if type(p[-1]).__name__ == 'BTree':
            Q = Queue()
            Q.Enqueue(p[-1])
        else:
            Q=p[-1]
            Q.Enqueue(p[0])        
        return Q

    @_('Variable','Variable COMMA VarsArgsList') # type: ignore
    def VarsArgsList(self, p):
        # Msg = addStr(BOLD, RED, "FnArgsList",WHITE," <-- ",YELLOW,"NegVar | NegVar , FnArgsList")
        # self.unrollP(p, Msg)
        print(type(p[-1]).__name__)
        if type(p[-1]).__name__ == 'str':
            Q = Queue()
            Q.Enqueue(p[-1])
        else:
            Q=p[-1]
            Q.Enqueue(p[0])        
        return Q
    
    @_('SUB_OP ALPHA_NUMERIC %prec UMINUS','SUB_OP LETTER %prec UMINUS') # type: ignore
    def NegedVariable(self, p):
        # Msg = addStr(BOLD, RED, "LtrVar", WHITE,"<--",YELLOW,"SUB_OP ALPHA_NUMERIC %prec UMINUS | SUB_OP LETTER %prec UMINUS")
        # self.unrollP(p, Msg)
        Tree = BTree('Op','*')
        Tree.left = BTree('VAL',-1)
        Tree.right = BTree('VAR',p[0])
        return Tree

    @_('ALPHA_NUMERIC','LETTER') # type: ignore
    def Variable(self, p):        
        #Msg = addStr(BOLD, RED, "Variable",WHITE," <-- ",YELLOW,"ALPHA_NUMERIC | LETTER")
        # self.unrollP(p, Msg)
        return p[0] #BTree('VAR',p[0])

    @_('Number','Number COMMA ArgsList') # type: ignore
    def ArgsList(self, p): # Tie point for negated and non-negated Numbers
        #Msg = addStr(BOLD, RED, "ArgsList",WHITE," <-- ",YELLOW,"Number | Number , ArgsList")
        #self.unrollP(p, Msg)
        self.Queue.Enqueue(p[0])
        return self.Queue 
    
    @_('SUB_OP Number %prec UMINUS') # type: ignore
    def Number(self, p):
        Results = 0
        if type(p[0]).__name__ == 'str':
            if type(p[1]).__name__ == 'int' or type(p[1]).__name__ == 'float':
                Results = -p[1]
            else:
                Results = -p[0]
        return Results

    @_('Integer', 'Real') # type: ignore
    def Number(self, p):
        p = p[0]
        return p

    @_('HEX_NUM') # type: ignore
    def HexNumber(self, p):
        return p[0]

    @_('BANG') # type: ignore
    def Quit (self, p):
        p='EXIT'
        return p

    @_('INTEGER') # type: ignore
    def Integer(self, p):
        # self.unrollP(p)
        p = p[0]
        return p
        
    @_('REAL') # type: ignore
    def Real(self, p):
        p = p[0]
        return p
    
