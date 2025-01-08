
import time

currentTime = int(time.strftime('%H'))  

if currentTime < 12 :
     greet = "Morning"
if currentTime > 12 :
     greet = "Good Afternoon"
if currentTime > 6 :
     greet = " Good Evening"


def start(update , context):
    update.message.reply_text(f"""{greet} boss!
Just setup the easy config to make me ready. view /help""")

    