from keep_alive import keep_alive
import os
import discord

TOKEN = os.environ["DISCORD_TOKEN"]

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Bot conectado como {client.user}")

keep_alive()
client.run(TOKEN)
