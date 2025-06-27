import discord, os, requests, json, asyncio
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

def get_crypto_coin(crypto_currency):
    coin_translator = {
        "btc": "bitcoin",
        "eth": "ethereum",
        "sol": "solana",
        "doge": "dogecoin",
        "ltc": "litecoin",
        "xmr": "monero"
    }

    if crypto_currency in coin_translator:
        return coin_translator[crypto_currency]
    elif crypto_currency in coin_translator.values():
        return crypto_currency
    else:
        return False

class crypto(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content.startswith(f"{data['prefix']}crypto"):
                split_message = message.content.split()
                if len(split_message) <= 2:
                    crypto_coin = get_crypto_coin(split_message[1])
                    if not crypto_coin:
                        error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** **{split_message[1]}** is Either Invalid or a Unsupported Coin.\n\n-# Created by @ s.eths・v{data['version']}")
                        await asyncio.sleep(3)
                        await error.delete()
                        return
                    current_coin_value = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_coin}&vs_currencies=usd").json()
                    await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Current Price Per Coin: **${current_coin_value[crypto_coin]['usd']:,}.**\n\n-# Created by @ s.eths・v{data['version']}")
                    os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}crypto {crypto_coin}` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def crypto(self, ctx, crypto_currency):
        crypto_coin = get_crypto_coin(crypto_currency)
        if not crypto_coin:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** **{crypto_currency}** is Either Invalid or a Unsupported Coin.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        await ctx.message.delete()
        current_coin_value = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_coin}&vs_currencies=usd").json()
        await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[!]** Current Price Per Coin: **${current_coin_value[crypto_coin]['usd']:,}.**\n\n-# Created by @ s.eths・v{data['version']}")

async def setup(bot):
    await bot.add_cog(crypto(bot))