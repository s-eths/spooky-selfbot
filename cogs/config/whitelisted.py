import discord, os, json, asyncio
from discord.ext import commands
from data.print import *

with open("./data/config.json", "r") as file:
    data = json.load(file)

class whitelisted(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def whitelisted(self, ctx):
        if not data["whitelisted"]:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** No users are currently **Whitelisted**.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        whitelisted_users = []
        for user_id in data["whitelisted"]:
            whitelisted_users.append(f"- <@{user_id}> (`{user_id}`)")
        whitelisted_users_string = "\n".join(whitelisted_users)
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Whitelisted Users:\n\n{whitelisted_users_string}\n\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(whitelisted(bot))