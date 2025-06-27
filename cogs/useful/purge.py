import discord, os, json, asyncio
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def purge(self, ctx, amount: int = 10):
        await ctx.message.delete()
        message_ = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Attempting to Delete {amount} Messages.\n\n-# Created by @ s.eths・v{data['version']}")
        deleted = 0
        async for message in ctx.channel.history(limit = 100):
            if message.author.id == self.bot.user.id and message.id != message_.id:
                await message.delete()
                deleted += 1
            if deleted >= amount:
                break
        await message_.edit(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Successfully Deleted {amount} Messages.\n\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(purge(bot))