# bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'Entr0py: Heal me.':
        response = 'Pressing E'
        await message.channel.send(response)
        
    if message.content == 'Entr0py: Save me.':
        response = 'Pressing E'
        await message.channel.send(response)
        
    if message.content == 'Entr0py: Use Q.':
        response = 'Pressing Q'
        await message.channel.send(response)    
        
client.run(TOKEN)