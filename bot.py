# bot.py
import os
import random
import discord
from gameactions import *
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

command_q = []
command_w_attach = ['Entr0py: Press W.', 'Entr0py: Attach to me.', 'Entr0py: Follow me.', 'Entr0py: Attach.']
command_w_detach = ['Entr0py: Press W.', 'Entr0py: Stop following.', 'Entr0py: Detach.']
command_e = ['Entr0py: Heal me.', 'Entr0py: Save me.', 'Entr0py: Press.', 'Entr0py: Press e.', 'Entr0py: Kill me.']
command_recall = ['Entr0py: Press B.', 'Entr0py: Back.', 'Entr0py: Base.', 'Entr0py: Space.', 'Entr0py: Bas.', 'Entr0py: Recall.']
command_ward = ['Entr0py: Ward here.', 'Entr0py: Toward here.', 'Entr0py: Board here.', 'Entr0py: Word here.']
command_toxic = ['Entr0py: Be toxic.', 'Entr0py: Detoxic.']
command_chitchat = ['Entr0py: Chit chat.', 'Entr0py: Say something.', 'Entr0py: Something?']
debug_center = ['Entr0py: Center mouse.']

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content in command_w_attach:
        use_w_attach()
        response = 'Attaching'
        await message.channel.send(response)        
    
    if message.content in command_w_detach:
        use_w_detach()
        response = 'Detaching'
        await message.channel.send(response)
    
    if message.content in command_e:
        use_e()
        response = 'Pressing E'
        await message.channel.send(response)        
    
    if message.content in command_recall:
        recall()
        response = 'Recalling'
        await message.channel.send(response)
        
    if message.content in command_ward:
        place_stealthward()
        response = 'Placing Stealth Ward'
        await message.channel.send(response)    
        
    if message.content in command_toxic:
        being_toxic()
        response = 'Being Toxic'
        await message.channel.send(response) 

    if message.content in command_chitchat:
        chitchat()
        response = 'Chit chatting'
        await message.channel.send(response) 

    if message.content in debug_center:
        center_mouse()
        response = 'Centering mouse'
        await message.channel.send(response)
        
client.run(TOKEN)