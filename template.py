## THIS DOES NOTHING, THIS IS A TEMPLATE FOR CUSTOM COMMANDS!!!

import discord, os, json, asyncio
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class INSERT_NAME_HERE(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}INSERT_NAME_HERE":
                await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** INSERT_ERROR_HERE\n\n-# Created by @ s.eths・v{data['version']}")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}INSERT_NAME_HERE` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def INSERT_NAME_HERE(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** INSERT_COMMAND_HERE\n\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(INSERT_NAME_HERE(bot))