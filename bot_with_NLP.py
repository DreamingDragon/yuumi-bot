# bot.py
import os
import random
import discord
from gameactions import *
from dotenv import load_dotenv
from lingual_approximator import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

command_q_1 = ["Q ONE" ]
command_q_2 = ["Q TWO"]
command_q_3 = ["Q THREE"]
command_q_4 = ["Q FOUR"]
command_q_5 = ["Q FIVE"]
command_q_6 = ["Q SIX"]
command_q_7 = ["Q SEVEN"]
command_q_8 = ["Q EIGHT"]
command_q_9 = ["Q NINE"]
command_q_10 = ["Q TEN"]
command_q_11 = ["Q ELEVEN"]
command_q_12 = ["Q TWELVE"]
command_w_attach = ["FOLLOW ME"]
command_w_detach = ["STOP FOLLOWING"]
command_e = ["HEAL ME", "SHIELD ME"]
command_r_1 = ["ALT ONE", "R ONE"]
command_r_2 = ["ALT TWO", "R TWO"]
command_r_3 = ["ALT THREE", "R THREE"]
command_r_4 = ["ALT FOUR", "R FOUR"]
command_r_5 = ["ALT FIVE", "R FIVE"]
command_r_6 = ["ALT SIX", "R SIX"]
command_r_7 = ["ALT SEVEN", "R SEVEN"]
command_r_8 = ["ALT EIGHT", "R EIGHT"]
command_r_9 = ["ALT NINE", "R NINE"]
command_r_10 = ["ALT NINE", "R NINE"]
command_r_11 = ["ALT ELEVEN", "R ELEVEN"]
command_r_12 = ["ALT TWELVE", "R TWELVE"]
command_recall = ["RECALL", "BASE", "BACK"]
command_ward = ["WARD HERE"]
command_toxic = ["BE TOXIC"]
command_chitchat = ["CHIT CHAT", "SAY SOMETHING"]
command_level_up_q = ["LEVEL UP Q"]
command_level_up_w = ["LEVEL UP W"]
command_level_up_e = ["LEVEL UP E"]
command_level_up_r = ["LEVEL UP R", "LEVEL ALT"]
command_level_up_generic = ["LEVEL UP"]
command_ignite = ["IGNITE"]
command_exhaust = ["EXHAUST"]
command_shop = ['**Entr0py**: Go shopping.', '**Entr0py**: Go buy.', '**Entr0py**: Go shop.', '**Entr0py**: Buy items.']
debug_center = ["CENTER MOUSE"]

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    #Processing Phonetics
    possibleCommand = message.content
    #debug
    print(possibleCommand)
    processedCommandTuple = phonetic_approximant(possibleCommand)
    #debug
    print(processedCommandTuple)
    
    if processedCommandTuple[1] < 1:
        processedCommand = processedCommandTuple[0]
        
        if processedCommand in command_level_up_q:
            level_up('Q')
            responce = 'Leveling Q'
            await message.channel.send(responce)
        
        if processedCommand in command_level_up_w:
            level_up('W')
            responce = 'Leveling W'
            await message.channel.send(responce)
            
        if processedCommand in command_level_up_e:
            level_up('E')
            responce = 'Leveling E'
            await message.channel.send(responce)
            
        if processedCommand in command_level_up_r:
            level_up('R')
            responce = 'Leveling R'
            await message.channel.send(responce)
            
        if processedCommand in command_level_up_generic:
            level_up('R')
            level_up('E')
            level_up('Q')
            level_up('W')
            responce = 'Auto Level'
            await message.channel.send(responce)
        
        if processedCommand in command_q_1:
            use_q('dir_one')
            response = 'Q towards 1'
            await message.channel.send(response)
        
        if processedCommand in command_q_2:
            use_q('dir_two')
            response = 'Q towards 2'
            await message.channel.send(response)
        
        if processedCommand in command_q_3:
            use_q('dir_three')
            response = 'Q towards 3'
            await message.channel.send(response)
        
        if processedCommand in command_q_4:
            use_q('dir_four')
            response = 'Q towards 4'
            await message.channel.send(response)
            
        if processedCommand in command_q_5:
            use_q('dir_five')
            response = 'Q towards 5'
            await message.channel.send(response)
            
        if processedCommand in command_q_6:
            use_q('dir_six')
            response = 'Q towards 6'
            await message.channel.send(response)
            
        if processedCommand in command_q_7:
            use_q('dir_seven')
            response = 'Q towards 7'
            await message.channel.send(response)
            
        if processedCommand in command_q_8:
            use_q('dir_eight')
            response = 'Q towards 8'
            await message.channel.send(response)
            
        if processedCommand in command_q_9:
            use_q('dir_nine')
            response = 'Q towards 9'
            await message.channel.send(response)
        
        if processedCommand in command_q_10:
            use_q('dir_ten')
            response = 'Q towards 10'
            await message.channel.send(response)
        
        if processedCommand in command_q_11:
            use_q('dir_eleven')
            response = 'Q towards 11'
            await message.channel.send(response)
        
        if processedCommand in command_q_12:
            use_q('dir_twelve')
            response = 'Q towards 12'
            await message.channel.send(response)
        
        if processedCommand in command_w_attach:
            use_w_attach()
            response = 'Attaching'
            await message.channel.send(response)        
        
        if processedCommand in command_w_detach:
            use_w_detach()
            response = 'Detaching'
            await message.channel.send(response)
        
        if processedCommand in command_e:
            use_e()
            response = 'Pressing E'
            await message.channel.send(response)        
        
        if processedCommand in command_r_1:
            use_ult('dir_one')
            response = 'R towards 1'
            await message.channel.send(response)
            
        if processedCommand in command_r_2:
            use_ult('dir_two')
            response = 'R towards 2'
            await message.channel.send(response)
            
        if processedCommand in command_r_3:
            use_ult('dir_three')
            response = 'R towards 3'
            await message.channel.send(response)
            
        if processedCommand in command_r_4:
            use_ult('dir_four')
            response = 'R towards 4'
            await message.channel.send(response)
        
        if processedCommand in command_r_5:
            use_ult('dir_five')
            response = 'R towards 5'
            await message.channel.send(response)
        
        if processedCommand in command_r_6:
            use_ult('dir_six')
            response = 'R towards 6'
            await message.channel.send(response)
        
        if processedCommand in command_r_7:
            use_ult('dir_seven')
            response = 'R towards 7'
            await message.channel.send(response)
        
        if processedCommand in command_r_8:
            use_ult('dir_eight')
            response = 'R towards 8'
            await message.channel.send(response)
        
        if processedCommand in command_r_9:
            use_ult('dir_nine')
            response = 'R towards 9'
            await message.channel.send(response)
        
        if processedCommand in command_r_10:
            use_ult('dir_ten')
            response = 'R towards 10'
            await message.channel.send(response)
        
        if processedCommand in command_r_11:
            use_ult('dir_eleven')
            response = 'R towards 11'
            await message.channel.send(response)
            
        if processedCommand in command_r_12:
            use_ult('dir_twelve')
            response = 'R towards 12'
            await message.channel.send(response)
        
        if processedCommand in command_ignite:
            use_ignite()
            response = 'Igniting'
            await message.channel.send(response)
        
        if processedCommand in command_exhaust:
            use_exhaust()
            response = 'Exhausting'
            await message.channel.send(response)
        
        if processedCommand in command_recall:
            recall()
            response = 'Recalling'
            await message.channel.send(response)
            
        if processedCommand in command_ward:
            place_stealthward()
            response = 'Placing Stealth Ward'
            await message.channel.send(response)    
        
        if processedCommand in command_shop:
            go_shopping()
            response = 'Cha-Ching $$$'
            await message.channel.send(response)    
        
        if processedCommand in command_toxic:
            being_toxic()
            response = 'Being Toxic'
            await message.channel.send(response) 

        if processedCommand in command_chitchat:
            chitchat()
            response = 'Chit chatting'
            await message.channel.send(response) 

        if processedCommand in debug_center:
            center_mouse()
            response = 'Centering mouse'
            await message.channel.send(response)
            
client.run(TOKEN)