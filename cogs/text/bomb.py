import discord, os, requests, json, asyncio
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class bomb(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}bomb":
                string = "# 💣 -------------------------------- 🔥"
                message = await message.reply(string)
                for i in range(32):
                    await asyncio.sleep(0.877771)
                    string = string.replace("-", "", 1)
                    await message.edit(string)
                await asyncio.sleep(0.877771)
                await message.edit("# 💣🔥")
                await asyncio.sleep(0.877771)
                await message.edit("https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}bomb` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def bomb(self, ctx):
        string = "# 💣 -------------------------------- 🔥"
        await ctx.message.delete()
        message = await ctx.send(string)
        for i in range(32):
            await asyncio.sleep(0.877771)
            string = string.replace("-", "", 1)
            await message.edit(string)
        await asyncio.sleep(0.877771)
        await message.edit("# 💣🔥")
        await asyncio.sleep(0.877771)
        await message.edit("https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831")

async def setup(bot):
    await bot.add_cog(bomb(bot))