import discord 
import os 
from discord.ext import commands
Token #the token of the bot
client=commands.Bot(command_prefix="!")

@client.command()
#allows owner to load a cog if they make changes while bot is online 
async def load(ctx,extension):
    await ctx.message.channel.send('loaded')
    client.load_extension(f'cogs.{extension}')

@client.command()
#allows user to unload cog if changes are made while bot is running
async def unload(ctx,extension):
    await.ctx.message.send('unloaded')
    client.unload_extension(f'cogs.{extension}')

# Runs at bot startup to load all cogs
for filename in os.listdir(r'C:\Users\rowlas2\Documents\Seanathan\cogs'): #replace path with your own file
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}') 
client.run(Token)
