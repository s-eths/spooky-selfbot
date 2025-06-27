import discord, os, json, asyncio
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class robloxtags(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content.startswith(f"{data['prefix']}robloxtags"):
                content = message.content[len(f"{data['prefix']}robloxtags"):].strip()
                if not content:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Missing **argument(s)**.\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                string = ""
                for i in list(content):
                    if i.isspace():
                        string = string + " "
                    else:
                        string = string + "#"
                await message.reply(string)
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}robloxtags {content}` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def robloxtags(self, ctx, *, args = None):
        if not args:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Missing **argument(s)**.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        string = ""
        for i in list(args):
            if i.isspace():
                string = string + " "
            else:
                string = string + "#"
        await ctx.message.delete()
        await ctx.send(string)

async def setup(bot):
    await bot.add_cog(robloxtags(bot))