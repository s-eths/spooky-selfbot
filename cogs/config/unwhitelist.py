import discord, os, json, asyncio
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class unwhitelist(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def unwhitelist(self, ctx, user: discord.User = None):
        if not user:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** **discord.User** is Missing, Incomplete or Incorrect.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        if user.id not in data["whitelisted"]:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** User is **Not Whitelisted**.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        data["whitelisted"].remove(user.id)
        with open("./data/config.json", "w") as file:
            json.dump(data, file, indent=4)
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** {user.mention} has been Successfully Unwhitelisted.\n\n> **[-]** Please Reset the Self-Bot to see Changes.\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(unwhitelist(bot))