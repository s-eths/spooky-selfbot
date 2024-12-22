import asyncio, os, requests, json
from discord.ext import commands
from data.print import *

with open("./data/config.json", "r") as file:
    data = json.load(file)

bot = commands.Bot(command_prefix = data["prefix"], self_bot = True, help_command = None, case_insensitive=True)

@bot.event
async def on_ready():
    os.system("cls"), print(logo()), print(login_box(bot.user))
    
def check_token(token):
    request = requests.get("https://discord.com/api/v9/users/@me", headers = {"Authorization": token})
    if request.status_code == 200:
        return "valid"
    else:
        return "invalid"

async def load():
    for folder in os.listdir("./cogs"):
        for file in os.listdir(f"./cogs/{folder}"):
            if file.endswith(".py"):
                await bot.load_extension(f"cogs.{folder}.{file[:-3]}")

async def main(token):
    await load(), await bot.start(token)

def startup():

    print(logo())

    if len(data["tokens"]["token"]) > 0:
        print(cool_text("Attempting to login to your token."))
        if check_token(data["tokens"]["token"]) == "valid":
            print(cool_text("Loading Spooky Self-Bot v1.1"))
            asyncio.run(main(data["tokens"]["token"]))
        else:
            print(cool_text("Invalid token, please input a working token: "))
            user_input = input("                    ")
            with open("data/token.txt", "w") as file:
                file.write(user_input)
            os.system("cls"), startup()
    else:
        print(cool_text("Please input your token: "))
        user_input = input("                    ")
        with open("data/token.txt", "w") as file:
            file.write(user_input)
        os.system("cls"), startup()
    
startup()