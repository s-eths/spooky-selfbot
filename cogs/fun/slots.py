import discord, os, json, asyncio, random
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

payouts = {
    "🍒🍒🍒": 10,
    "🍋🍋🍋": 20,
    "🍊🍊🍊": 30,
    "🍉🍉🍉": 40,
    "🍇🍇🍇": 50,
    "🍓🍓🍓": 60,
    "⭐⭐⭐": 100,
    "🍒🍒": 5,
    "🍋🍋": 5,
    "🍊🍊": 5,
    "🍉🍉": 5,
    "🍇🍇": 5,
    "🍓🍓": 5,
    "⭐⭐": 10
}

class slots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}slots":
                symbols = ["🍒", "🍋", "🍊", "🍉", "🍇", "🍓", "⭐"]
                results = [random.choice(symbols) for i in range(3)]
                payout = 0
                for combo, amount in payouts.items():
                    if combo in "".join(results):
                        payout = max(payout, amount)
                message_ = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> {' | '.join([random.choice(symbols) for i in range(3)])}\n\n-# Created by @ s.eths・v{data['version']}")
                for i in range(4):
                    await asyncio.sleep(0.877771)
                    await message_.edit(f"**spooky.wtf - Discord Self-Bot**\n\n> {' | '.join([random.choice(symbols) for i in range(3)])}\n\n-# Created by @ s.eths・v{data['version']}")
                if payout > 0:
                    await message_.edit(f"**spooky.wtf - Discord Self-Bot**\n\n> {' | '.join(results)}\n\nCongrats you won {payout} coins 🪙\n\n-# Created by @ s.eths・v{data['version']}")
                else:
                    await message_.edit(f"**spooky.wtf - Discord Self-Bot**\n\n> {' | '.join(results)}\n\nNo Matches, you lost 😢\n\n-# Created by @ s.eths・v{data['version']}")

    
    @commands.command()
    async def slots(self, ctx):
        await ctx.message.delete()
        symbols = ["🍒", "🍋", "🍊", "🍉", "🍇", "🍓", "⭐"]
        results = [random.choice(symbols) for i in range(3)]
        payout = 0
        for combo, amount in payouts.items():
            if combo in "".join(results):
                payout = max(payout, amount)
        message = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> {' | '.join([random.choice(symbols) for i in range(3)])}\n\n-# Created by @ s.eths・v{data['version']}")
        for i in range(4):
            await asyncio.sleep(0.877771)
            await message.edit(f"**spooky.wtf - Discord Self-Bot**\n\n> {' | '.join([random.choice(symbols) for i in range(3)])}\n\n-# Created by @ s.eths・v{data['version']}")
        if payout > 0:
            await message.edit(f"**spooky.wtf - Discord Self-Bot**\n\n> {' | '.join(results)}\n\nCongrats you won {payout} coins 🪙\n\n-# Created by @ s.eths・v{data['version']}")
        else:
            await message.edit(f"**spooky.wtf - Discord Self-Bot**\n\n> {' | '.join(results)}\n\nNo Matches, you lost 😢\n\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(slots(bot))