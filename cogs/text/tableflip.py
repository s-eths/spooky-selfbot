import discord, os, json, asyncio
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class tableflip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}tableflip":
                await message.reply("(╯°□°)╯︵ ┻━┻")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}tableflip` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def tableflip(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"(╯°□°)╯︵ ┻━┻")

async def setup(bot):
    await bot.add_cog(tableflip(bot))