import requests
import json
import constants

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

##
## SPELLS
## 
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

def get_spells_with_level(level):
  responseDnd5eApi = requests.get("https://www.dnd5eapi.co/api/spells?level=" + level)
  json_data_dnd = json.loads(responseDnd5eApi.text)
  spells = ""
  for item in json_data_dnd['results']:
    spells += item['name'] + ", "

  login = requests.post("https://pastebin.com/api/api_login.php", data=constants.login_data)
  constants.paste_data['api_user_key'] = login.text
  constants.paste_data['api_paste_code'] = spells
  constants.paste_data['api_paste_name'] = 'Spells Level ' + level
  
  r = requests.post("https://pastebin.com/api/api_post.php", data=constants.paste_data)
  return r.text

def get_spells_with_name(name):
  responseDnd5eApi = requests.get("https://www.dnd5eapi.co/api/spells?name=" + name)
  json_data_dnd = json.loads(responseDnd5eApi.text)
  spells = ""
  for item in json_data_dnd['results']:
    spells += item['name'] + ": " + item['index'] + "\n"

  if(json_data_dnd['count'] > 50):
    login = requests.post("https://pastebin.com/api/api_login.php", data=constants.login_data)
    constants.paste_data['api_user_key'] = login.text
    constants.paste_data['api_paste_code'] = spells
    constants.paste_data['api_paste_name'] = 'Spell name ' + name
    
    r = requests.post("https://pastebin.com/api/api_post.php", data=constants.paste_data)
    return r.text
  else:
    return spells

def get_specific_spell(spell):
  responseDnd5eApi = requests.get("https://www.dnd5eapi.co/api/spells/" + spell)
  json_data_dnd = json.loads(responseDnd5eApi.text)
  spell = json_data_dnd['name'] + ": "+ "\n" + json_data_dnd['desc'][0] + "\n" + "Casting time: " + json_data_dnd['casting_time'] + "\n" + "Level: " + str(json_data_dnd['level']) + "\n" + "Duration: " + json_data_dnd['duration'] + "\n" + "Concentration: " + str(json_data_dnd['concentration'])

  return spell    

##
## Feats
##                        

def get_specific_feat(feat):
  responseDnd5eApi = requests.get("https://www.dnd5eapi.co/api/features/" + feat)
  json_data_dnd = json.loads(responseDnd5eApi.text)
  featDesc = ""
  for ftDsc in json_data_dnd['desc']:
    featDesc += ftDsc + "\n"
    
  feat = json_data_dnd['name'] + ": " + featDesc

  return feat


def get_all_feats():
  responseDnd5eApi = requests.get("https://www.dnd5eapi.co/api/features/")
  json_data_dnd = json.loads(responseDnd5eApi.text)
  spells = ""
  for item in json_data_dnd['results']:
    spells += item['name'] + ", "

  login = requests.post("https://pastebin.com/api/api_login.php", data=constants.login_data)
  constants.paste_data['api_user_key'] = login.text
  constants.paste_data['api_paste_code'] = spells
  constants.paste_data['api_paste_name'] = 'Features'
  
  r = requests.post("https://pastebin.com/api/api_post.php", data=constants.paste_data)
  return r.text

def get_feats_with_name(name):
  responseDnd5eApi = requests.get("https://www.dnd5eapi.co/api/features?name=" + name)
  json_data_dnd = json.loads(responseDnd5eApi.text)
  feats = ""
  for item in json_data_dnd['results']:
    feats += item['name'] + ": " + item['index'] + "\n"

  if(json_data_dnd['count'] > 50):
    login = requests.post("https://pastebin.com/api/api_login.php", data=constants.login_data)
    constants.paste_data['api_user_key'] = login.text
    constants.paste_data['api_paste_code'] = feats
    constants.paste_data['api_paste_name'] = 'Feats that match ' + name
    
    r = requests.post("https://pastebin.com/api/api_post.php", data=constants.paste_data)
    return r.text
  else:
    return feats

##
## Condition
##               

def get_specific_condition(condition):
  responseDnd5eApi = requests.get("https://www.dnd5eapi.co/api/conditions/" + condition)
  json_data_dnd = json.loads(responseDnd5eApi.text)
  conditionsDesc = ""
  for desc in json_data_dnd['desc']:
    conditionsDesc +=  desc + "\n"
  cond = json_data_dnd['name'] + ": " + conditionsDesc

  return cond

def get_all_condition():
  responseDnd5eApi = requests.get("https://www.dnd5eapi.co/api/conditions/")
  json_data_dnd = json.loads(responseDnd5eApi.text)
  condition = ""
  for item in json_data_dnd['results']:
    condition += item['name'] + ", "

  return condition


def get_mameds():
  return "MAMEDS!"

