import discord, os, json, asyncio, base64
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class decodeb64(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content.startswith(f"{data['prefix']}decodeb64"):
                content = message.content[len(f"{data['prefix']}decodeb64"):].strip()
                if not content:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Missing **argument(s)**.\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                try:
                    decoded_bytes = base64.b64decode(content)
                    decoded_text = decoded_bytes.decode("utf-8")
                    await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** 🔓 Decoded: `{decoded_text}`.\n\n-# Created by @ s.eths・v{data['version']}")
                except Exception as error:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** ERROR: {str(error)}\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}decodeb64 {content}` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def decodeb64(self, ctx, *, args = None):
        if not args:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Missing **argument(s)**.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        try:
            decoded_bytes = base64.b64decode(args)
            decoded_text = decoded_bytes.decode("utf-8")
            await ctx.message.delete()
            await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** 🔓 Decoded: `{decoded_text}`.\n\n-# Created by @ s.eths・v{data['version']}")
        except Exception as error:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** ERROR: {str(error)}\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return

async def setup(bot):
    await bot.add_cog(decodeb64(bot))