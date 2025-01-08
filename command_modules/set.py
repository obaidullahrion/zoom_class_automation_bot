import json
def set(update , context):

    with open('database/data.json') as f:
            data = json.load(f) 


    arg_1 = context.args[0]
    arg_2 = context.args[1]
    update.message.reply_text(f"value {arg_2} set for {arg_1}") 


    if arg_1 == "c1_time":       
        for key, value in data.items():
            data["c1_time"] = arg_2

    if arg_1 == "my_name":       
        for key, value in data.items():
            data["my_name"] = arg_2

    if arg_1 == "c1_id":       
        for key, value in data.items():
            data["c1_id"] = arg_2


    if arg_1 == "c1_pass":       
        for key, value in data.items():
            data["c1_pass"] = arg_2

    with open('database/data.json', 'w') as f:
        json.dump(data, f)
