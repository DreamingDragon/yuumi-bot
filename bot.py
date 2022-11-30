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
command_w = ['Entr0py: Press W.', 'Entr0py: Attach to me.', 'Entr0py: Follow me.', 'Entr0py: Stop following.', 'Entr0py: Attach.', 'Entr0py: Detach.']
command_e = ['Entr0py: Heal me.', 'Entr0py: Save me.', 'Entr0py: Press.', 'Entr0py: Press e.']

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content in command_w:
        response = 'Pressing W'
        await message.channel.send(response)
        use_w()
    
    if message.content in command_e:
        response = 'Pressing E'
        await message.channel.send(response)
        use_e()
        
    if message.content == 'Entr0py: Be toxic.':
        response = 'Being Toxic'
        await message.channel.send(response) 
        being_toxic()
        
client.run(TOKEN)