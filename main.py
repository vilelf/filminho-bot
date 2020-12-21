import os

import discord
from dotenv import load_dotenv

from commands import help_command, save_movie, list_movies

load_dotenv()
client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ola'):
        await message.channel.send(f'Ola {message.author.mention}')

    if message.content.startswith('!help'):
        await help_command(message.channel)
    
    if message.content.startswith('!salva-filme'):
        _, *movie = message.content.split(' ')
        movie = ' '.join(movie)
        await save_movie(message.channel, message.author, movie)

    if message.content.startswith('!lista-filme'):
        await list_movies(message.channel)


client.run(os.environ['DISCORD_TOKEN'])
