import discord, os, json, asyncio, requests
from discord.ext import commands
from PIL import Image, ImageDraw
from io import BytesIO
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class wanted(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content.startswith(f"{data['prefix']}wanted"):
                user = None
                if not message.mentions:
                    user = message.author
                else:
                    user = message.mentions[0]
                avatar_image = Image.open(BytesIO(requests.get(user.avatar.with_size(512).url).content)).convert("RGBA")
                poster = Image.open("./data/images/wanted.png").convert("RGBA")
                avatar_image = avatar_image.resize((472, 441))
                poster.paste(avatar_image, (132, 328), avatar_image)
                output_buffer = BytesIO()
                poster.save(output_buffer, format = "PNG")
                output_buffer.seek(0)
                await message.reply(file = discord.File(fp = output_buffer, filename = "wanted.png"))
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}wanted` has been successfully ran by {message.author}"))

    @commands.command()
    async def wanted(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        if not user:
            user = ctx.author
        avatar_image = Image.open(BytesIO(requests.get(user.avatar.with_size(512).url).content)).convert("RGBA")
        poster = Image.open("./data/images/wanted.png").convert("RGBA")
        avatar_image = avatar_image.resize((472, 441))
        poster.paste(avatar_image, (132, 328), avatar_image)
        output_buffer = BytesIO()
        poster.save(output_buffer, format = "PNG")
        output_buffer.seek(0)
        await ctx.send(file = discord.File(fp = output_buffer, filename = "wanted.png"))

async def setup(bot):
    await bot.add_cog(wanted(bot))