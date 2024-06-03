import discord
import requests
import json
from discord.ext import commands

# GET IP
PORT = 727
IP = requests.get('https://icanhazip.com').text.rstrip() + f':{PORT}'

# OPEN IP FILE (or create)
file = open('ip_last.txt', 'a+')
file.seek(0)

# EXIT IF
if (file.read() == IP):
    file.close()
    exit()

# SAVE NEW IP
file.truncate(0)
file.write(IP)
file.close()

# BOT
cfg = json.load(open('ipbot_cfg.json'))
TOKEN = cfg['TOKEN']
CHANNEL_ID = cfg['CHANNEL_ID']
MC_VERSION = cfg['MC_VERSION']

intents = discord.Intents.default()
intents.message_content = False
client = commands.Bot(intents = intents, command_prefix = '!')

@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)
    await channel.purge(limit=3)
    await channel.send(f'Wersja Minecraft: `{MC_VERSION}`\nAdres: `{IP}`')
    await client.close()

client.run(TOKEN)
