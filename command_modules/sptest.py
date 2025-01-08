

def sptest(update , context):
    import speedtest
    import telegram
    import json

    update.message.reply_text("Running okla speedtest...")

    st = speedtest.Speedtest()
    
    st.get_best_server()

    st.download()

    st.upload()

    st.results.share()

    result = st.results.dict()

    up_res = result["upload"]/1000000

    down_res = result["download"]/1000000

    ping_res = result["ping"]

    server_name_res = result["server"]["name"]

    server_country_res = result["server"]["country"]

    isp_res = result["client"]["isp"]

    clint_ip_res = result["client"]["ip"]

    isp_rating_res = result["client"]["isprating"]

    isp_country_res = result["client"]["country"]

    img_res = result["share"]



    with open('database/bot_token.json') as t:
        token = json.load(t)
    bot = telegram.Bot(token=token["BOT_TOKEN"])
    bot.send_photo(chat_id=update.message.chat_id, photo=img_res)


    update.message.reply_text(f""" _______________Result______________
    Download: {down_res:.2f} Mb/s 
    upload: {up_res:.2f} Mb/s 
    ping: {ping_res} ms
    
    speedtest-server:{server_name_res} , {server_country_res}
   
    clint:
    ip addr: {clint_ip_res}
    isp: {isp_res} , {isp_country_res}
    isp rating: {isp_rating_res}""")
  



