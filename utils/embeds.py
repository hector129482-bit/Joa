import discord


def embed_error(descripcion, titulo="❌ Error"):
    """Embed rojo para mensajes de error."""
    return discord.Embed(title=titulo, description=descripcion, color=discord.Color.red())
