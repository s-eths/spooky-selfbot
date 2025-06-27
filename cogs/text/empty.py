import discord, os, json, asyncio
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class empty(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}empty":
                await message.reply("‎")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}empty` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def empty(self, ctx):
        await ctx.message.delete()
        await ctx.send("‎")

async def setup(bot):
    await bot.add_cog(empty(bot))