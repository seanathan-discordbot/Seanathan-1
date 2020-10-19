import discord

TOKEN = 'NzY3MjM0NzAzMTYxMjk0ODU4.X4u8_w.hxrXVVzZfpK7NlGPEp8p1hcNiKE'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)