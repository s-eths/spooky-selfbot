import discord, os, json, asyncio, random, string
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class fakenitro(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}fakenitro":
                await message.reply(f"https://discord.gift/{''.join(random.choices(string.ascii_letters + string.digits, k=24))}")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}fakenitro` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def fakenitro(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"https://discord.gift/{''.join(random.choices(string.ascii_letters + string.digits, k=24))}")

async def setup(bot):
    await bot.add_cog(fakenitro(bot))