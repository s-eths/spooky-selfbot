import discord, os, requests, json
from discord.ext import commands
from data.print import *

with open("./data/config.json", "r") as file:
    data = json.load(file)

class breakingbad_quote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}breakingbad quote":
                request = requests.get("https://api.breakingbadquotes.xyz/v1/quotes").json()[0]
                await message.reply(f"**```ansi\n[2;41mSpooky - Discord Self-Bot v1.1[0m```\n**```ansi\n[2;31m[2;34m<> {request['author']}: {request['quote']}.[2;31m[0m```\n**```ansi\n[2;45m[2;35m[2;37m[1;37mCreated by @s.eths[0m[2;37m[2;45m[0m[2;35m[2;45m[0m[2;45m[0m```**")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}breakingbad quote` has been successfully ran by {message.author}"))

    @commands.group()
    async def breakingbad(self, ctx):
        return
    
    @breakingbad.command()
    async def quote(self, ctx):
        await ctx.message.delete()
        request = requests.get("https://api.breakingbadquotes.xyz/v1/quotes").json()[0]
        await ctx.send(f"**```ansi\n[2;41mSpooky - Discord Self-Bot v1.1[0m```\n**```ansi\n[2;31m[2;34m<> {request['author']}: {request['quote']}.[2;31m[0m```\n**```ansi\n[2;45m[2;35m[2;37m[1;37mCreated by @s.eths[0m[2;37m[2;45m[0m[2;35m[2;45m[0m[2;45m[0m```**")
        os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}breakingbad quote` has been successfully ran by {ctx.message.author}"))

async def setup(bot):
    await bot.add_cog(breakingbad_quote(bot))