import discord, os, json, asyncio, requests
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class yomama(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}yomama":
                await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** {requests.get('https://www.yomama-jokes.com/api/v1/jokes/random/').json()['joke']}\n\n-# Created by @ s.eths・v{data['version']}")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}jimmysmother` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def yomama(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** {requests.get('https://www.yomama-jokes.com/api/v1/jokes/random/').json()['joke']}\n\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(yomama(bot))