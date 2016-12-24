import discord
import asyncio
import re

REGEX = "<:[a-zA-Z0-9_]{2,}:(\d+)>"

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event
async def on_message(message):
    message_text = message.content
    pattern = re.compile(REGEX)
    for image_id in re.findall(pattern,message_text):
        url="https://cdn.discordapp.com/emojis/"+image_id+".png"
        await client.send_message(message.channel, url)
        
client.run('TOKEN')