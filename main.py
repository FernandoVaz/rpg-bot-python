import discord
import os
import requests
import json
import constants
from replit import db
from keep_alive import keep_alive

client = discord.Client()


# 1. api_dev_key - which is your unique API Developers Key.
# 2. api_option - set as paste, this will indicate you want to create a new paste.
# 3. api_paste_code - this is the text that will be written inside your paste.
# https://pastebin.com/asRbutde


if "responding" not in db.keys():
  db["responding"] = True

def get_classes():
  response = requests.get("https://www.dnd5eapi.co/api/classes/")
  json_data = json.loads(response.text)
  classes = ""
  for item in json_data['results']:
    classes += item['name'] + ", "

  return classes

def get_races():
  response = requests.get("https://www.dnd5eapi.co/api/races/")
  json_data = json.loads(response.text)
  races = ""
  for item in json_data['results']:
    races += item['name'] + ", "

  return races

def get_wizard_spell():
  responseDnd5eApi = requests.get("https://www.dnd5eapi.co/api/classes/wizard/spells/")
  json_data_dnd = json.loads(responseDnd5eApi.text)
  spells = ""
  for item in json_data_dnd['results']:
    spells += item['name'] + ", "

  login = requests.post("https://pastebin.com/api/api_login.php", data=constants.login_data)
  constants.paste_data['api_user_key'] = login.text
  constants.paste_data['api_paste_code'] = spells
  constants.paste_data['api_paste_name'] = 'Wizard Spells'
  
  r = requests.post("https://pastebin.com/api/api_post.php", data=constants.paste_data)
  return r.text

def get_cleric_spell():
  responseDnd5eApi = requests.get("https://www.dnd5eapi.co/api/classes/cleric/spells/")
  json_data_dnd = json.loads(responseDnd5eApi.text)
  spells = ""
  for item in json_data_dnd['results']:
    spells += item['name'] + ", "

  login = requests.post("https://pastebin.com/api/api_login.php", data=constants.login_data)
  constants.paste_data['api_user_key'] = login.text
  constants.paste_data['api_paste_code'] = spells
  constants.paste_data['api_paste_name'] = 'Cleric Spells'
  
  r = requests.post("https://pastebin.com/api/api_post.php", data=constants.paste_data)
  return r.text

def get_bard_spell():
  responseDnd5eApi = requests.get("https://www.dnd5eapi.co/api/classes/wizard/spells/")
  json_data_dnd = json.loads(responseDnd5eApi.text)
  spells = ""
  for item in json_data_dnd['results']:
    spells += item['name'] + ", "

  login = requests.post("https://pastebin.com/api/api_login.php", data=constants.login_data)
  constants.paste_data['api_user_key'] = login.text
  constants.paste_data['api_paste_code'] = spells
  constants.paste_data['api_paste_name'] = 'Bard Spells'
  
  r = requests.post("https://pastebin.com/api/api_post.php", data=constants.paste_data)
  return r.text

def get_warlock_spell():
  responseDnd5eApi = requests.get("https://www.dnd5eapi.co/api/classes/warlock/spells/")
  json_data_dnd = json.loads(responseDnd5eApi.text)
  spells = ""
  for item in json_data_dnd['results']:
    spells += item['name'] + ", "

  login = requests.post("https://pastebin.com/api/api_login.php", data=constants.login_data)
  constants.paste_data['api_user_key'] = login.text
  constants.paste_data['api_paste_code'] = spells
  constants.paste_data['api_paste_name'] = 'Warlock Spells'
  
  r = requests.post("https://pastebin.com/api/api_post.php", data=constants.paste_data)
  return r.text

def get_paladin_spell():
  responseDnd5eApi = requests.get("https://www.dnd5eapi.co/api/classes/paladin/spells/")
  json_data_dnd = json.loads(responseDnd5eApi.text)
  spells = ""
  for item in json_data_dnd['results']:
    spells += item['name'] + ", "

  login = requests.post("https://pastebin.com/api/api_login.php", data=constants.login_data)
  constants.paste_data['api_user_key'] = login.text
  constants.paste_data['api_paste_code'] = spells
  constants.paste_data['api_paste_name'] = 'Paladin Spells'
  
  r = requests.post("https://pastebin.com/api/api_post.php", data=constants.paste_data)
  return r.text

def get_druid_spell():
  responseDnd5eApi = requests.get("https://www.dnd5eapi.co/api/classes/druid/spells/")
  json_data_dnd = json.loads(responseDnd5eApi.text)
  spells = ""
  for item in json_data_dnd['results']:
    spells += item['name'] + ", "

  login = requests.post("https://pastebin.com/api/api_login.php", data=constants.login_data)
  constants.paste_data['api_user_key'] = login.text
  constants.paste_data['api_paste_code'] = spells
  constants.paste_data['api_paste_name'] = 'Paladin Spells'
  
  r = requests.post("https://pastebin.com/api/api_post.php", data=constants.paste_data)
  return r.text

def get_sorcerer_spell():
  responseDnd5eApi = requests.get("https://www.dnd5eapi.co/api/classes/sorcerer/spells/")
  json_data_dnd = json.loads(responseDnd5eApi.text)
  spells = ""
  for item in json_data_dnd['results']:
    spells += item['name'] + ", "

  login = requests.post("https://pastebin.com/api/api_login.php", data=constants.login_data)
  constants.paste_data['api_user_key'] = login.text
  constants.paste_data['api_paste_code'] = spells
  constants.paste_data['api_paste_name'] = 'Sorcerer Spells'
  
  r = requests.post("https://pastebin.com/api/api_post.php", data=constants.paste_data)
  return r.text

@client.event
async def on_ready():
  print(get_wizard_spell())
  print('Logged in as {0.user}.format(client)')

@client.event
async def on_message(message):

  if message.author == client.user:
    return
  if str(message.channel) != "bot-channel":
    return

  if db["responding"]:
    
    if message.content.startswith('$getClasses'):
      await message.channel.send(get_classes())

    if message.content.startswith("$getRaces"):
       await message.channel.send(get_races())

    if message.content.startswith("$bard spells"):
      print("Bard spells")

    if message.content.startswith("$cleric spells"):
      print("Cleric spells")

    if message.content.startswith("$wizard spells"):
      await message.channel.send(get_wizard_spell())

    if message.content.startswith("$warlock spells"):
      await message.channel.send(get_warlock_spell())

    if message.content.startswith("$bard spells"):
      await message.channel.send(get_bard_spell())

    if message.content.startswith("$druid spells"):
      await message.channel.send(get_druid_spell())

    if message.content.startswith("$cleric spells"):
      await message.channel.send(get_cleric_spell())

    if message.content.startswith("$paladin spells"):
      await message.channel.send(get_paladin_spell())

    if message.content.startswith("$sorcerer spells"):
      await message.channel.send(get_sorcerer_spell())

  
  if message.content.startswith("$responding"):
    value = message.content.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on")
    else:
      db["responding"] = False
      await message.channel.send("Responding is false")

keep_alive()
client.run(constants.github_secret)
