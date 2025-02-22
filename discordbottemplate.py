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
import sqlite3
from dndlib import Character

############################### INITIALIZATION ################################################
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
bot.remove_command('help')

############################# INIT ###########################################################
#@bot.event
#async def on_connect(ctx):
#    await ctx.send('Gay')
#################

con = sqlite3.connect('dndbot.db')
#con.row_factory = sqlite3.Row

cur = con.cursor()

##################
@bot.event
async def on_ready():
    log.info('Bot logged in as `%s` (id %s)', bot.user, bot.user.id)
    log.info('Member of the following servers/guilds:')
    for guild in bot.guilds:
        log.info('  %s', guild.name)


@bot.command(name='verb', aliases=['verbs'])
async def verb(ctx, a, b):
    print(Role.name)

    c = int(a)+int(b)
    await ctx.send('{} + {} = {}'.format(a,b,c))
############################ CHARACTER ##############################
@bot.command(name='spawn', aliases=['summon','build','create'])
async def spawn(ctx, name, score_str,score_dex,score_con,score_int,score_wis,score_chr,st_str, st_dex, st_con, st_int, st_wis,st_chr,mod_str,mod_dex,mod_con,mod_int,mod_wis,mod_chr,save,atk,hp,maxhp,ac,init):
    #newcharacter = Character(name,[score],[savingthrow],[mod],save, attack, hp, maxhp)
    #sukakog = Character("sukakog",[16,16,16,16,16,16],[3,3,3,3,6,6],[3,3,3,3,3,3],15,7,48,48)
    con.execute("INSERT INTO character (name, score_str,score_dex,score_con,score_int,score_wis,score_chr,st_str, st_dex, st_con, st_int, st_wis,st_chr,mod_str,mod_dex,mod_con,mod_int,mod_wis,mod_chr,save,atk,hp,maxhp,ac,init) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (name, score_str,score_dex,score_con,score_int,score_wis,score_chr,st_str, st_dex, st_con, st_int, st_wis,st_chr,mod_str,mod_dex,mod_con,mod_int,mod_wis,mod_chr,save,atk,hp,maxhp,ac,init))
    con.commit()
    await ctx.send(name)
#ctx.author.roles??? #TODO

@bot.command(name='see', aliases=['lookat','watch','observe'])
async def see(ctx, name):
    await ctx.send(name.__string__)
############################ ACTIONS #######################################
@bot.command(name='dmg', aliases=['damage','hit','deal','-hp'])
async def verb(ctx, c, hp):

    exec(f"{c}.hp = {c}.hp-int(hp)")  #Not quite safe but OK
    print(f"{c}'s hp:",sukakog.hp)
    await ctx.send(f"Hit {hp}!\n{c}'s hp is now on **{sukakog.hp}**")

@bot.command(name='heal', aliases=['+hp'])
async def verb(ctx, c, hp):

    exec(f"{c}.hp = {c}.hp+int(hp)")  #Not quite safe but OK
    print(f"{c}'s hp:",c.hp)
    await ctx.send(f"Healed {hp}!\n{c}'s hp is now on **{c.hp}**")

############################ EDIT CHARACTER ################################

#TODO modify score


#TODO level up

############################ ROLL COMMAND ##################################
@bot.command(name="roll") 
async def roll(ctx, die):
    xdy=die.split("d")
    xd=int(xdy[0])
    dy=int(xdy[1])
    total=[]
    for i in range(xd):
        dy=random.randint(1,dy)
        total.append(dy)
        print(dy)
    await ctx.send("**Rolls:** {}\n**Sum:** {}\nROLE:{}".format(total,sum(total),ctx.author.Role))

@bot.command(name='hello', aliases=['hi','lol'])
async def add(ctx):
    await ctx.send('Hello there, {}!'.format(ctx.author.name))

#omtale af bot.guilds
    #Bot.guilds er en liste af de guilds botten er medlem af.
    #

    #bot.guilds er faktisk en attribut (fordi det er en "variabel", som er en del af en klasse/objekt)

############################### DM COMMANDS ################################




############################### HELP ######################################
@bot.command(name='help')
async def help(ctx):

    about_text = ('A DnD bot.')

    embed = discord.Embed(colour = discord.Colour.dark_magenta())
    embed.set_author(name='Help')
    embed.add_field(name='About', value=about_text, inline=False)
                          
    embed.add_field(name='`_roll 1d6`',
                    value='roll any dice',
                    inline=False)

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


    await ctx.send(embed=embed)
    await ctx.send(embed=embed)


# Run the bot
TOKEN = os.getenv('DISCORD_TOKEN')

if not TOKEN:
    log.error('`DISCORD_TOKEN` must be set in .env file')
    sys.exit()

try:
    bot.run(TOKEN)
except discord.errors.LoginFailure:
    log.error('Bot login failed, improper/invalid token')
    sys.exit()
