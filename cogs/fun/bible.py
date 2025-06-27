import discord, os, json, asyncio, requests, random
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

books = {
    "Genesis": 50,
    "Exodus": 40,
    "Psalms": 150,
    "Proverbs": 31,
    "Matthew": 28,
    "Mark": 16,
    "Luke": 24,
    "John": 21,
    "Acts": 28,
    "Romans": 16,
    "1 Corinthians": 16,
    "2 Corinthians": 13,
    "Galatians": 6,
    "Ephesians": 6,
    "Philippians": 4,
    "Colossians": 4,
    "1 Thessalonians": 5,
    "2 Thessalonians": 3,
    "1 Timothy": 6,
    "2 Timothy": 4,
    "Titus": 3,
    "Philemon": 1,
    "Hebrews": 13,
    "James": 5,
    "1 Peter": 5,
    "2 Peter": 3,
    "1 John": 5,
    "2 John": 1,
    "3 John": 1,
    "Jude": 1,
    "Revelation": 22
}

def get_random_bible_verse():
    while True:
        book = random.choice(list(books.keys()))
        chapter = random.randint(1, books[book])
        verse = random.randint(1, 30)

        try:
            response = requests.get(f"https://bible-api.com/{book.replace(' ', '%20')}%20{chapter}:{verse}")
            if response.status_code == 200:
                data = response.json()
                return f"📖 {data['reference']} — {data['text'].strip()}"
        except:
            pass
        
        time.sleep(0.2)

class bible(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content == f"{data['prefix']}bible":
                await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> {get_random_bible_verse()}\n\n-# Created by @ s.eths・v{data['version']}")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}bible` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def bible(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> {get_random_bible_verse()}\n\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(bible(bot))