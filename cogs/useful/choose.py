import discord, os, json, asyncio, random
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class choose(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content.startswith(f"{data['prefix']}choose"):
                content = message.content[len(f"{data['prefix']}choose"):].strip().split()
                if len(content) < 2:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Atleast 2 **arguments** are Required.\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> 🎲 Chosen: **{random.choice(content)}**\n\n-# Created by @ s.eths・v{data['version']}")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}choose {content}` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def choose(self, ctx, *args):
        if len(args) < 2:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Atleast 2 **arguments** are Required.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> 🎲 Chosen: **{random.choice(args)}**\n\n-# Created by @ s.eths・v{data['version']}")
        
async def setup(bot):
    await bot.add_cog(choose(bot))