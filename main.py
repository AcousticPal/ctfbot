import discord
import json

client = discord.Client()
config = json.load(open('config.json'))


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return


client.run(config["token"])
