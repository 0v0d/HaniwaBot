import os

import discord
from dotenv import load_dotenv
from Keep_Alive import keep_alive
from cog.Calculation import Calculator
from cog.Decorate import DecorateText
from cog.Random import RandomGenerator
from cog.Weather import Weather

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)


@client.event
async def on_ready():
    print("Started")
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(activity=discord.Game(name="im sleepy"))
    await tree.sync()


load_dotenv()

commands = [RandomGenerator(), DecorateText(), Calculator(), Weather()]

for command in commands:
    tree.add_command(command)

keep_alive()
client.run(os.getenv("DISCORD_BOT_TOKEN"))
