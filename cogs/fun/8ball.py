import discord, os, json, asyncio, random
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

responses = [
    "Yes.",
    "No.",
    "Maybe.",
    "Definitely.",
    "Absolutely not.",
    "I don't know.",
    "Ask again later.",
    "It is certain.",
    "Very doubtful.",
    "Without a doubt.",
    "Better not tell you now.",
    "My reply is no.",
    "Signs point to yes.",
    "Concentrate and ask again.",
    "Outlook not so good."
]

class _8ball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"] or message.author.id == self.bot.user.id:
            if message.content.startswith(f"{data['prefix']}8ball"):
                content = message.content[len(f"{data['prefix']}8ball"):].strip()
                if not content:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Missing **argument(s)**.\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> `Question:`  {content}\n> `Response:`  {random.choice(responses)}.\n\n-# Created by @ s.eths・v{data['version']}")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}8ball {content}` has been successfully ran by {message.author}"))

async def setup(bot):
    await bot.add_cog(_8ball(bot))