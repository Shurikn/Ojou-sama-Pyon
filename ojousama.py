import discord
import asyncio
import re

REGEX = "<:[a-zA-Z0-9_]{2,}:(\d+)>"
ANIMATED_REGEX="<a:[a-zA-Z0-9_]{2,}:(\d+)>"

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
    i=0
    already_posted_emoji=[]
    for image_id in re.findall(pattern,message_text):
        if image_id not in already_posted_emoji:
            already_posted_emoji.append(image_id)
            url = "https://cdn.discordapp.com/emojis/" + image_id + ".png"
            embed=discord.Embed()
            embed.set_image(url=url)
            await message.channel.send(embed=embed)
            i+=1
            if i >= 3:
                break
    pattern = re.compile(ANIMATED_REGEX)
    i = 0
    already_posted_emoji = []
    for image_id in re.findall(pattern, message_text):
        if image_id not in already_posted_emoji:
            already_posted_emoji.append(image_id)
            url = "https://cdn.discordapp.com/emojis/" + image_id + ".gif"
            embed = discord.Embed()
            embed.set_image(url=url)
            await message.channel.send(embed=embed)
            i += 1
            if i >= 3:
                break
client.run('TOKEN')