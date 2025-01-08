def help(update , context):
    update.message.reply_text(f"""/help to get this message.
    /config  display current bot configuration.
    /set set/change config values. syntax: /set <name> <value>.
    /log get the log.txt and configure file.
    /screenshot take a screenshot of the current screen of host.
    /speedtest display internet speed of host.
    /quick isntantly join a meeting . syntax: /quick <mid> <mpass> <name>
    """)