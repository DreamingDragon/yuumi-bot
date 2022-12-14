import pyautogui
from keystrokes import *
import time
import random

KEYS = {'R':0x13,
        'E':0x12,
        'W':0x11,
        'Q':0x10,
        'B':0x30,
        'D':0x20,
        'F':0x21,
        'Enter':0x1C,
        'Ctrl':0x1D,
        '4':0x05}
        
COORD_X = 0
COORD_Y = 1

DIRECTIONS = { 'dir_one': [1400, 56],
               'dir_two': [1730, 200],
               'dir_three': [1919, 500],
               'dir_four': [1730, 800],
               'dir_five': [1400, 944],
               'dir_six': [960, 1079],
               'dir_seven': [520, 944],
               'dir_eight': [193, 800],
               'dir_nine': [0, 500],
               'dir_ten': [195, 200],
               'dir_eleven': [520 , 56],
               'dir_twelve': [960, 0],}

#Level up an ability
def level_up(ability):
  PressKey(KEYS['Ctrl'])
  time.sleep(.01)
  KeyPress(KEYS[ability])
  time.sleep(.01)
  ReleaseKey(KEYS['Ctrl'])
  time.sleep(.01)  
  
  
#Use Q
def use_q(direction):
  pyautogui.moveTo(DIRECTIONS[direction][COORD_X], DIRECTIONS[direction][COORD_Y])
  KeyPress(KEYS['Q'])
  
#Use W (Attaching)
def use_w_attach():
  center_mouse()
  k = 200
  
  KeyPress(KEYS['W'])
  pyautogui.move(k, k)  #move to 9
  KeyPress(KEYS['W'])
  pyautogui.move(0, -k) #move to 6
  KeyPress(KEYS['W'])
  pyautogui.move(0, -k) #move to 3
  KeyPress(KEYS['W'])
  pyautogui.move(-k, 0) #move to 2
  KeyPress(KEYS['W'])
  pyautogui.move(-k, 0) #move to 1
  KeyPress(KEYS['W'])
  pyautogui.move(0, k)  #move to 4
  KeyPress(KEYS['W'])
  pyautogui.move(0, k)  #move to 7
  KeyPress(KEYS['W'])
  pyautogui.move(k, 0)  #move to 8
  KeyPress(KEYS['W'])
  
  center_mouse()


#Use W (Detaching)
def use_w_detach():
  center_mouse()
  KeyPress(KEYS['W'])


#Use E  
def use_e():
  center_mouse()
  KeyPress(KEYS['E'])


#Use R  
def use_ult(direction):
  pyautogui.moveTo(DIRECTIONS[direction][COORD_X], DIRECTIONS[direction][COORD_Y])
  KeyPress(KEYS['R'])
  time.sleep(.05)
  center_mouse()
  
#Buy Items
def go_shopping():
  return 0
  
  
#Recall
def recall():
  KeyPress(KEYS['B'])


#Use Ignite
def use_ignite():
  center_mouse()
  k = 200
  
  KeyPress(KEYS['F'])
  pyautogui.move(k, k)  #move to 9
  KeyPress(KEYS['F'])
  pyautogui.move(0, -k) #move to 6
  KeyPress(KEYS['F'])
  pyautogui.move(0, -k) #move to 3
  KeyPress(KEYS['F'])
  pyautogui.move(-k, 0) #move to 2
  KeyPress(KEYS['F'])
  pyautogui.move(-k, 0) #move to 1
  KeyPress(KEYS['F'])
  pyautogui.move(0, k)  #move to 4
  KeyPress(KEYS['F'])
  pyautogui.move(0, k)  #move to 7
  KeyPress(KEYS['F'])
  pyautogui.move(k, 0)  #move to 8
  KeyPress(KEYS['F'])
  
  center_mouse()


#Use Exhaust
def use_exhaust():
  center_mouse()
  k = 200
  
  KeyPress(KEYS['D'])
  pyautogui.move(k, k)  #move to 9
  KeyPress(KEYS['D'])
  pyautogui.move(0, -k) #move to 6
  KeyPress(KEYS['D'])
  pyautogui.move(0, -k) #move to 3
  KeyPress(KEYS['D'])
  pyautogui.move(-k, 0) #move to 2
  KeyPress(KEYS['D'])
  pyautogui.move(-k, 0) #move to 1
  KeyPress(KEYS['D'])
  pyautogui.move(0, k)  #move to 4
  KeyPress(KEYS['D'])
  pyautogui.move(0, k)  #move to 7
  KeyPress(KEYS['D'])
  pyautogui.move(k, 0)  #move to 8
  KeyPress(KEYS['D'])
  
  center_mouse()


#Use Heal (Summoner)
def use_heal_sum():
  center_mouse()
  KeyPress(KEYS['D'])
  
  
#Use a stealth ward
def place_stealthward():
  center_mouse()
  KeyPress(KEYS['4'])
  
  
#Use pinkward
def place_pinkward():
  return 0
  
  
#Use Redmeption
def use_redemption():
  return 0
  
  
#Be Toxic
toxic_phrases = ['GGEZ', 'Git gud', 'sup diff', 'GG uninstall', 'EZ uninstall', 'Noobs', 'ggez', 'sup gap', 'jg diff', 'ff15']
toxic_len = len(toxic_phrases) - 1

def being_toxic():
  KeyPress(KEYS['Enter'])
  time.sleep(0.01)
  pyautogui.write(toxic_phrases[random.randint(0,toxic_len)])
  time.sleep(0.01)
  KeyPress(KEYS['Enter'])
  
  
#Chit-chat
quotes = ["Keep an eye out for red dot, Book! It's gotta be here somewhere.", "Where to, Book? Purr~", "Book, float us that-a-way!", "I hiss at you, giant pile of stones! Hiss!", "Cat-tack!", "We got the zoomies!", "OwO wats dis~?", "You look like unscratched furniture!", "I'm Yuumi, and you're warm!", "Beep boop! Hi I'm Yuumi bot!", ]
quotes_len = len(quotes) - 1

def chitchat():
  KeyPress(KEYS['Enter'])
  time.sleep(0.01)
  pyautogui.write(quotes[random.randint(0,quotes_len)])
  time.sleep(0.01)
  KeyPress(KEYS['Enter'])
  
  
def center_mouse():
  pyautogui.moveTo(960, 500)