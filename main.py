import discord
from discord.ext import commands

TOKEN = 'MTA3NDEwMzc2ODM0MzM5NjQ3Mg.GS6fOX.Ma7ESAD6jYjefVCeq_XE0vlYYcS6RSDUlyCv44'
intents = discord.Intents.default()
intents.message_content = True


client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
    print('bot ready')
    
@client.event
async def on_message(message):
    if (message.author.bot):
        return 
    inStr=message.content
    await message.channel.send('Message: '+inStr)

    
client.run(TOKEN)