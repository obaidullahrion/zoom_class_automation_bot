def ping(update, context):
    import time
    start_time = int(round(time.time() * 1000))
    print("user ping done")
    end_time = int(round(time.time() * 1000))
    update.message.reply_text(f'I am alive with {end_time - start_time} ms')