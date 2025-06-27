import discord, os, requests, json, asyncio, time
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}ping":
                start = time.perf_counter()
                message_ = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** 🏓 Pinging....\n\n-# Created by @ s.eths・v{data['version']}")
                end = time.perf_counter()
                await message_.edit(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Ping: `{int((end - start) * 1000)}ms` | Gateway: `{round(self.bot.latency * 1000)}ms`\n\n-# Created by @ s.eths・v{data['version']}")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}ping` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def ping(self, ctx):
        start = time.perf_counter()
        message = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** 🏓 Pinging....\n\n-# Created by @ s.eths・v{data['version']}")
        end = time.perf_counter()
        await message.edit(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Ping: `{int((end - start) * 1000)}ms` | Gateway: `{round(self.bot.latency * 1000)}ms`\n\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(ping(bot))