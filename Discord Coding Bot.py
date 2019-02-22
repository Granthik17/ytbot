import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "^")

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='with V£NØM'))
    print("Bot is online and connected to Discord")
    
@client.event
async def on_message(message):
    if message.content.startswith('^ping'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.startswith('^say'):
        args = message.content.split(" ")
        #args[0] = ^say
        #args[1] = Hey
        #args[2] = There
        #args[1:] = Hey There
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))

client.run("NTQ4MDM5NDA2ODQyNDEzMDU3.D1AOsQ.Kij1WIoINwSpWVx1S5Sx_gUnQwo")
