import discord, os, json, asyncio, requests, time
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class deletegroup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def deletegroup(self, ctx):
        if not isinstance(ctx.channel, discord.GroupChannel):
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Command can only be ran inside of a **Groupchat**.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Attempting to Delete the Groupchat.\n\n-# Created by @ s.eths・v{data['version']}")
        start_time = time.time()
        while True:
            channel = await self.bot.fetch_channel(ctx.channel.id)
            recipients = channel.recipients
            if len(recipients) <= 1:
                break
            if time.time() - start_time > 60:
                break
            for user in recipients:
                if self.bot.user.id != user.id:
                    requests.delete(f"https://discord.com/api/v9/channels/{ctx.channel.id}/recipients/{user.id}", headers = {"Authorization": data["tokens"]["token"], "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        await ctx.channel.leave()


async def setup(bot):
    await bot.add_cog(deletegroup(bot))