# bot.py
import os
import discord
import random
import yaml

client = discord.Client()

file = open("intake.yml")
parsed_file = yaml.load(file, Loader=yaml.FullLoader)
header = parsed_file["APP"]
s = header["SECRET"]

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name="Heck Ochem")
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    gek_quotes = [
        'On Jah? Just like that?',
        'I am Gekyume'
    ]

    if message.content == '!gek':
        response = random.choice(gek_quotes)
        await message.channel.send(response)

    if message.content == '!jah':
        await message.channel.send("Enough")

    if message.content == '!gek face reveal':
        await message.channel.send("https://tenor.com/view/punch-dwarf-gif-5261161")

client.run(s)