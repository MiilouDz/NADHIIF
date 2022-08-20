# NADHIIF
Telegram bot for protect your groups from inappropriate content/users

## Pre-Requirements
 
- Install latest python from  python.org 
- add python to path, when installing [windows os]


### config 

Before working with Telegram’s API, you need to get your own API ID and hash:
Login to your account on my.telegram.org with the phone number of the developer account to use.
Click under API Development tools. A Create new application window will appear. Fill in your application details. There is no need to enter any URL, and only the first two fields (App title and Short name) can currently be changed later.
Click on Create application at the end. Remember that your API hash is secret and Telegram won’t let you revoke it. Don’t post it anywhere!


API_ID : Your Telegram account api_id. Get from my.telegram.org 
API_HASH : Your telegram account api_hash. Get from my.telegram.org 
BOT_TOKEN: Your bot toke from @Botfather on telegram
GROUP_ID: Your group id. Where your bot will be added as admin.
 
Add @Miss_rosebot to your group and type /id to get the id. 
BAN_ACCOUNT_WITHOUT_PROFILE_PIC: If its sets to 'True' it will ban account if it doesn't have profile PIC. Default to False
pic_purify_api_key: Your pic purify api key. Get from https://www.picpurify.com/



### How to run this bot 

- fill your details properly on config.py 
- add bot as admin on your group
- then run run.bat file [windows only]




### for linux 


- pip install -r requirements.txt
- python3 main.py 

### Deploy the bot in Heroku or other service 

- create github account and push the code 
- create Heroku account 
  - Create new app
  - Connect with github repo 
  - Then deploy
  - Come to resources tab and enable python main.py
  - Open the heroku logs
  - Congrats


##  :orange_heart: 
