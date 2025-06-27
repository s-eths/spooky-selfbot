import discord, os, json
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(invoke_without_command = True)
    async def help(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Help - Sub Commands\n\n`{data['prefix']}help ai`\n`{data['prefix']}help config`\n`{data['prefix']}help crypto`\n`{data['prefix']}help custom`\n`{data['prefix']}help encode`\n`{data['prefix']}help exploit`\n`{data['prefix']}help fun`\n`{data['prefix']}help image`\n`{data['prefix']}help music`\n`{data['prefix']}help roleplay`\n`{data['prefix']}help social`\n`{data['prefix']}help text`\n`{data['prefix']}help trolling`\n`{data['prefix']}help useful`\n\n-# Created by @ s.eths・v{data['version']}")
    
    @help.command()
    async def ai(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Help - AI\n\n`{data['prefix']}ocr [image]`\n\n-# Created by @ s.eths・v{data['version']}")
    
    @help.command()
    async def config(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Help - Configuration\n\n> **(ALL OWNER ONLY)**\n\n`{data['prefix']}setprefix [prefix]`\n`{data['prefix']}whitelist [user]`\n`{data['prefix']}unwhitelist [user]`\n`{data['prefix']}whitelisted`\n\n-# Created by @ s.eths・v{data['version']}")

    @help.command()
    async def crypto(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Help - Crypto\n\n`{data['prefix']}crypto bitcoin/btc`\n`{data['prefix']}crypto ethereum/eth`\n`{data['prefix']}crypto solana/sol`\n`{data['prefix']}crypto dogecoin/doge`\n`{data['prefix']}crypto litecoin/ltc`\n`{data['prefix']}crypto monero/xmr`\n\n-# Created by @ s.eths・v{data['version']}")

    @help.command()
    async def custom(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Help - Custom\n\n`{data['prefix']}cca`\n`{data['prefix']}jimmysmother`\n`{data['prefix']}shadow`\n\n-# Created by @ s.eths・v{data['version']}")

    @help.command()
    async def encode(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Help - Encode\n\n`{data['prefix']}decodeb64 [base64string]`\n\n-# Created by @ s.eths・v{data['version']}")
    
    @help.command()
    async def exploit(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Help - Exploit\n\n> **(ALL OWNER ONLY)**\n\n`{data['prefix']}gcspam [user] [user2]`\n`{data['prefix']}stopgcspam`\n`{data['prefix']}ghostping [user]`\n`{data['prefix']}stopghostping`\n`{data['prefix']}spam [message]`\n`{data['prefix']}stopspam`\n\n-# Created by @ s.eths・v{data['version']}")
    
    @help.command()
    async def fun(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Help - Fun\n\n`{data['prefix']}8ball [question]`\n`{data['prefix']}advice`\n`{data['prefix']}affirmation`\n`{data['prefix']}bible`\n`{data['prefix']}bitch [user]`\n`{data['prefix']}breakingbad`\n`{data['prefix']}chucknorris`\n`{data['prefix']}coinflip`\n`{data['prefix']}compliment`\n`{data['prefix']}count`\n`{data['prefix']}counter`\n`{data['prefix']}dadjoke`\n`{data['prefix']}dice`\n`{data['prefix']}ego [user]`\n`{data['prefix']}fact`\n`{data['prefix']}fortune`\n`{data['prefix']}gay [user]`\n`{data['prefix']}guess [number]`\n`{data['prefix']}hack [user]`\n`{data['prefix']}insult [user]`\n`{data['prefix']}iq [user]`\n`{data['prefix']}joke`\n`{data['prefix']}nigger [user]`\n`{data['prefix']}nword`\n`{data['prefix']}penis [user]`\n`{data['prefix']}randomemoji`\n`{data['prefix']}randomhex`\n`{data['prefix']}simp [user]`\n`{data['prefix']}slots`\n`{data['prefix']}yomama`\n\n-# Created by @ s.eths・v{data['version']}")
    
    @help.command()
    async def image(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Help - Image\n\n`{data['prefix']}cat`\n`{data['prefix']}dog`\n`{data['prefix']}meme`\n`{data['prefix']}wanted [user]`\n\n-# Created by @ s.eths・v{data['version']}")
    
    @help.command()
    async def music(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Help - Music\n\n`{data['prefix']}makemp3 [.mp4_file]`\n\n-# Created by @ s.eths・v{data['version']}")
    
    @help.command()
    async def roleplay(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Help - Roleplay\n\n`{data['prefix']}airkiss [user]`\n`{data['prefix']}angrystare [user]`\n`{data['prefix']}bite [user]`\n`{data['prefix']}bleh [user]`\n`{data['prefix']}brofist [user]`\n`{data['prefix']}celebrate [user]`\n`{data['prefix']}cry [user]`\n`{data['prefix']}cuddle [user]`\n`{data['prefix']}fuck [user]`\n`{data['prefix']}hug [user]`\n`{data['prefix']}kiss [user]`\n`{data['prefix']}lick [user]`\n`{data['prefix']}pat [user]`\n`{data['prefix']}poke [user]`\n`{data['prefix']}punch [user]`\n`{data['prefix']}sad [user]`\n`{data['prefix']}decodeb64 [user]`\n`{data['prefix']}scared [user]`\n`{data['prefix']}shy [user]`\n`{data['prefix']}sigh [user]`\n`{data['prefix']}slap [user]`\n`{data['prefix']}stare [user]`\n`{data['prefix']}touch [user]`\n\n-# Created by @ s.eths・v{data['version']}")

    @help.command()
    async def social(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Help - Social\n\n`{data['prefix']}gagstock`\n`{data['prefix']}pinterest [pinterest_link]`\n\n-# Created by @ s.eths・v{data['version']}")
    
    @help.command()
    async def text(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Help - Text\n\n`{data['prefix']}ascii [text]`\n`{data['prefix']}bomb`\n`{data['prefix']}cock`\n`{data['prefix']}empty`\n`{data['prefix']}fliptext [text]`\n`{data['prefix']}freaky [text]`\n`{data['prefix']}fuckyou`\n`{data['prefix']}glitch [text]`\n`{data['prefix']}lennyface`\n`{data['prefix']}miniemoji [emoji]`\n`{data['prefix']}rainbow [text]`\n`{data['prefix']}reverse [text]`\n`{data['prefix']}robloxtags [text]`\n`{data['prefix']}shrug`\n`{data['prefix']}tableflip`\n`{data['prefix']}translate [text]`\n`{data['prefix']}tts [text]`\n`{data['prefix']}uwu [text]`\n`{data['prefix']}wave [text]`\n\n-# Created by @ s.eths・v{data['version']}")
    
    @help.command()
    async def trolling(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Help - Trolling\n\n`{data['prefix']}emptyping [user]`\n`{data['prefix']}fakenitro`\n`{data['prefix']}trollnitro`\n`{data['prefix']}trolltoken [user]`\n\n-# Created by @ s.eths・v{data['version']}")
    
    @help.command()
    async def useful(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Help - Useful\n\n`{data['prefix']}afk` **(OWNER ONLY)**\n`{data['prefix']}avatar [user]`\n`{data['prefix']}choose [choice] [choice2]`\n`{data['prefix']}deletegroup` **(OWNER ONLY)**\n`{data['prefix']}help`\n`{data['prefix']}password`\n`{data['prefix']}ping`\n`{data['prefix']}purge [amount]` **(OWNER ONLY)**\n`{data['prefix']}quickpoll`\n`{data['prefix']}timezone [location/offset]`\n\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(help(bot))