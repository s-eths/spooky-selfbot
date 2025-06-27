import discord, os, json, asyncio
from discord.ext import commands
from moviepy.editor import VideoFileClip
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class makemp3(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}makemp3":
                if not message.attachments:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Please Upload a **MP4 File**.\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                attachment = message.attachments[0]
                if not attachment.filename.endswith(".mp4"):
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Please Upload a **MP4 File**.\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                mp4_path = f"./data/temp/{attachment.filename}"
                mp3_path = mp4_path.replace(".mp4", ".mp3")
                await attachment.save(mp4_path)
                try:
                    video = VideoFileClip(mp4_path)
                    video.audio.write_audiofile(mp3_path, logger = None)
                    video.close()
                    await message.reply(file = discord.File(mp3_path, filename = os.path.basename(mp3_path)))
                except:
                    pass
                finally:
                    if os.path.exists(mp4_path):
                        os.remove(mp4_path)
                    if os.path.exists(mp3_path):
                        os.remove(mp3_path)
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}makemp3` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def makemp3(self, ctx):
        if not ctx.message.attachments:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Please Upload a **MP4 File**.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        attachment = ctx.message.attachments[0]
        if not attachment.filename.endswith(".mp4"):
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Please Upload a **MP4 File**.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        mp4_path = f"./data/temp/{attachment.filename}"
        mp3_path = mp4_path.replace(".mp4", ".mp3")
        await attachment.save(mp4_path)
        try:
            video = VideoFileClip(mp4_path)
            video.audio.write_audiofile(mp3_path, logger = None)
            video.close()
            await ctx.message.delete()
            await ctx.send(file = discord.File(mp3_path, filename = os.path.basename(mp3_path)))
        except:
            pass
        finally:
            if os.path.exists(mp4_path):
                os.remove(mp4_path)
            if os.path.exists(mp3_path):
                os.remove(mp3_path)

async def setup(bot):
    await bot.add_cog(makemp3(bot))