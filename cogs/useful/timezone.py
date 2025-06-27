import discord, os, json, asyncio, dateparser, pytz
from discord.ext import commands
from datetime import datetime
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class timezone(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content.startswith(f"{data['prefix']}timezone"):
                split_message = message.content.split()
                if len(split_message) >= 2:
                    timezone = split_message[1]
                else:
                    timezone = "UTC"

                try:
                    parsed_time = dateparser.parse("now", settings = {"TIMEZONE": timezone, "RETURN_AS_TIMEZONE_AWARE": True})
                except pytz.exceptions.UnknownTimeZoneError:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** **{timezone}** is not a Correct Timezone.\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Current Time in **{timezone}** is **{parsed_time.strftime('%H:%M:%S')}.**\n\n-# Created by @ s.eths・v{data['version']}")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}timezone` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def timezone(self, ctx, timezone: str = "UTC"):
        try:
            parsed_time = dateparser.parse("now", settings = {"TIMEZONE": timezone, "RETURN_AS_TIMEZONE_AWARE": True})
        except pytz.exceptions.UnknownTimeZoneError:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** **{timezone}** is not a Correct Timezone.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Current Time in **{timezone}** is **{parsed_time.strftime('%H:%M:%S')}.**\n\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(timezone(bot))