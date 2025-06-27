import discord, os, json, asyncio, random
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class guess(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content.startswith(f"{data['prefix']}guess"):
                content = message.content[len(f"{data['prefix']}guess"):].strip()
                if not content:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Missing **argument(s)**.\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                if not content.isdigit() or int(content) > 100:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Please Input a **Number** from 1-100.\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                selected_number = random.randint(1, 100)
                if content == selected_number:
                    await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** **Correct Number!** The Selected Number was **{selected_number}** 🎊\n\n-# Created by @ s.eths・v{data['version']}")
                else:
                    await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** **Incorrect Number**, The Selected Number was **{selected_number}** 🥲\n\n-# Created by @ s.eths・v{data['version']}")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}guess {content}` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def guess(self, ctx, *, args = None):
        if not args:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Missing **argument(s)**.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        if not args.isdigit() or int(args) > 100:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Please Input a **Number** from 1-100.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        selected_number = random.randint(1, 100)
        await ctx.message.delete()
        if args == selected_number:
            await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** **Correct Number!** The Selected Number was **{selected_number}** 🎊\n\n-# Created by @ s.eths・v{data['version']}")
        else:
            await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** **Incorrect Number**, The Selected Number was **{selected_number}** 🥲\n\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(guess(bot))