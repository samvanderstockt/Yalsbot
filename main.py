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

mod_roles = {"trial mod", "head devs"}


def normalize_role_name(name):
    return "".join(character for character in name.casefold() if character.isalnum())


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

    if "Yals" in message.content.lower():
        await message.channel.send(f"https://yals.netlify.app")

    if "Yalsify" in message.content.lower():
        await message.channel.send(f)

    if "neger" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, - Geen racistisch taalgebruik in deze server. ")

    if "nigger" in message.content.lower():
      await message.delete()
      await message.channel.send(f"{message.author.mention}, - Geen racistisch taalgebruik in deze server. ")

    if "kankerhomo" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, - Niet schelden met ziektes in deze server.")

    if "kankerneger" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, - Niet schelden met ziektes en geen racistisch taalgebruik in deze server.")

    if "chihuahua" in message.content.lower():
        await message.channel.send(f"{message.author.mention}, - Ik Chihuahua Jij Chihuahua Wij chihuahua.")

    if "chatgpt" in message.content.lower():
        await message.channel.send(f"{message.author.mention}, - Ben je een boomer ofzo chatgpt was nieuw in 2020.")

    if "sam" in message.content.lower():
        await message.channel.send(f"{message.author.mention}, - Sam is afwezig as hij niet binnen de 5 minuten reageert")

    if "yalsify" in message.content.lower():
        await message.channel.send(f"{message.author.mention}, - Yalsify is super nice.")

    if "victorini" in message.content.lower():
        await message.channel.send(f"{message.author.mention}, - Victorini is wss pita met look aan het eten")

    if "thomas" in message.content.lower():
        await message.channel.send(f"{message.author.mention}, - Thomas is wss MineCraft aan het grinden")

    if "appelmoes" in message.content.lower():
        await message.channel.send(f"{message.author.mention}, - APPELMOES??? I LOVE APPELMOES.")

    if "kanker" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, - Niet schelden met ziektes in deze server.")


   
    


    await bot.process_commands(message)



@bot.command()
async def bark(ctx):
    await ctx.send(f"Arf Arf {ctx.author.mention}!")

@bot.command()
async def cap(ctx):
    await ctx.send(f"Cap cap capperdecap")

@bot.command()
async def warn(ctx, member: discord.Member):
    allowed_roles = {normalize_role_name(name) for name in mod_roles}
    if any(normalize_role_name(role.name) in allowed_roles for role in ctx.author.roles):
        await ctx.send(f"{member.mention} has been warned by {ctx.author.mention}.")
    else:
        await ctx.send(f"{ctx.author.mention}, you do not have permission to warn members.")





bot.run(token, log_handler=handler, log_level=logging.DEBUG)