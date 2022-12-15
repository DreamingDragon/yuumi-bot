# bot.py
import os
import random
import discord
from gameactions import *
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

command_q_1 = ['**Entr0py**: Q. one.', ]
command_q_2 = ['**Entr0py**: Q, two.', '**Entr0py**: Two, two.' '**Entr0py**: Two.']
command_q_3 = ['**Entr0py**: Q, three.', '**Entr0py**: Three.', '**Entr0py**: Three, three.', '**Entr0py**: Through three.' ]
command_q_4 = ['**Entr0py**: Q, four.', '**Entr0py**: Four, four.', '**Entr0py**: Hue for.', '**Entr0py**: Four.' ]
command_q_5 = ['**Entr0py**: Five.', '**Entr0py**: Q, five.', '**Entr0py**: Five, five.' ]
command_q_6 = ['**Entr0py**: Six.', '**Entr0py**: Q, six.', '**Entr0py**: Six, six.', '**Entr0py**: Through six.']
command_q_7 = ['**Entr0py**: Q, seven.', '**Entr0py**: Seven, seven.', '**Entr0py**: Thank you, seven.', '**Entr0py**: Seven.']
command_q_8 = ['**Entr0py**: Q, eight.', '**Entr0py**: Eight.']
command_q_9 = ['**Entr0py**: Q. nine.', '**Entr0py**: Nine.']
command_q_10 = ['**Entr0py**: Qan.', '**Entr0py**: Q, Ten.']
command_q_11 = ['**Entr0py**: Q. eleven.', '**Entr0py**: Eleven.']
command_q_12 = ['**Entr0py**: Q. twelve.', '**Entr0py**: Q. twel.', '**Entr0py**: Twelve.']
command_w_attach = ['**Entr0py**: Press W.', '**Entr0py**: Attach to me.', '**Entr0py**: Follow me.', '**Entr0py**: Attach.']
command_w_detach = ['**Entr0py**: Press W.', '**Entr0py**: Stop following.', '**Entr0py**: Detach.']
command_e = ['**Entr0py**: Heal me.', '**Entr0py**: Save me.', '**Entr0py**: Press.', '**Entr0py**: Press e.', '**Entr0py**: Kill me.']
command_r_1 = ['**Entr0py**: Old Juan.', '**Entr0py**: Cult one.', '**Entr0py**: Old one.', '**Entr0py**: Fault one.', '**Entr0py**: Alt one.', '**Entr0py**: R one.']
command_r_2 = ['**Entr0py**: Alt two.', '**Entr0py**: R. two.', '**Entr0py**: Alt to.']
command_r_3 = ['**Entr0py**: All three.', '**Entr0py**: Alt three.', '**Entr0py**: Cult three.', '**Entr0py**: R. three.']
command_r_4 = ['**Entr0py**: Alt for.', '**Entr0py**: Holt for.', '**Entr0py**: R. four.']
command_r_5 = ['**Entr0py**: R. five.', '**Entr0py**: Alt five.']
command_r_6 = ['**Entr0py**: Alt six.', '**Entr0py**: R. six.']
command_r_7 = ['**Entr0py**: Alt seven.', '**Entr0py**: R. seven.']
command_r_8 = ['**Entr0py**: R. eight.', '**Entr0py**: Alt eight.', '**Entr0py**: Old eight.', '**Entr0py**: All eight.']
command_r_9 = ['**Entr0py**: Alt nine.', '**Entr0py**: All nine.', '**Entr0py**: Holt nine.', '**Entr0py**: R. nine.']
command_r_10 = ['**Entr0py**: R. ten.', '**Entr0py**: Alt ten.', '**Entr0py**: All ten.']
command_r_11 = ['**Entr0py**: Alt eleven.', '**Entr0py**: R. eleven.', '**Entr0py**: All eleven.']
command_r_12 = ['**Entr0py**: R. twel.', '**Entr0py**: R. twelve.', '**Entr0py**: Alt twelve.', '**Entr0py**: Alt twel.', '**Entr0py**: All twel.', '**Entr0py**: All twelve.' ]
command_recall = ['**Entr0py**: Press B.', '**Entr0py**: Back.', '**Entr0py**: Base.', '**Entr0py**: Space.', '**Entr0py**: Bas.', '**Entr0py**: Recall.']
command_ward = ['**Entr0py**: Ward here.', '**Entr0py**: Toward here.', '**Entr0py**: Board here.', '**Entr0py**: Word here.']
command_toxic = ['**Entr0py**: Be toxic.', '**Entr0py**: Detoxic.']
command_chitchat = ['**Entr0py**: Chit chat.', '**Entr0py**: Say something.', '**Entr0py**: Something?']
command_level_up_q = ['**Entr0py**: Level up, Q.', '**Entr0py**: Lovell up, Q.', '**Entr0py**: Level Q.', '**Entr0py**: Lovell, Q.']
command_level_up_w = ['**Entr0py**: Level W.', '**Entr0py**: Level up, W.', '**Entr0py**: Lovell up, W.', '**Entr0py**: Lovell, W.']
command_level_up_e = ['**Entr0py**: Level E.', '**Entr0py**: Lovell E.']
command_level_up_r = ['**Entr0py**: Lovell, R.', '**Entr0py**: Level up, r.', '**Entr0py**: Level up, Alt.', '**Entr0py**: Level up old.', '**Entr0py**: Level Alt.' '**Entr0py**: Level r.']
command_level_up_generic = ['**Entr0py**: Level up.', '**Entr0py**: Lovell.', '**Entr0py**: Love.', '**Entr0py**: Le.', '**Entr0py**: Leve.']
command_ignite = ['**Entr0py**: Use ignite.', '**Entr0py**: Ignite.']
command_exhaust = ['**Entr0py**: Use exhaust.', '**Entr0py**: Exhaust.']
command_shop = ['**Entr0py**: Go shopping.', '**Entr0py**: Go buy.', '**Entr0py**: Go shop.', '**Entr0py**: Buy items.']
debug_center = ['**Entr0py**: Center mouse.']

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content in command_level_up_q:
        level_up('Q')
        responce = 'Leveling Q'
        await message.channel.send(responce)
    
    if message.content in command_level_up_w:
        level_up('W')
        responce = 'Leveling W'
        await message.channel.send(responce)
        
    if message.content in command_level_up_e:
        level_up('E')
        responce = 'Leveling E'
        await message.channel.send(responce)
        
    if message.content in command_level_up_r:
        level_up('R')
        responce = 'Leveling R'
        await message.channel.send(responce)
        
    if message.content in command_level_up_generic:
        level_up('R')
        level_up('E')
        level_up('Q')
        level_up('W')
        responce = 'Auto Level'
        await message.channel.send(responce)
    
    if message.content in command_q_1:
        use_q('dir_one')
        response = 'Q towards 1'
        await message.channel.send(response)
    
    if message.content in command_q_2:
        use_q('dir_two')
        response = 'Q towards 2'
        await message.channel.send(response)
    
    if message.content in command_q_3:
        use_q('dir_three')
        response = 'Q towards 3'
        await message.channel.send(response)
    
    if message.content in command_q_4:
        use_q('dir_four')
        response = 'Q towards 4'
        await message.channel.send(response)
        
    if message.content in command_q_5:
        use_q('dir_five')
        response = 'Q towards 5'
        await message.channel.send(response)
        
    if message.content in command_q_6:
        use_q('dir_six')
        response = 'Q towards 6'
        await message.channel.send(response)
        
    if message.content in command_q_7:
        use_q('dir_seven')
        response = 'Q towards 7'
        await message.channel.send(response)
        
    if message.content in command_q_8:
        use_q('dir_eight')
        response = 'Q towards 8'
        await message.channel.send(response)
        
    if message.content in command_q_9:
        use_q('dir_nine')
        response = 'Q towards 9'
        await message.channel.send(response)
    
    if message.content in command_q_10:
        use_q('dir_ten')
        response = 'Q towards 10'
        await message.channel.send(response)
    
    if message.content in command_q_11:
        use_q('dir_eleven')
        response = 'Q towards 11'
        await message.channel.send(response)
    
    if message.content in command_q_12:
        use_q('dir_twelve')
        response = 'Q towards 12'
        await message.channel.send(response)
    
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
    
    if message.content in command_r_1:
        use_ult('dir_one')
        response = 'R towards 1'
        await message.channel.send(response)
        
    if message.content in command_r_2:
        use_ult('dir_two')
        response = 'R towards 2'
        await message.channel.send(response)
        
    if message.content in command_r_3:
        use_ult('dir_three')
        response = 'R towards 3'
        await message.channel.send(response)
        
    if message.content in command_r_4:
        use_ult('dir_four')
        response = 'R towards 4'
        await message.channel.send(response)
    
    if message.content in command_r_5:
        use_ult('dir_five')
        response = 'R towards 5'
        await message.channel.send(response)
    
    if message.content in command_r_6:
        use_ult('dir_six')
        response = 'R towards 6'
        await message.channel.send(response)
    
    if message.content in command_r_7:
        use_ult('dir_seven')
        response = 'R towards 7'
        await message.channel.send(response)
    
    if message.content in command_r_8:
        use_ult('dir_eight')
        response = 'R towards 8'
        await message.channel.send(response)
    
    if message.content in command_r_9:
        use_ult('dir_nine')
        response = 'R towards 9'
        await message.channel.send(response)
    
    if message.content in command_r_10:
        use_ult('dir_ten')
        response = 'R towards 10'
        await message.channel.send(response)
    
    if message.content in command_r_11:
        use_ult('dir_eleven')
        response = 'R towards 11'
        await message.channel.send(response)
        
    if message.content in command_r_12:
        use_ult('dir_twelve')
        response = 'R towards 12'
        await message.channel.send(response)
    
    if message.content in command_ignite:
        use_ignite()
        response = 'Igniting'
        await message.channel.send(response)
    
    if message.content in command_exhaust:
        use_exhaust()
        response = 'Exhausting'
        await message.channel.send(response)
    
    if message.content in command_recall:
        recall()
        response = 'Recalling'
        await message.channel.send(response)
        
    if message.content in command_ward:
        place_stealthward()
        response = 'Placing Stealth Ward'
        await message.channel.send(response)    
    
    if message.content in command_shop:
        go_shopping()
        response = 'Cha-Ching $$$'
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