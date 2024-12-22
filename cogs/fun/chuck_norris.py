import discord, os, requests, json
from discord.ext import commands
from data.print import *

with open("./data/config.json", "r") as file:
    data = json.load(file)

class chuck_norris(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}chuck norris":
                request = requests.get("https://api.chucknorris.io/jokes/random").json()
                await message.reply(f"**```ansi\n[2;41mSpooky - Discord Self-Bot v1.1[0m```\n**```ansi\n[2;31m[2;34m<>  {request['value']}[2;31m[0m```\n**```ansi\n[2;45m[2;35m[2;37m[1;37mCreated by @s.eths[0m[2;37m[2;45m[0m[2;35m[2;45m[0m[2;45m[0m```**")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}chuck norris` has been successfully ran by {message.author}"))
    
    @commands.group()
    async def chuck(self, ctx):
        return
    
    @chuck.command()
    async def norris(self, ctx):
        await ctx.message.delete()
        request = requests.get("https://api.chucknorris.io/jokes/random").json()
        await ctx.send(f"**```ansi\n[2;41mSpooky - Discord Self-Bot v1.1[0m```\n**```ansi\n[2;31m[2;34m<>  {request['value']}[2;31m[0m```\n**```ansi\n[2;45m[2;35m[2;37m[1;37mCreated by @s.eths[0m[2;37m[2;45m[0m[2;35m[2;45m[0m[2;45m[0m```**")
        os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}chuck norris` has been successfully ran by {ctx.message.author}"))

async def setup(bot):
    await bot.add_cog(chuck_norris(bot))