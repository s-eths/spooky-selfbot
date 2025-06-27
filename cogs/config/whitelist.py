import discord, os, json, asyncio
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class whitelist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def whitelist(self, ctx, user: discord.User = None):
        if not user:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** **discord.User** is Missing, Incomplete or Incorrect.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        if user.id in data["whitelisted"]:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** User is **Already Whitelisted**.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        data["whitelisted"].append(user.id)
        with open("./data/config.json", "w") as file:
            json.dump(data, file, indent = 4)
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** {user.mention} has been Successfully Whitelisted.\n\n> **[-]** Please Reset the Self-Bot to see Changes.\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(whitelist(bot))