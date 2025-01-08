import json

def config(update , context):

    with open('database/data.json') as f:
        data = json.load(f) 
        
   
    update.message.reply_text(f"""___name_____value___

    my_name = {data["my_name"]}
    c1_time = {data["c1_time"]}
    c1_id = {data["c1_id"]}
    c1_pass = {data["c1_pass"]}
    """)