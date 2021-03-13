import discord
from discord.ext.commands import Bot
from discord import Intents
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get("TOKEN")

intents = Intents.all()
bot = Bot(intents, command_prefix="bruh ")


@bot.event
async def on_ready():
    print("Bot has connected.")


bot.run(TOKEN)
