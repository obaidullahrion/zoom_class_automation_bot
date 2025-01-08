import time
import json
import pyttsx3
import logging
import keyboard
import telegram
from core import *
from datetime import datetime
from selenium import webdriver
from command_modules.set import *
from command_modules.quick import *
from command_modules.help import *
from command_modules.start import *
from command_modules.config import *
from command_modules.sptest import *
from command_modules.screenshot import *
from command_modules.botping import ping
from command_modules.botlogs import botlogs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from telegram.ext import CommandHandler, Updater, contexttypes
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains



logging.basicConfig(filename="logs.log",format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)



currentTime = int(time.strftime('%H'))   


with open('database/bot_token.json') as t:
    token = json.load(t)


bot = telegram.Bot(token=token["BOT_TOKEN"]) 

updater = Updater(token = token["BOT_TOKEN"] , use_context= True)
dispatcher = updater.dispatcher



with open('database/data.json') as f:
    data = json.load(f) 


if currentTime == data["c1_time"]:
    pyttsx3.speak('Joining class 1! Starting at ' + currentTime + ' \'o clock!')
    mid = data["c1_time"]
    mpass = data["c1_time"]
    zoom()



botcmds = [
    ('/help', 'Get help details...'),
    ('/config',  'display current bot configuration.'),
    ('/set', 'set/change config values. syntax: /set <name> <value>.'),
    ('/log', 'get the log.txt and configure file.'),
    ('/screenshot', 'take a screenshot of the current screen of host.'),
    ('/speedtest', 'display internet speed of host.'),
    ('/quick', 'isntantly join a meeting . syntax: /quick <mid> <mpass> <name>')
    ]

bot.set_my_commands(botcmds)
    

dispatcher.add_handler(CommandHandler("start" , start))
dispatcher.add_handler(CommandHandler("help" , help))
dispatcher.add_handler(CommandHandler("set" , set))
dispatcher.add_handler(CommandHandler("config" , config))
dispatcher.add_handler(CommandHandler("help" , help))
dispatcher.add_handler(CommandHandler("screenshot" , sendss))
dispatcher.add_handler(CommandHandler("speedtest" , sptest))
dispatcher.add_handler(CommandHandler("log" , botlogs))
dispatcher.add_handler(CommandHandler("ping" , ping))
dispatcher.add_handler(CommandHandler("log" , botlogs))
dispatcher.add_handler(CommandHandler("quick" , quick))





updater.start_polling()
updater.idle()