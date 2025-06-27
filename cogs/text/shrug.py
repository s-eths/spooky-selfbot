import discord, os, json, asyncio
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class shrug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}shrug":
                await message.reply("¯\_(ツ)_/¯")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}shrug` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def shrug(self, ctx):
        await ctx.message.delete()
        await ctx.send("¯\_(ツ)_/¯")

async def setup(bot):
    await bot.add_cog(shrug(bot))