import discord, os, json, asyncio
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class counter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        with open ("./data/config.json", "r") as file:
            data = json.load(file)
        
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}counter":
                await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Current Counter Value: **{data['counter']}**\n\n-# Created by @ s.eths・v{data['version']}")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}counter` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def counter(self, ctx):
        with open ("./data/config.json", "r") as file:
            data = json.load(file)
        
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Current Counter Value: **{data['counter']}**\n\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(counter(bot))