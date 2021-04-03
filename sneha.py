import discord
import os
import io
import aiohttp
import asyncio
from random import shuffle
from discord.ext import commands
from discord.ext.commands import Bot

bot = Bot("!")

from discord.ext.commands import has_permissions, CheckFailure


intents = discord.Intents.all()
client = discord.Client(intents=intents)

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

async def change_nicknames():
  while True:
    members = list(client.get_all_members())
    members = [member for member in members if member.name == 'mungeable' or member.name == 'Dank Memer']
    names = [member.name for member in members if member.name == 'mungeable' or member.name == 'Dank Memer']
    names.append('shrek')
    shuffle(names)
    print(names)
    
    for i, member in enumerate(members):
      try:
        await member.edit(nick=names[i])
      except discord.Forbidden:
        print("stupid u are forbidden")
        continue
    await asyncio.sleep(10)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    bot.loop.create_task(change_nicknames())


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if any(word in message.content for word in sad_words):
      await message.channel.send("OOOH spicy")
    
    if 'subway' in message.content:
      await message.channel.send("STOP EATING SUBWAY YOU LOSER")

    if 'react' in message.content:
      emoji = '\N{THUMBS UP SIGN}'
      await message.add_reaction(emoji)

    if 'shrek' in message.content:
      my_url = 'https://am22.mediaite.com/tms/cnt/uploads/2021/02/shrek.jpg'
      async with aiohttp.ClientSession() as session:
          async with session.get(my_url) as resp:
              if resp.status != 200:
                  return await message.channel.send('Could not download file...')
              data = io.BytesIO(await resp.read())
              await message.channel.send(file=discord.File(data, 'cool_image.png'))
    
    if 'scramble' in message.content:
      whatever = 0


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

async def leaderboard(ctx, x=10):
  
  users = ['suha', 'jerome']
  leaderboard = {}
  total=[]
  
  for user in list(users[str(ctx.guild.id)]):
    print(ctx.guild.id)
    name = int(user)
    total_amt = users[str(ctx.guild.id)][str(user)]['experience']
    leaderboard[total_amt] = name
    total.append(total_amt)
    

  total = sorted(total,reverse=True)
  

  em = discord.Embed(
    title = f'Top {x} highest leveled members in {ctx.guild.name}',
    description = 'The highest leveled people in this server'
  )
  
  index = 1
  for amt in total:
    id_ = leaderboard[amt]
    member = client.get_user(id_)
    
    
    em.add_field(name = f'{index}: {member}', value = f'{amt}', inline=False)




#bot.run(os.getenv('TOKEN'))
client.run(os.getenv('TOKEN'))

