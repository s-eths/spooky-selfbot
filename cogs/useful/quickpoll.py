import discord, os, json, asyncio
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class quickpoll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content.startswith(f"{data['prefix']}quickpoll"):
                await message.add_reaction("⬆️"), await message.add_reaction("⬇️")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}quickpoll` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def quickpoll(self, ctx):
        await ctx.message.add_reaction("⬆️"), await ctx.message.add_reaction("⬇️")

async def setup(bot):
    await bot.add_cog(quickpoll(bot))