import discord
from discord.ext import commands
import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():

    print(f"Logged in as {bot.user}")

@bot.command(name="visits")
async def visits(ctx, uid: str, region: str):

    api_url =f"http://np2.npcloud.online:2053/visits?uid={uid}&region={region}"

    async with aiohttp.ClientSession() as session:

        async with session.get(api_url) as response:

            data = await response.json()

    embed = discord.Embed(
        title="Visit Statistics",
        color=0x2F3136
    )

    embed.add_field(
        name="Nickname",
        value=data.get("nickname", "N/A"),
        inline=False
    )

    embed.add_field(
        name="Region",
        value=data.get("region", "N/A"),
        inline=False
    )

    embed.add_field(
        name="Player UID",
        value=uid,
        inline=False
    )

    embed.add_field(
        name="Level",
        value=data.get("level", "N/A"),
        inline=False
    )

    embed.add_field(
        name="Likes",
        value=data.get("likes", "0"),
        inline=False
    )

    embed.set_footer(
        text="DEVELOPED BY DIBOXE LEGIT"
    )

    await ctx.send(embed=embed)

bot.run(TOKEN)
