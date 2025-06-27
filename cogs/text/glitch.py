import discord, os, json, asyncio, random
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class glitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content.startswith(f"{data['prefix']}glitch"):
                content = message.content[len(f"{data['prefix']}glitch"):].strip()
                if not content:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Missing **argument(s)**.\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                zalgo_up = "̍̎̄̅̿̑̐͒͗͛̋̓"
                zalgo_down = "̖̗̘̙̜̝̞̟̠̤̥̦̩̪̫̬̮̯̰"
                zalgo_mid = "̡̢̧̨̛̀̕͘"
                glitched_text = ""
                for i in content:
                    glitched_text += i
                    glitched_text += "".join(random.choice(zalgo_up + zalgo_down + zalgo_mid) for _ in range(random.randint(2, 5)))
                await message.reply(glitched_text)
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}glitch {content}` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def glitch(self, ctx, *, args = None):
        if not args:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Missing **argument(s)**.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        zalgo_up = "̍̎̄̅̿̑̐͒͗͛̋̓"
        zalgo_down = "̖̗̘̙̜̝̞̟̠̤̥̦̩̪̫̬̮̯̰"
        zalgo_mid = "̡̢̧̨̛̀̕͘"
        glitched_text = ""
        for i in args:
            glitched_text += i
            glitched_text += "".join(random.choice(zalgo_up + zalgo_down + zalgo_mid) for _ in range(random.randint(2, 5)))
        await ctx.message.delete()
        await ctx.send(glitched_text)

async def setup(bot):
    await bot.add_cog(glitch(bot))