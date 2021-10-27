import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()
my_secret = os.environ['discord_token']


if "responding" not in db.keys():
  db["responding"] = True


def get_quote():
  response = requests.get("https://zenquote.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return quote

def get_classes():
  response = requests.get("https://www.dnd5eapi.co/api/classes/")
  json_data = json.loads(response.text)
  classes = []
  for item in json_data['results']:
    classes.append(item['name'])

  return classes

@client.event
async def on_ready():
  print('Logged in as {0.user}.format(client)')
  print(get_classes())

@client.event
async def on_message(message):
  print(message.channel)
  print("bot-channel")

  if message.author == client.user:
    print("teste")
    return
  if str(message.channel) != "bot-channel":
    print("outro teste")
    return

  if db["responding"]:
    
    if message.content.startswith('$getClasses'):
      await message.channel.send(get_classes())

    if message.content.startswith("$wizard spells"):
      print("wizard spells")  

    if message.content.startswith("$bard spells"):
      print("Bard spells")

    if message.startswith("$cleric spells"):
      print("Cleric spells")

  
  if message.startswith("$responding"):
    value = message.content.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on")
    else:
      db["responding"] = False
      await message.channel.send("Responding is false")

keep_alive()
client.run(my_secret)
