import asyncio, json
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class count(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}count":
                data["counter"] = data.get("counter", 0) + 1
                with open("./data/config.json", "w") as f:
                    json.dump(data, f, indent = 4)
                await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Added **+1** to the Counter.\n\n-# Created by @ s.eths・v{data['version']}")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}count` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def count(self, ctx):
        data["counter"] = data.get("counter", 0) + 1
        with open("./data/config.json", "w") as f:
            json.dump(data, f, indent = 4)
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Added **+1** to the Counter.\n\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(count(bot))