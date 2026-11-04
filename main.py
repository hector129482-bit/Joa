import asyncio
import os
import sys

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


def _leer_token():
    """Lee DISCORD_TOKEN y limpia errores típicos al pegarlo (espacios, comillas, 'Bot ')."""
    token = os.environ.get("DISCORD_TOKEN", "").strip().strip('"').strip("'").strip()
    if token.lower().startswith("bot "):
        token = token[4:].strip()
    if token.startswith("DISCORD_TOKEN="):
        token = token.split("=", 1)[1].strip()
    return token


async def main():
    token = _leer_token()
    if not token:
        sys.exit("❌ Falta la variable DISCORD_TOKEN (en Railway: servicio → Variables).")

    async with bot:
        await bot.load_extension("cogs.setup_servidor")
        try:
            await bot.start(token)
        except discord.LoginFailure:
            sys.exit(
                "❌ Discord rechazó el token (401). Entra a discord.com/developers/applications → "
                "tu aplicación → Bot → Reset Token, copia el token nuevo y pégalo en la variable "
                "DISCORD_TOKEN, sin comillas ni espacios."
            )


if __name__ == "__main__":
    asyncio.run(main())
