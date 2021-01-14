#! /usr/bin/python


from datetime import datetime
import json
import logging
import os
import sys

import discord
from discord.ext import commands
import dotenv
import aiohttp
import random



# Load .evn variables 
dotenv.load_dotenv()

# Logging
LOG_LVL = os.getenv('LOG_LVL')
log = logging.getLogger(__name__)
if not LOG_LVL:
    LOG_LVL = 'DEBUG'

h = logging.StreamHandler(sys.stdout)
h.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
log.addHandler(h)
log.setLevel(LOG_LVL)


# The bot   
bot = commands.Bot(command_prefix='_')
print("bot type:", type(bot))
bot.remove_command('help')

#@bot.event
#async def on_connect(ctx):
#    await ctx.send('Gay')

@bot.event
async def on_ready():
    log.info('Bot logged in as `%s` (id %s)', bot.user, bot.user.id)
    log.info('Member of the following servers/guilds:')
    for guild in bot.guilds:
        log.info('  %s', guild.name)


@bot.command(name='add', aliases=['sum'])
async def add(ctx, a, b):
            
    c = int(a)+int(b)
    await ctx.send('{} + {} = {}'.format(a,b,c))

@bot.command(name="roll") ############################ROLL COMMAND##################################
async def roll(ctx, die):
    xdy=die.split("d")
    xd=int(xdy[0])
    xy=int(xdy[1])
    total=[]
    for i in range(xd):
        dy=random.randint(1,xy)
        total.append(dy)
        print(dy)
    await ctx.send("{}\n**Sum:** {}".format(total,sum(total)))

@bot.command(name='hello', aliases=['hi','lol'])
async def add(ctx):
    await ctx.send('Hello there, {}!'.format(ctx.author.name))

#omtale af bot.guilds
    #Bot.guilds er en liste af de guilds botten er medlem af.
    #

    #bot.guilds er faktisk en attribut (fordi det er en "variabel", som er en del af en klasse/objekt)


@bot.command(name='help')
async def help(ctx):

    about_text = ('A random bot.')

    embed = discord.Embed(colour = discord.Colour.dark_magenta())
    embed.set_author(name='Help')
    embed.add_field(name='About', value=about_text, inline=False)
                          
    #embed.add_field(name='`!add a b| !sum a b`',
    #                value='Calculate a+b',
    #                inline=False)
#
    #embed.add_field(name='`!hello | !hi`',
    #                value='Have the bot greet you',
    #                inline=False)
#
    #embed.add_field(name='`!meme',
    #                value='Have the bot generate a meme in the channel',
    #                inline=False)
#
    #embed.add_field(name='`!mememe @user amount',
    #                value='Have the bot send a certain amount of memes to a user',
    #                inline=False)

    embed.add_field(name='`!mememe amount subreddit',
                    value="i don't want to help you lmao",
                    inline=False)

    await ctx.send(embed=embed)
    await ctx.send(embed=embed)


@bot.command(pass_context=True) 
async def meme(ctx): 
    embed = discord.Embed(title="", description="")
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=top') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def memeuser(ctx, user: discord.User,amount):
    r = int(amount)
    for i in range(r):
        embed = discord.Embed(title="", description="")
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=top') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await user.send("hello{}".format(ctx.author.name),embed=embed,delete_after=30)

@bot.command(pass_context=True, name="mememe",aliases=["Mememe"])
async def mememe(ctx, amount=None, subreddit=None):#,user: discord.User
    print("Amount type:",type(amount))
    print("Subreddit type:",type(subreddit))
    print("async def type:",type(mememe))
    if amount != None:
        try:
            amount=int(amount)
        except ValueError or TypeError:
            print("Amount conversion failed")

    if subreddit !=None:
        try:
            subreddit=int(subreddit)
        except ValueError or TypeError:
            print("Subreddit conversion failed")

    if type(amount) == int and subreddit==None:
        r = amount
        subreddit = "dankmemes"
        print("Input: !mememe amount")
    elif type(amount) == int and type(subreddit)==str:
        r = amount
        subreddit = subreddit
        print("Input: !mememe amount subreddit")
    elif amount == None and subreddit == None:
        r = 1
        subreddit = "dankmemes"
        print("Input: !mememe")
    elif type(amount) == str and type(subreddit) == int:
        r = subreddit
        subreddit = amount
        print("Input: !mememe subreddit amount")
    elif type(amount) == str and subreddit==None:
        subreddit = amount
        r = 1
        print("Input: !mememe subreddit")

    print("Amount of memes generated:",r,
        "Subreddit:", subreddit)

    print("ctx:",type(ctx))
    
    for i in range(r):
        embed = discord.Embed(title="", description="")
        print("title:",type(embed))
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://www.reddit.com/r/{subreddit}/new.json?sort=top') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.author.send(embed=embed,delete_after=30)
                print("aiohttp type:", type(cs))

print("async2 def type:",type(mememe))
    #message = message or "This Message is sent via DM"
    #await user.send(content=message, delete_after=10)
    

# Run the bot
TOKEN = os.getenv('DISCORD_TOKEN')
print("token type:",type(TOKEN))

if not TOKEN:
    log.error('`DISCORD_TOKEN` must be set in .env file')
    sys.exit()

try:
    bot.run(TOKEN)
except discord.errors.LoginFailure:
    log.error('Bot login failed, improper/invalid token')
    sys.exit()
