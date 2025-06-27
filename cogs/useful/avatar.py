import discord, os, json, asyncio
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content.startswith(f"{data['prefix']}avatar"):
                user = None
                if not message.mentions:
                    user = message.author
                else:
                    user = message.mentions[0]
                await message.reply(user.avatar)
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}avatar` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def avatar(self, ctx, user: discord.User = None):
        if not user:
            user = ctx.author
        await ctx.message.delete()
        await ctx.send(user.avatar)

async def setup(bot):
    await bot.add_cog(avatar(bot))