#from argparse import FileType
import platform
import sys
Platform = platform.system()
if ('CYGWIN_NT' in Platform): #-10.0-22631'):
    sys.path.append('/usr/local/Lib/Python')
    from msPrompt import KeyboardPrompt # type: ignore
elif ('Windows' in Platform):
    sys.path.append("C:\\Lib\\Python")
    from msPrompt import KeyboardPrompt # type: ignore
elif ('Linux' in Platform):
    sys.path.append('/usr/local/Lib/Python')
    from Prompt import KeyboardPrompt # type: ignore

sys.path.append("RaspberryPI")

#import os
#import mimetypes

# Include the Colorizer and COLORS Objects
#from COLORS import BOLD, GREEN, RED, BLUE, YELLOW, WHITE, RESET # type: ignore
#from Colorizer import Colorizer # type: ignore

# ============================================================================
## import modules ect
#import RPi.GPIO as GPIO  # type: ignore
from Pin import Pin # type: ignore

# Inport the Extention class
from Extentions import Extention # type: ignore
#from PiPinSysHlp import Help # type: ignore

# ===============================================================================================
# MetAdATa
# ===============================================================================================
__author__ = "Greg Montgomery"
__version__ = "2.0.0"
__status__ = "Development"

#cprint = Colorizer().cprint
#addStr = Colorizer().addStr

#*****************************************************************************
# FileSys Extention
#*****************************************************************************
class CmdPi(Extention):
    def __init__(cls, # cls stands for Class
                 Name="Operations", 
                 Version=__version__, 
                 Author=__author__, 
                 Status=__status__):
        In = True
        Out = False
        cls.Debug=True
        #cls.__gpio=GPIO
        #cls.__gpio.setwarnings(False)
        #cls.__gpio.setmode(GPIO.BCM)
        cls.PinCfg = {
            1:"3.3V",    2:"5V",
            3:"GPIO2",   4:"5V",
            5:"GPIO3",   6:"GPIO",
            7:"GPIO4",   8:"GPIO",
            9:"GND",    10:"GPIO",
           11:"GPIO17", 12:"GPIO",
           13:"GPIO27", 14:"GND",
           15:"GPIO22", 16:"GPIO",
           17:"3.3V",   18:"GPIO",
           19:"GPIO10", 20:"GND",
           21:"GPIO9",  22:"GPIO",
           23:"GPIO11", 24:"GPIO",
           25:"GND",    26:"GPIO",
           27:"GPIO0",  28:"GPIO",
           29:"GPIO5",  30:"GND",
           31:"GPIO6",  32:"GPIO",
           33:"GPIO13", 34:"GPIO",
           35:"GPIO19", 36:"GPIO",
           37:"GPIO26", 38:"GPIO",
           39:"GND",    40:"GPIO"
        }

        # Load acutal Pins
        cls.Pins = {}
#        for p in range(0,40):
#            cls.Pins = Pin(p,In)

        # Additional Pin Functions
        cls.PinFn = {
            "SDA":3,"SCL":5,
            "GP_CLK":7,
            "TX":8,"RX":10,
            "PCM_CLK":18,
            "MOSI":19,"MISO":21,"SCLK":23,
            "CE0":24, "CE1":26,
            "ID_SD":27,"ID_SC":28,
            "PWM":33,            
            "PCM_FS":35,"PCM_DIN":38,"PCM_DOUT":40,
        }

        cls.Ops={
            'Exec': cls.Execute,
            'Print': cls.Print,
            'PinConfig': cls.PinConfig,
            'CleanUp': cls.CleanUp,
            'Poke': cls.Poke,
            'Peek': cls.Peek
            #'HELP' : Help().Usage
         }  

    #*****************************************************************************
    # Change Directory
    #*****************************************************************************
    @classmethod
    def Execute(cls, Line):
        aCmd = False
        return aCmd

    #=========================================================================
    @classmethod
    def Print(cls, Cmd):
        print("Message: ", Cmd)

    #=========================================================================
    @classmethod
    def Exe(cls, Command, Mnemonic):
        pass

    #=========================================================================
    @classmethod
    def PinConfig(cls, Direction, WhichPin, Args=None):
        p=None
        if Direction=='IN':
            p=Pin(cls.__gpio, cls.__gpio.IN,  WhichPin, Args)
        elif Direction=='OUT':
            p=Pin(cls.__gpio, cls.__gpio.OUT, WhichPin, Args)
        else:
            print("Don't know if Pin is supposed to be an input or an output")
        return p


    #*****************************************************************************
    # Execute a Line of Code <IMMEDIATE> Mode
    #*****************************************************************************
    @classmethod
    def CleanUp(cls):
        #GPIO.cleanup()
        pass

    #*****************************************************************************
    # 
    #*****************************************************************************
    @classmethod
    def Poke(cls, WhichPin, State):
        pass

    #*****************************************************************************
    # 
    #*****************************************************************************
    @classmethod
    def Peek(cls, WhichPin):
        pass

    #*****************************************************************************
    # 
    #*****************************************************************************
    @classmethod
    def getTable(cls):
        return cls.Ops

    #*****************************************************************************
    # 
    #*****************************************************************************
    @property
    def PinConfiguations(cls):
        return cls.PinCfg

    #*****************************************************************************
    # Cat for a File
    #*****************************************************************************
    @property
    def Table(cls):
        return cls.Ops

    #*****************************************************************************
    # return Name of Extention
    #*****************************************************************************
    @property
    def Name(cls):
        # Ensure instance access works
        return cls.__class__.__name__
    
    #*****************************************************************************
    # Return True because this Extention is implemented
    #*****************************************************************************
    @property
    def Implemented(cls):
        return True

    #*****************************************************************************
    # Return Help Text/String
    #*****************************************************************************
    @property
    def Help(cls):
        pass
        # Msg = addStr(BOLD, BLUE, "Raspberry PI Pin Extention Help")
        # Msg = addStr(Msg, WHITE, " Provides basic Raspberry PI PIN operations")
        # Msg = addStr(Msg, WHITE, " Available Operations:")
        # for Op in cls.Ops:
        #     Msg = addStr(Msg, GREEN, "  ", Op)
        # return Msg   
