import discord, os, json, asyncio, base64
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class trolltoken(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content.startswith(f"{data['prefix']}trolltoken"):
                if not message.mentions:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** **discord.User** is Missing, Incomplete or Incorrect.\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                user = message.mentions[0].id
                token = base64.b64encode(str(user).encode("utf-8")).decode("utf-8")
                await message.reply(f"`{token}.{'*' * 26}`")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}trolltoken @{user.name}` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def trolltoken(self, ctx, user: discord.User = None):
        if not user:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** **discord.User** is Missing, Incomplete or Incorrect.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        token = base64.b64encode(str(user.id).encode("utf-8")).decode("utf-8")
        await ctx.message.delete()
        await ctx.send(f"`{token}.{'*' * 26}`")

async def setup(bot):
    await bot.add_cog(trolltoken(bot))