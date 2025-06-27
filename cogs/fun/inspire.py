import discord, os, json, asyncio, requests
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class inspire(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}inspire":
                data_ = requests.get("https://zenquotes.io/api/random").json()[0]
                await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** {data_['q']} - {data_['a']}\n\n-# Created by @ s.eths・v{data['version']}")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}inspire` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def inspire(self, ctx):
        data_ = requests.get("https://zenquotes.io/api/random").json()[0]
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** {data_['q']} - {data_['a']}\n\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(inspire(bot))