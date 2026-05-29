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

    api_url = (
        f"http://np2.npcloud.online:2007/visits?uid={uid}&region={region}"
    )

    try:

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
            inline=True
        )

        embed.add_field(
            name="UID",
            value=data.get("uid", uid),
            inline=True
        )

        embed.add_field(
            name="Level",
            value=data.get("level", "N/A"),
            inline=True
        )

        embed.add_field(
            name="Likes",
            value=str(data.get("likes", "0")),
            inline=True
        )

        embed.add_field(
            name="Success",
            value=str(data.get("success", "0")),
            inline=True
        )

        embed.add_field(
            name="Fail",
            value=str(data.get("fail", "0")),
            inline=True
        )



        # Attach GIF
        file = discord.File(
            "assets/standard (8).gif",
            filename="standard.gif"
        )

        # Set GIF inside embed
        embed.set_image(
            url="attachment://standard.gif"
        )

        # User avatar as thumbnail
        embed.set_thumbnail(
            url=ctx.author.avatar.url
            if ctx.author.avatar
            else ctx.author.default_avatar.url
        )

        embed.set_footer(
            text="DEVELOPED BY DIBOXE LEGIT •"
        )

        await ctx.send(
            f"{ctx.author.mention}",
            embed=embed,
            file=file
        )

    except Exception as e:
        print(e)
        await ctx.send(
            f"{ctx.author.mention} ❌ Failed to fetch visit data."
        )


bot.run(TOKEN)
