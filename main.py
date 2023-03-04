
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()

bot = discord.Bot(intents = intents) # creates the bot object

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

## # # # # # # # # # #
#                    #
#   SLASH COMMANDS   #
#                    #
## # # # # # # # # # #

@bot.slash_command(name="testcommand", description="Use this at your own risk as this bot is extremely unstable and may install malware at random.")
async def testcommand(ctx):
    await ctx.respond("Hello there good sir! Your PC has been successfully hacked. Please allow up to 48 hours for best results.")

@bot.event # Run on message
async def on_message(message):
    print(message.content)
    if "General Kenobi!" in message.content:
        await message.channel.send("Hello there")

@commands.is_owner() # Owner commands
@bot.slash_command(name="send", description="Make the bot send a message")
async def send(ctx, message: int):
    await ctx.send_response("Message sent!", ephemeral=True)
    return await ctx.send(message)

@bot.event # Tell users they don't have perms
async def on_application_command_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.send_response("You don't have the permissions to use this command!", ephemeral=True)
    else:
        raise error

"""
END OF CODE WTF DONT STOP WRITING CODE DOWN HERE NO STOPPPPP
"""
bot.run(DISCORD_TOKEN)