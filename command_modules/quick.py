from core import *
def quick(update , context):
    import telegram.ext 
    args1 = context.args[0] #mid
    args2 = context.args[1] #pass
    args3 = context.args[2] #uname
    
    update.message.reply_text("Hold on sir, joining now...")
    quick_join(args1 , args2 , args3)