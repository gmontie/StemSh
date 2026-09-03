import platform
import sys
Platform = platform.system()
if ('CYGWIN_NT' in Platform): # type: ignore
    sys.path.append('/usr/local/Lib/Python')
    from msPrompt import KeyboardPrompt # type: ignore
elif ('Windows' in Platform): # type: ignore
    sys.path.append("C:\\Lib\\Python")
    from msPrompt import KeyboardPrompt # type: ignore
elif ('Linux' in Platform): # type: ignore
    sys.path.append('/usr/local/Lib/Python')
    from Prompt import KeyboardPrompt # type: ignore

from sly import Lexer
from Colorizer import Colorizer # type: ignore

# =============================================================================
# MEtaDaTA
# =============================================================================
__author__ = "Greg Montgomery"
__version__ = "0.2.0"
__status__ = "Development"

isColor = Colorizer().isColor

class Tokenize(Lexer):
    tokens = { 
        LETTER, # type: ignore
        ASSIGN, # type: ignore
        NUMBERED_LINE, # type: ignore
        ADD_ASGN, # type: ignore
        SUB_ASGN, # type: ignore
        MUL_ASGN, # type: ignore
        DIV_ASGN, # type: ignore
        EQ, # type: ignore
        NEQ, # type: ignore
        LEQ, # type: ignore
        GEQ, # type: ignore
        LT, # type: ignore
        GT, # type: ignore
        AND_OP, # type: ignore
        OR_OP, # type: ignore
        XOR_OP, # type: ignore
        SHFT_RIGHT, # type: ignore
        SHFT_LEFT, # type: ignore
        LBRACKET, # type: ignore
        RBRACKET, # type: ignore
        PERMUT, # type: ignore
        CHOOSE, # type: ignore
        BANG, # type: ignore
        ADD_OP, # type: ignore
        SUB_OP, # type: ignore
        MUL_OP, # type: ignore
        BACKSLASH_OP, # type: ignore
        COLON, # type: ignore
        POW_OP, # type: ignore
        COMMA, # type: ignore
        ALPHA_NUMERIC, # type: ignore
        COLOR, # type: ignore
        STRING, # type: ignore
        EXTENTION, # type: ignore
        EXT, # type: ignore
        INFO, # type: ignore
        CLEAR, # type: ignore
        PRINT, # type: ignore
        LIST, # type: ignore
        PROGRAM, # type: ignore
        WAIT, # type: ignore
        SAVE, # type: ignore
        LOAD, # type: ignore
        VARS, # type: ignore
#        EXTENTIONS, # type: ignore
        SOLVE, # type: ignore
        DOUBLEDOT, # type: ignore
        DOT, # type: ignore
        ENV, # type: ignore
        NOW, # type: ignore
        TIME, # type: ignore
        CAT, # type: ignore
        FILE, # type: ignore
        HELP, # type: ignore
        LIST, # type: ignore
        LOAD, # type: ignore
        NOW,  # type: ignore  
        EXIT, # type: ignore
        LOG,  # type: ignore
        LOG2,  # type: ignore
        LN,   # type: ignore
        DIR,  # type: ignore
        LS,  # type: ignore
        PWD,  # type: ignore
        CD,   # type: ignore
    #    IF,
    #    THEN,
    #    ELSE,
    #    FOR,
        REM, # type: ignore
        REN, # type: ignore
        NEW, # type: ignore
    #    NEXT,
        RUN,         # type: ignore
        HEX_NUM, # type: ignore
        INTEGER, # type: ignore
        REAL, # type: ignore
        '?','\\','(',')','~'
        }

    ignore  = ' \r\n\t'

    literals = {'?','\\','(',')','~'} 

    # Tokens -  Reserved Words
    PRINT     = r'print|Print|PRINT'
    EXTENTION = r'Extention|extention'
    #IF       = r'if|IF'
    #THEN     = r'then|THEN'
    #ELSE     = r'else|ELSE'
    #FUNC      = r'func|FUNC'
    #FOR      = r'for|FOR'
    #TO       = r'to|TO'
    #NEXT     = r'next|NEXT'
    # Build In Functions or Immediate
    EXT       =r'ext|Ext|EXT'
    INFO      = r'Info|info|INFO'
    NEW       = r'new|NEW'
    SOLVE     = r'solve|SOLVE'
    ENV       = r'env|ENV'
    CAT       = r'cat|CAT'
    FILE      = r'file|FILE'
    CLEAR     = r'clear|CLEAR|CLS|cls|Cls'
    HELP      = r'help|HELP'
    LIST      = r'list|LIST'
    LOAD      = r'load|LOAD'
    TIME      = r'Time|time|TIME'
    NOW       = r'Now|NOW|now'
    PROGRAM   = r'program|PROGRAM'
    EXIT      = r'exit|EXIT|quit|QUIT'
    REN       = r'ren|REN'# Renumber
    RUN       = r'run|RUN'
    SAVE      = r'save|SAVE'
    VARS      = r'vars|VARS'
    WAIT      = r'WAIT|wait'
    DIR       = r'dir|DIR'
    LS        = r'ls|LS'
    PWD       = r'pwd|PWD'
    CD        = r'cd|CD'
    LOG2      = r'log2|LOG2'
    LOG       = r'log|LOG'
    LN        = r'ln|LN'
    DOUBLEDOT = r"\.\."
    DOT       = r"\."

    @_(r'^\d{0,3}\ REM .*')  # type: ignore
    def REM(self, t):
        return t

    # Left Bracket
    @_(r'\[')  # type: ignore
    def LBRACKET(self, t):
        return t

    # Left Bracket
    @_(r'\]')  # type: ignore
    def RBRACKET(self, t):
        return t
    
    @_(r'\".*?\"')  # type: ignore
    def STRING(self, t):
        return t
    
    # Comma
    @_(r',')  # type: ignore
    def COMMA(self, t):
        return t
    
    @_(r'\+=')  # type: ignore
    def ADD_ASGN(self, t):
        return t
    
    @_(r'-=')  # type: ignore
    def SUB_ASGN(self, t):
        return t 

    @_(r'\*=')  # type: ignore
    def MUL_ASGN(self, t):
        return t

    @_(r'/=') # type: ignore
    def DIV_ASGN(self, t):
        return t

    @_(r'==') # type: ignore
    def EQ(self, t):
        return t

    @_(r'!=') # type: ignore
    def NEQ(self, t):
        return t

    @_(r'<=') # type: ignore
    def LEQ(self, t):
        return t
    
    @_(r'>=')  # type: ignore
    def GEQ(self, t):
        return t

    # Add Operator
    @_(r'\+')  # type: ignore
    def ADD_OP(self, t):
        return t

    # Subtract Operator
    @_(r'-')  # type: ignore
    def SUB_OP(self, t):
        return t
    
    # Multiply Operator
    @_(r'\*')  # type: ignore
    def MUL_OP(self, t):
        return t

    @_(r'&') # type: ignore
    def AND_OP(self, t):
        return t

    @_(r'\|') # type: ignore
    def OR_OP(self, t):
        return t

    # Divide Operator
    @_(r'/')  # type: ignore
    def BACKSLASH_OP(self, t):
        return t

    @_(r':') # type: ignore
    def COLON(self, t):
        return t

    # Power Operator
    @_(r'\^')  # type: ignore
    def POW_OP(self, t):
        return t

    @_(r'!') # type: ignore
    def BANG(self, t):
        return t

    # Assignment
    @_(r'=')  # type: ignore
    def ASSIGN(self, t):
        return t

    @_(r'^\d{0,3}\ ') # type: ignore
    def NUMBERED_LINE(self, t):
        t.value = t.value.strip()
        return t
    
    @_(r'<')  # type: ignore
    def LT(self, t):
        return t
    
    @_(r'>')  # type: ignore
    def GT(self, t):
        return t
    
    @_(r'\>\>')  # type: ignore
    def SHFT_RIGHT(self, t):
        return t

    @_(r'\<\<')  # type: ignore
    def SHFT_LEFT(self, t):
        return t

    @_(r'\n+')  # type: ignore
    def newline(self, t):
        self.lineno += t.value.count('\n')

    # Floating point and real numbers
    @_(r'(\d*\.\d+)|(\d+\.\d+)|(\-\d+\.\d+)')  # type: ignore
    def REAL(self, t):
        t.value=float(t.value)
        return t

    @_(r'0x[0-9a-fA-F]+')  # type: ignore
    def HEX_NUM(self, t):
        t.value = int(t.value, 16)
        return t

    # Integer numbers
    @_(r'\d+|\-\d+')  # type: ignore
    def INTEGER(self, t):
        t.value = int(t.value)
        return t    

    # XOR OP
    @_(r'XOr')  # type: ignore
    def XOR_OP(self, t):
        return t

    # Combinatorics nCr
    @_(r'nCr')  # type: ignore
    def CHOOSE(self, t):
        return t

    # Permutations nPr
    @_(r'nPr')  # type: ignore
    def PERMUT(self, t):
        print(t)
        return t

    # Alphanumeric strings
    @_(r'[a-z_A-Z][a-zA-Z0-9_\-]+') # type: ignore
    def ALPHA_NUMERIC(self, t):
        if isColor(t.value):
            t.type = 'COLOR'
        return t
        
    # Alphabet character or string
    @_(r'[a-zA-Z]|[a-zA-Z][a-zA-Z]')  # type: ignore
    def LETTER(self, t):
        return t

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
   
