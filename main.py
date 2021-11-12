import discord
import constants
import dnd5erequests
from replit import db
from keep_alive import keep_alive

client = discord.Client()


# 1. api_dev_key - which is your unique API Developers Key.
# 2. api_option - set as paste, this will indicate you want to create a new paste.
# 3. api_paste_code - this is the text that will be written inside your paste.
# https://pastebin.com/asRbutde


if "responding" not in db.keys():
  db["responding"] = True




@client.event
async def on_ready():
  print('Logged in as {0.user}.format(client)')

@client.event
async def on_message(message):

  if message.author == client.user:
    return
  if str(message.channel) != "bot-channel":
    return

  if db["responding"]:
     
    if message.content.startswith('#commands'):
      await message.channel.send("#getClasses " + "\n" + "#getRaces" + "\n" + "#<class> spells" + "\n" + "#feat <feat Index>" + "\n" + "#all-feats" + "\n" + "#feat-name <name>" + "\n" + "#get-spells <level>" + "\n" + "spell <index>" + "\n" + "spell-name <name>" + "\n" + "#all-condition" + "#condition <Name>")

    if message.content.startswith('#getClasses'):
      await message.channel.send(dnd5erequests.get_classes())

    if message.content.startswith("#getRaces"):
       await message.channel.send(dnd5erequests.get_races())

    if message.content.startswith("#wizard spells"):
      await message.channel.send(dnd5erequests.get_wizard_spell())

    if message.content.startswith("#warlock spells"):
      await message.channel.send(dnd5erequests.get_warlock_spell())

    if message.content.startswith("#bard spells"):
      await message.channel.send(dnd5erequests.get_bard_spell())

    if message.content.startswith("#druid spells"):
      await message.channel.send(dnd5erequests.get_druid_spell())

    if message.content.startswith("#cleric spells"):
      await message.channel.send(dnd5erequests.get_cleric_spell())

    if message.content.startswith("#paladin spells"):
      await message.channel.send(dnd5erequests.get_paladin_spell())

    if message.content.startswith("#sorcerer spells"):
      await message.channel.send(dnd5erequests.get_sorcerer_spell())

    if message.content.startswith("#feat "):
      value = message.content.split("#feat ", 1)[1]
      await message.channel.send(dnd5erequests.get_specific_feat(value))

    if message.content.startswith("#feat-name "):
      value = message.content.split("#feat-name ", 1)[1]
      await message.channel.send(dnd5erequests.get_feats_with_name(value))
    
    if message.content.startswith("#all-feats"):
      await message.channel.send(dnd5erequests.get_all_feats())

    if message.content.startswith("#get-spells "):
      value = message.content.split("#get-spells ", 1)[1]
      await message.channel.send(dnd5erequests.get_spells_with_level(value))

    if message.content.startswith("#spell "):
      value = message.content.split("#spell ", 1)[1]
      await message.channel.send(dnd5erequests.get_specific_spell(value))

    if message.content.startswith("#spell-name "):
      value = message.content.split("#spell-name ", 1)[1]
      await message.channel.send("Format -> Name: Index" + "\n" + "Type #spell <Index> (Without brackets) to view spell description")
      await message.channel.send(dnd5erequests.get_spells_with_name(value))

    if message.content.startswith("#all-condition"):
      await message.channel.send(dnd5erequests.get_all_condition())

    if message.content.startswith("#condition "):
      value = message.content.split("#condition ", 1)[1]
      await message.channel.send(dnd5erequests.get_specific_condition(value))

    if message.content.startswith("#mameds"):
      await message.channel.send(dnd5erequests.get_mameds())

    if message.content.startswith("#reallyBadNews"):
      await message.channel.send("https://www.youtube.com/watch?v=J-DFfBUA6vM")


  
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
