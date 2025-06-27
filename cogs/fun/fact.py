import discord, os, json, asyncio, requests
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class fact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}fact":
                await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** {requests.get('https://uselessfacts.jsph.pl/random.json?language=en').json()['text']}\n\n-# Created by @ s.eths・v{data['version']}")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}fact` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def fact(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** {requests.get('https://uselessfacts.jsph.pl/random.json?language=en').json()['text']}\n\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(fact(bot))