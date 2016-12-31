import os
import logging
import happylogging
from slackbot.bot import Bot
import slackbot.settings

import pyjpbot

def main():
    happylogging.initlog(syslog='/var/run/syslog', facility='syslog')   
    slackbot.settings.API_TOKEN = os.environ['PYTHONJP_SLACKBOT_KEY']

    pyjpbot.init()
    pyjpbot.create_table()
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
