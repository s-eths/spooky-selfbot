import discord, os, json, asyncio, datetime
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

afk_stats = {
    "afk_status": False,
    "afk_start_time": None
}

def format_time(delta):
    total_seconds = int(delta.total_seconds())
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    parts = []
    if days:
        parts.append(f"{days}d")
    if hours:
        parts.append(f"{hours}h")
    if minutes:
        parts.append(f"{minutes}m")
    if seconds or not parts:
        parts.append(f"{seconds}s")

    return " ".join(parts)

class afk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.bot.user.id and afk_stats["afk_status"]:
            if message.content != ",afk" and not message.content.startswith("**spooky.wtf - Discord Self-Bot**"):
                afk_stats["afk_status"] = False
                await message.channel.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** {self.bot.user.mention} is no longer **AFK**, You were AFK for **{format_time(datetime.datetime.utcnow() - afk_stats['afk_start_time'])}**.\n\n-# Created by @ s.eths・v{data['version']}")
        
        if self.bot.user.mentioned_in(message) and afk_stats["afk_status"] and message.author.id != self.bot.user.id:
            afk_message = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** {self.bot.user.mention} has been **AFK** for **{format_time(datetime.datetime.utcnow() - afk_stats['afk_start_time'])}**.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(5)
            await afk_message.delete()
    
    @commands.command()
    async def afk(self, ctx):
        afk_stats["afk_status"] = True
        afk_stats["afk_start_time"] = datetime.datetime.utcnow()
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** You're Status is set to **AFK**.\n\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(afk(bot))