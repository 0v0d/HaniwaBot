import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from keep_alive import keep_alive

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
from cog.Calculation import Calculator
from cog.sub import MyCog
from cog.Random import Random

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(
  command_prefix=commands.when_mentioned_or("h"),
  intents=intents,
  case_insensitive=True,
  help_command=None,
)


@client.event
async def on_ready():
  print('ログインしました')
  await client.add_cog(MyCog(client))
  await client.add_cog(Calculator(client))
  await client.add_cog(Random(client))
  print(client.user.name)  # Botの名前
  print(client.user.id)  # ID
  await client.change_presence(activity=discord.Game(
    name=f"{len(client.guilds)}サーバー"))


keep_alive()
try:
  client.run(os.environ.get("DISCORD_BOT_TOKEN"))
except:
  os.system("kill 1")
