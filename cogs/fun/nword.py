import discord, os, json, asyncio
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class nword(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        with open ("./data/config.json", "r") as file:
            data = json.load(file)
        
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}nword":
                await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** {self.bot.user.mention} has said the N-Word **{data['nword_counter']}** Times.\n\n-# Created by @ s.eths・v{data['version']}")
                await message.channel.send("https://media.discordapp.net/attachments/990748872986988604/1169732095686492322/1698911116407211.gif?ex=6855c1e8&is=68547068&hm=97b72bbc0018337c2c0df9aecc29269b6f7f8a8f7ad812c0aa8f4233235c6fbd&")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}nword` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def nword(self, ctx):
        with open ("./data/config.json", "r") as file:
            data = json.load(file)
        
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** {self.bot.user.mention} has said the N-Word **{data['nword_counter']}** Times.\n\n-# Created by @ s.eths・v{data['version']}")
        await ctx.send("https://media.discordapp.net/attachments/990748872986988604/1169732095686492322/1698911116407211.gif?ex=6855c1e8&is=68547068&hm=97b72bbc0018337c2c0df9aecc29269b6f7f8a8f7ad812c0aa8f4233235c6fbd&")

async def setup(bot):
    await bot.add_cog(nword(bot))