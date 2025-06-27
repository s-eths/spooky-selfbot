import discord, os, json, asyncio
from discord.ext import commands
from gtts import gTTS
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class tts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content.startswith(f"{data['prefix']}tts"):
                content = message.content[len(f"{data['prefix']}tts"):].strip()
                if not content:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Missing **argument(s)**.\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                try:
                    gTTS(text = content, lang = "en").save("./data/temp/tts.mp3")
                    await message.reply(file = discord.File("./data/temp/tts.mp3", filename = "tts.mp3"))
                    os.remove("./data/temp/tts.mp3")
                except Exception as error:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** ERROR Generating TTS: `{str(error)}`\n\n-# Created by @ s.eths・v{data['version']}")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}tts {content}` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def tts(self, ctx, *, args = None):
        if not args:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Missing **argument(s)**.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        try:
            gTTS(text = args, lang = "en").save("./data/temp/tts.mp3")
            await ctx.message.delete()
            await ctx.send(file = discord.File("./data/temp/tts.mp3", filename = "tts.mp3"))
            os.remove("./data/temp/tts.mp3")
        except Exception as error:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** ERROR Generating TTS: `{str(error)}`\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}tts {content}` has been successfully ran by {message.author}"))

async def setup(bot):
    await bot.add_cog(tts(bot))