import discord, os, json, asyncio, tempfile, easyocr, cv2, numpy, sys, contextlib
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

@contextlib.contextmanager
def suppress_stdout():
    with open(os.devnull, 'w') as devnull:
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = devnull
        sys.stderr = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr

class ocr(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with suppress_stdout():
            self.reader = easyocr.Reader(['en'])
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content.startswith(f"{data['prefix']}ocr"):
                if not message.attachments:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Missing a **Image** File.\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                image = message.attachments[0]

                if not (image.filename.endswith('.png') or image.filename.endswith('.jpg')):
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Please Upload a Image with Either **PNG or JPG**.\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return

                try:
                    _, extension = os.path.splitext(image.filename)
                    with tempfile.NamedTemporaryFile(suffix = extension, delete = False) as temp_file:
                        temp_path = temp_file.name
                        try:
                            image_bytes = await image.read()
                            temp_file.write(image_bytes)
                            temp_file.flush()
                            image_ = cv2.imread(temp_path)
                            results = self.reader.readtext(image_)
                            if results:
                                await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Output: {' '.join([text[1] for text in results])}\n\n-# Created by @ s.eths・v{data['version']}")
                            else:
                                error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Sadly, **No Text** was Detected in the Image.\n\n-# Created by @ s.eths・v{data['version']}")
                                await asyncio.sleep(3)
                                await error.delete()
                                return
                        except Exception as error:
                            error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** **{str(error)}**\n\n-# Created by @ s.eths・v{data['version']}")
                            await asyncio.sleep(3)
                            await error.delete()
                            return
                        finally:
                            try:
                                os.unlink(temp_path)
                            except Exception:
                                pass
                except Exception as e:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** **{str(error)}**\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return

    @commands.command()
    async def ocr(self, ctx):
        if not ctx.message.attachments:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Missing a **Image** File.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        image = ctx.message.attachments[0]

        if not (image.filename.endswith('.png') or image.filename.endswith('.jpg')):
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Please Upload a Image with Either **PNG or JPG**.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        
        try:
            _, extension = os.path.splitext(image.filename)
            with tempfile.NamedTemporaryFile(suffix = extension, delete = False) as temp_file:
                temp_path = temp_file.name
                try:
                    image_bytes = await image.read()
                    temp_file.write(image_bytes)
                    temp_file.flush()
                    image_ = cv2.imread(temp_path)
                    results = self.reader.readtext(image_)
                    if results:
                        await ctx.message.delete()
                        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Output: {' '.join([text[1] for text in results])}\n\n-# Created by @ s.eths・v{data['version']}")
                    else:
                        await ctx.message.delete()
                        error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Sadly, **No Text** was Detected in the Image.\n\n-# Created by @ s.eths・v{data['version']}")
                        await asyncio.sleep(3)
                        await error.delete()
                        return
                except Exception as error:
                    await ctx.message.delete()
                    error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** **{str(error)}**\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                finally:
                    try:
                        os.unlink(temp_path)
                    except Exception:
                        pass
        except Exception as e:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** **{str(error)}**\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return

async def setup(bot):
    await bot.add_cog(ocr(bot))
