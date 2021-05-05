import discord
from discord.ext import commands

import json
import os

with open('cnf.json') as f:
	json_file = json.load(f)

client = commands.Bot(
    command_prefix=json_file['prefix'],
    intents = discord.Intents.default()
)

@client.event
async def on_ready():
    print('-----------------')
    print('Github: https://github.com/Rapi-Dev/discordpy-template')
    print('Made with <3 by the team of RapiDev!')
    print('-----------------')
    print(f'I have logged into {client.user} and the bot is running!')
    print('-----------------')
    
for filename in os.listdir("./cogs"):
  if filename.endswith(".py") and filename != "__init.py__":
    client.load_extension(f"cogs.{filename[:-3]}")
    print(f"Loaded cogs.{filename[:-3]}")

client.run(json_file['token'])
