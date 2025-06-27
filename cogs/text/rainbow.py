import discord, os, json, asyncio
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

colors = ["\u001b[31m", "\u001b[33m", "\u001b[32m", "\u001b[36m", "\u001b[34m", "\u001b[35m"]

class rainbow(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content.startswith(f"{data['prefix']}rainbow"):
                content = message.content[len(f"{data['prefix']}rainbow"):].strip()
                if not content:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Missing **argument(s)**.\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                rainbow_message = ""
                for i, char in enumerate(content):
                    rainbow_message += colors[i % len(colors)] + char
                await message.reply(f"```ansi\n{rainbow_message}```")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}rainbow {content}` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def rainbow(self, ctx, *, args = None):
        if not args:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Missing **argument(s)**.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        rainbow_message = ""
        for i, char in enumerate(args):
            rainbow_message += colors[i % len(colors)] + char
        await ctx.message.delete()
        await ctx.send(f"```ansi\n{rainbow_message}```")

async def setup(bot):
    await bot.add_cog(rainbow(bot))