import discord
import os

intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")

bot.run(os.getenv("DISCORD_TOKEN"))
