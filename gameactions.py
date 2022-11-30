import pyautogui as keyboard
import time
import ctypes
import random

R = 0x13
E = 0x12
W = 0x11
Q = 0x10
Enter = 0x1C

# Bunch of stuff so that the script can send keystrokes to game #

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def KeyPress(key):
    PressKey(key) # press 
    time.sleep(.05)
    ReleaseKey(key) #release 


#Level up an ability
def level_up(ability):
  keyboard.press_and_release('ctrl+' + ability)
  
#Use Q
def use_q(direction):
  return 0
  
#Use W 
def use_w():
  KeyPress(W)

#Use E  
def use_e():
  KeyPress(E)

#Use R  
def use_ult(direction):
  return 0
  
#Buy Items
def go_shopping():
  return 0
  
#Recall
def recall():
  keyboard.press('B')

#Use Ignite
def use_ignite():
  keyboard.press('D')

#Use Exhaust
def use_exhaust():
  keyboard.press('F')

#Use Heal (Summoner)
def use_heal_sum():
  keyboard.press('D')
  
#Use a stealth ward
def place_stealthward():
  return 0
  
#Use pinkward
def place_pinkward():
  return 0
  
#Use Redmeption
def use_redemption():
  return 0
  
#Be Toxic
toxic_phrases = ['GGEZ', 'Git gud', 'Sup diff', 'GG uninstall', 'EZ uninstall']
def being_toxic():
  KeyPress(Enter)
  time.sleep(0.01)
  keyboard.write(toxic_phrases[random.randint(0,4)], interval = 0.01)
  time.sleep(0.01)
  KeyPress(Enter)
