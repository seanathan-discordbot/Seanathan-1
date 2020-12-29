import discord
from discord.ext import commands
import os
import asyncio

Token #add discord bot token here 
client = commands.Bot(command_prefix = '$')
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def hello(ctx):
    await ctx.message.channel.send('Hello!')
@client.command()
async def sean(ctx):
    await ctx.message.channel.send('Sean is short for Seanathan')

@client.command()
async def delay(ctx):
    await asyncio.sleep(60)
    await ctx.message.channel.send('Delay')

@client.command()
async def echo(ctx, *, returnStatement):
    await ctx.send(returnStatement)
@client.command()
async def is_num(ctx,*,returnStatement):
    if returnStatement.isdigit()==False:
        await ctx.send('Please enter a number')
    else:
        await ctx.send(returnStatement)
        

@client.command()
async def ping(ctx):
    await ctx.send(ctx.author.mention)
 """
incorporate into a cog called remind. 
Also need to test how remind works with multiple reminders
"""
@client.command() #work on this tommorow 
async def remind(ctx,*,returnStatement):
    if returnStatement.isdigit()==False:
        await ctx.send('Please enter a number')
    else:
        await ctx.send("I'll remind you in "+returnStatement)
        pause=int(returnStatement)
        await asyncio.sleep(pause)
        await ctx.send(ctx.author.mention+" your reminder")
   client.run(Token)
