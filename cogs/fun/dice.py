import discord, os, json, asyncio, random
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}dice":
                await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** You rolled {random.randint(1, 6)} 🎲\n\n-# Created by @ s.eths・v{data['version']}")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}dice` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def dice(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** You rolled {random.randint(1, 6)} 🎲\n\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(dice(bot))