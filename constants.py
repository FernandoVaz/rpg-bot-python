import os

pastebin_acc = 'MFBloo'
my_pastebin = os.environ['pastebin']
my_pastebin_pass = os.environ['pastebin_pass']
github_secret = os.environ['discord_token']

login_data = {
      'api_dev_key': my_pastebin,
      'api_user_name': pastebin_acc,
      'api_user_password': my_pastebin_pass
    }

paste_data = {
    'api_option': 'paste',
    'api_dev_key': my_pastebin,
    'api_paste_code':'text',
    'api_paste_private': '0',
    'api_paste_name':'t_title',
    'api_paste_expire_date': '10M',
    'api_user_key': None,
    'api_paste_format': 'php'
  }