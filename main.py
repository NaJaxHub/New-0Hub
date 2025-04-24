import discord
import os

from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.slash_command(name="ping", description="เช็คบอท")
async def ping(ctx):
    await ctx.respond("🏓 Pong!")

bot.run(os.getenv("DISCORD_TOKEN"))
