import discord, os, json, asyncio, requests
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

def format_section(name, items):
    return f"### {name}\n" + "\n".join([f"-# {item['name']}: {item['stock']}" for item in items])

class gagstock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}gagstock":
                stock_data = requests.get("https://growagardenapi.vercel.app/api/stock/GetStock").json().get("Data", {})
                sections = []
                for key in ["gear", "seeds", "egg", "honey", "cosmetics"]:
                    if key in stock_data:
                        sections.append(format_section(key.capitalize(), stock_data[key]))
                await message.reply("**spooky.wtf - Discord Self-Bot**\n\n> **[!] Grow a Garden - Current Stock**\n" + "\n".join(sections) + f"\n\n-# Created by @ s.eths・v{data['version']}")
    
    @commands.command()
    async def gagstock(self, ctx):
        stock_data = requests.get("https://growagardenapi.vercel.app/api/stock/GetStock").json().get("Data", {})
        sections = []
        for key in ["gear", "seeds", "egg", "honey", "cosmetics"]:
            if key in stock_data:
                sections.append(format_section(key.capitalize(), stock_data[key]))
        await ctx.message.delete()
        await ctx.send("**spooky.wtf - Discord Self-Bot**\n\n> **[!] Grow a Garden - Current Stock**\n" + "\n".join(sections) + f"\n\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(gagstock(bot))