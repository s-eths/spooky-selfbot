import discord, os, json, asyncio
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class bite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content.startswith(f"{data['prefix']}bite"):
                if not message.mentions:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** **discord.User** is Missing, Incomplete or Incorrect.\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                user = message.mentions[0]
                await message.reply(f"{user.mention} you were bitten by {message.author.mention}.\nhttps://tenor.com/view/spongebob-wacky-bite-got-me-gif-16950691")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}bite @{user.name}` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def bite(self, ctx, user: discord.User = None):
        if not user:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** **discord.User** is Missing, Incomplete or Incorrect.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        await ctx.message.delete()
        await ctx.send(f"{user.mention} you were bitten by {ctx.author.mention}.\nhttps://tenor.com/view/spongebob-wacky-bite-got-me-gif-16950691")

async def setup(bot):
    await bot.add_cog(bite(bot))