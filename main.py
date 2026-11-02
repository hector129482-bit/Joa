import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True  # activar también "Message Content Intent" en el portal de desarrolladores

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Conectado como {bot.user} (id {bot.user.id})")


async def main():
    async with bot:
        await bot.load_extension("cogs.setup_servidor")
        await bot.start(os.environ["DISCORD_TOKEN"])


if __name__ == "__main__":
    asyncio.run(main())
