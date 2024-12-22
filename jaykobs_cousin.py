import discord, os, random
from discord.ext import commands

world_records = [
    "The longest time holding the breath underwater is 24 minutes 37.36 seconds,",
    "The fastest 100 meters by a human is 9.58 seconds,",
    "The tallest man ever recorded was 8 feet 11 inches tall,",
    "The longest fingernails ever measured on a pair of hands were 909.6 cm (358.1 in),",
    "The heaviest pumpkin weighed 1,190.49 kg (2,624.6 lb),",
    "The most tattoos in 24 hours by a single person is 801,",
    "The largest pizza ever made was 13,580.28 square feet,",
    "The longest marathon playing a board game is 80 hours,",
    "The longest distance swum underwater with one breath is 200 meters,",
    "The most skips over a single rope in one minute by a team is 230,",
    "The fastest marathon dressed as a vegetable is 2 hours 59 minutes 33 seconds,",
    "The most people performing a choreographed dance is 50,085,",
    "The longest time balancing on one foot is 76 hours 40 minutes,",
    "The most spoons balanced on the face is 31,",
    "The largest collection of rubber ducks is 9,000,",
    "The longest time spent in direct full-body contact with snow is 1 hour 53 minutes 10 seconds,",
    "The most push-ups in one hour is 3,054,",
    "The fastest time to solve a Rubik's Cube one-handed is 6.82 seconds,",
    "The largest gathering of people dressed as penguins is 624,",
    "The longest distance cycled in 24 hours is 914.02 km (567.27 miles),"
]

class jaykobs_cousin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group()
    async def jaykobs(self, ctx):
        return

    @jaykobs.command()
    async def cousin(self, ctx):
        await ctx.message.delete()
        await ctx.send(f"```ansi\n[2;34m[2;41m[2;37m[1;37m[1;31m[1;33m[1;37mSpooky - Discord Self-Bot v1.1[1;35m[0m[1;37m[1;41m[0m[1;33m[1;41m[0m[1;31m[1;41m[0m[1;37m[1;41m[0m[2;37m[2;41m[0m[2;34m[2;41m[0m[2;34m[0m```\n\n`<>`  {random.choice(world_records)} Which is currently owned by Jaykob's Cousin.\n\n```ansi\n[2;45m[2;35m[2;37m[1;37mCreated by @s.eths[0m[2;37m[2;45m[0m[2;35m[2;45m[0m[2;45m[0m```")

async def setup(bot):
    await bot.add_cog(jaykobs_cousin(bot))