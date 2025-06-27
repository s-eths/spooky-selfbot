import discord, os, json, asyncio, requests
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}meme":
                await message.reply(requests.get("https://meme-api.com/gimme/memes").json()["url"])
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}meme` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def meme(self, ctx):
        await ctx.message.delete()
        await ctx.send(requests.get("https://meme-api.com/gimme/memes").json()["url"])

async def setup(bot):
    await bot.add_cog(meme(bot))