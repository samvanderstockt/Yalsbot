from email.mime import message

import discord 
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
logging.basicConfig(level=logging.INFO, handlers=[handler])
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

mod_role= "trial mod"


@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

@bot.event
async def on_member_join(member):
    await member.send("Welkom in Yalsify! Lees zeker de regels!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "neger" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, - Geen racistisch taalgebruik in deze server. ")

    if "nigger" in message.content.lower():
      await message.delete()
      await message.channel.send(f"{message.author.mention}, - Geen racistisch taalgebruik in deze server. ")

    await bot.process_commands(message)


@bot.command()
async def bark(ctx):
    await ctx.send(f"Arf Arf {ctx.author.mention}!")




bot.run(token, log_handler=handler, log_level=logging.DEBUG)