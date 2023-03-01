import discord
from read_config import TOKEN
from discord.ext import commands
from ScrapePaperData import trending_url_list, latest_url_list, greatest_url_list

intents = discord.Intents.all()
client = discord.Client(command_prefix='-', intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.content.startswith('-trends'):
        header_message = 'Here is the Trending Papers:'
        await message.channel.send(header_message)
        for link in trending_url_list:
            await message.channel.send(link)

    elif message.content.startswith('-latest'):
        header_message = 'Here is the Latest Papers:'
        await message.channel.send(header_message)
        for link in latest_url_list:
            await message.channel.send(link)

    elif message.content.startswith('-greatest'):
        header_message = 'Here is the Greatest Papers:'
        await message.channel.send(header_message)
        for link in greatest_url_list:
            await message.channel.send(link)

# send_trending_papers
client.run(TOKEN)