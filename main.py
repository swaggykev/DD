import discord
import os
from dice import *
from istats import *
from helps import *
from discord.utils import get

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == ('$gm'):
        member = message.author
        role = get(message.guild.roles, name='GM')
        await member.add_roles(role)

    if message.content.startswith('$total'):
      totalstr = message.content.split()
      dies = totalstr[1]
      times = int(totalstr[2])
      adds = int(totalstr[3])
      await message.channel.send('Roll is '+ str(total(dies,times,adds)))

    if message.content == ('$characterstats'):
      await message.channel.send(stats())
    
    if message.content == ('$help'):
      await message.channel.send(helppoint())
      
  
    
client.run(('ENTER YOUR DISCORD BOT TOKEN HERE'))
