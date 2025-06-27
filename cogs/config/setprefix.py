import discord, os, json
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class setprefix(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def setprefix(self, ctx, prefix):
        data["prefix"] = prefix

        with open("./data/config.json", "w") as file:
            json.dump(data, file, indent=4)

        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Successfully set prefix to `{prefix}`\n\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(setprefix(bot))