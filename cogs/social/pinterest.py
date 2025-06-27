import discord, os, requests, json, asyncio
from discord.ext import commands
from data.print import *
from bs4 import BeautifulSoup

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class pinterest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content.startswith(f"{data['prefix']}pinterest"):
                split_message = message.content.split()
                if len(split_message) <= 2:
                    if not "pinterest" in split_message[1]:
                        error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** **Invalid Link**, Please Provide a Pinterest Link.\n\n-# Created by @ s.eths・v{data['version']}")
                        await asyncio.sleep(3)
                        await error.delete()
                        return
                    try:
                        response = requests.get(split_message[1], headers = {"User-Agent": "Mozilla/5.0"})
                        soup = BeautifulSoup(response.text, "html.parser")
                        og_image = soup.find("meta", property="og:image")
                        if og_image and og_image.get("content"):
                            image_url = og_image["content"]
                            await message.reply(image_url)
                            os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}pinterest {split_message[1]}` has been successfully ran by {message.author}"))
                        else:
                            error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Couldn't find a **Image or GIF**\n\n-# Created by @ s.eths・v{data['version']}")
                            await asyncio.sleep(3)
                            await error.delete()
                            return
                    except Exception as error:
                        error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** **{str(error)}**\n\n-# Created by @ s.eths・v{data['version']}")
                        await asyncio.sleep(3)
                        await error.delete()
                        return

    @commands.command()
    async def pinterest(self, ctx, link: str):
        if not "pinterest" in link:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** **Invalid Link**, Please Provide a Pinterest Link.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        try:
            response = requests.get(link, headers = {"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(response.text, "html.parser")
            og_image = soup.find("meta", property="og:image")
            if og_image and og_image.get("content"):
                image_url = og_image["content"]
                await ctx.message.delete()
                await ctx.send(image_url)
            else:
                await ctx.message.delete()
                error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** Couldn't find a **Image or GIF**\n\n-# Created by @ s.eths・v{data['version']}")
                await asyncio.sleep(3)
                await error.delete()
                return
        except Exception as error:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** **{str(error)}**\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return

async def setup(bot):
    await bot.add_cog(pinterest(bot))