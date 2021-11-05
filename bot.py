import discord
From discord.ext import commands

bot = commands.Bot(command_prefix= '[')

@bot.event
async def on_ready():
    print(">>Bot is online <<")
    
bot.run(OTA0MjA2Mzc4ODI5MjMwMTMx.YX4J0A.JlIYYHH6pQrlMwFRrwe2vA4fxsw)