import time
import random
import discord

import os
from dotenv import load_dotenv
load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_CHANNEL = os.getenv('DISCORD_CHANNEL')
INFURA_TOKEN = os.getenv('WEB3_INFURA_PROJECT_ID')

from web3.auto.infura import w3

GWEI_THRESHOLD = 200     # under this threshold, the bot send a msg
MSG_COOLDOWN = 10        # wait 1 hour if the sent a msg
ETH_TX_REFRESH_RATE = 15 # time between 2 ethereum Tx



client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    channel = client.get_channel(int(DISCORD_CHANNEL))

    while(True):
        gwei = w3.eth.gasPrice / 10**9

        if(gwei < GWEI_THRESHOLD):
            msg = "Gwei is worth " + str(gwei)
            await channel.send(msg)
            time.sleep(MSG_COOLDOWN)
        else:
            time.sleep(ETH_TX_REFRESH_RATE)

client.run(DISCORD_TOKEN)