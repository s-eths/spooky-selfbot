import discord, os, json, asyncio, requests
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class dog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}dog":
                await message.reply(requests.get("https://dog.ceo/api/breeds/image/random").json()["message"])
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}dog` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def dog(self, ctx):
        await ctx.message.delete()
        await ctx.send(requests.get("https://dog.ceo/api/breeds/image/random").json()["message"])

async def setup(bot):
    await bot.add_cog(dog(bot))