import discord
import os

client = discord.Client()
my_secret = os.environ['discord_token']

@client.event
async def on_ready():
  print('Logged in as {0.user}.format(client)')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send("hello")
  
client.run(my_secret)
