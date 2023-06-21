import os

from dotenv import load_dotenv
load_dotenv()

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", "15939361")) #API ID from https://my.telegram.org/auth
API_HASH = os.environ.get("API_HASH", "f8beb0bd0054a717d84fbe9be12a23ea") #API Hash from https://my.telegram.org/auth
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5931484630:AAFDph-1OJ6z4wba9Fa7WFkIpFEY22LKkg0") # Bot token from @BotFather
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS", "5543917190").split(",")] if os.environ.get("ADMINS", "5543917190") else []

DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://amrobots:amrobots@cluster0.e3hn16i.mongodb.net/?retryWrites=true&w=majority") # mongodb uri from https://www.mongodb.com/
OWNER_ID =  int(os.environ.get("OWNER_ID", "5543917190")) # id of the owner
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []

#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001527701055")) # log channel for information about users
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", False) # For Force Subscription
BROADCAST_AS_COPY = is_enabled((os.environ.get('BROADCAST_AS_COPY', "True")), False) # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://telegra.ph/file/03691465baa774e46506d.mp4') # image when someone hit /start
LINK_BYPASS = "True" 


