import discord, os, json, asyncio, random, faker
from discord.ext import commands
from data.print import *

with open ("./data/config.json", "r") as file:
    data = json.load(file)

hack_strings = [
    "Hacking the mainframe...",
    "Bypassing firewall...",
    "Decrypting passwords...",
    "Accessing secure server...",
    "Injecting malware...",
    "Downloading confidential data...",
    "Initiating DDoS attack...",
    "Compromising security protocols...",
    "Gaining root access...",
    "Simulating hack...",
    "Cracking encryption...",
    "Phishing for credentials...",
    "Scanning for vulnerabilities...",
    "Exploiting backdoor...",
    "Hijacking session...",
    "Spoofing IP address...",
    "Brute-forcing login...",
    "Planting trojan...",
    "Overclocking CPU...",
    "Mining cryptocurrency..."
]

class hack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in data["whitelisted"]:
            if message.content.startswith(f"{data['prefix']}hack"):
                if not message.mentions:
                    error = await message.reply(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** **discord.User** is Missing, Incomplete or Incorrect.\n\n-# Created by @ s.eths・v{data['version']}")
                    await asyncio.sleep(3)
                    await error.delete()
                    return
                user = message.mentions[0]
                message = await message.reply(f"Attempting to hack {user.mention}.")
                for i in range(5):
                    await asyncio.sleep(1)
                    await message.edit(random.choice(hack_strings))
                await asyncio.sleep(1)
                await message.edit(f"Successfully hacked {user.mention}, GG\n\nFull Name: {faker.Faker().name()}\n\nAddress: {faker.Faker().address()}\n\nPhone Number: {faker.Faker().phone_number()}\n\nIP: {faker.Faker().ipv4()}\n\nIPv6: {faker.Faker().ipv6()}\n\nSSN: {faker.Faker().ssn()}\n\nMAC: {faker.Faker().mac_address()}\n\nISP: {faker.Faker().company()}")
                os.system("cls"), print(logo()), print(login_box(self.bot.user)), print(output_text(f"[<>] `{data['prefix']}hack @{user.name}` has been successfully ran by {message.author}"))
    
    @commands.command()
    async def hack(self, ctx, user: discord.User = None):
        if not user:
            await ctx.message.delete()
            error = await ctx.send(f"**spooky.wtf - Discord Self-Bot**\n\n> **[?]** **discord.User** is Missing, Incomplete or Incorrect.\n\n-# Created by @ s.eths・v{data['version']}")
            await asyncio.sleep(3)
            await error.delete()
            return
        await ctx.message.delete()
        message = await ctx.send(f"Attempting to hack {user.mention}.")
        for i in range(5):
            await asyncio.sleep(1)
            await message.edit(random.choice(hack_strings))
        await asyncio.sleep(1)
        await message.edit(f"Successfully hacked {user.mention}, GG\n\nFull Name: {faker.Faker().name()}\n\nAddress: {faker.Faker().address()}\n\nPhone Number: {faker.Faker().phone_number()}\n\nIP: {faker.Faker().ipv4()}\n\nIPv6: {faker.Faker().ipv6()}\n\nSSN: {faker.Faker().ssn()}\n\nMAC: {faker.Faker().mac_address()}\n\nISP: {faker.Faker().company()}")

async def setup(bot):
    await bot.add_cog(hack(bot))