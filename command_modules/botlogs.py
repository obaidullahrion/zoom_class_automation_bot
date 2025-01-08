def botlogs(update , context):
    import telegram
    import json
    with open('database/bot_token.json') as t:
        token = json.load(t)
    bot = telegram.Bot(token=token["BOT_TOKEN"])
    bot.send_document(chat_id=update.message.chat_id, document=open('logs.log', 'r'))