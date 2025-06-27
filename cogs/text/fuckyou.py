import discord, os, json, asyncio
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class fuckyou(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}fuckyou":
                arg = "uck you!"
                string = "### f"
                message = await message.reply(string)
                for i in list(arg):
                    await asyncio.sleep(0.877771)
                    string = string + i
                    await message.edit(f"{string}")
                await message.edit("### FUCK YOU!")
                await message.edit("## FUCK YOU!")
                await message.edit("# FUCK YOU!")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}fuckyou` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def fuckyou(self, ctx):
        arg = "uck you!"
        string = "### f"
        await ctx.message.delete()
        message = await ctx.send(string)
        for i in list(arg):
            await asyncio.sleep(0.877771)
            string = string + i
            await message.edit(f"{string}")
        await message.edit("### FUCK YOU!")
        await message.edit("## FUCK YOU!")
        await message.edit("# FUCK YOU!")

async def setup(bot):
    await bot.add_cog(fuckyou(bot))