import discord, os, json, asyncio
from discord.ext import commands
from googletrans import Translator
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.translator = Translator()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content.startswith(f"{data['prefix']}translate"):
                args = message.content.split()
                if len(args) < 2:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Please Input a **Language**.\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                if len(args) < 3:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Please Input a **Message**.\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                translation = self.translator.translate(" ".join(args[2:]), dest = args[1])
                await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Translated ({translation.src} → {translation.dest}): **{translation.text}**\n\n-# Created by @ s.eths・v{data['version']}")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}translate` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def translate(self, ctx, language: str = None, *, text: str = None):
        if not language:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Please Input a **Language**.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        if not text:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Please Input a **Message** to Translate.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        await ctx.message.delete()
        translation = self.translator.translate(text, dest = language)
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Translated ({translation.src} → {translation.dest}): **{translation.text}**\n\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(translate(bot))