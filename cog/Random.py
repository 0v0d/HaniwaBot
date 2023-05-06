from discord.ext import commands
import random

class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='r')
    async def random(self, ctx, args='1,100'):
        numbers = args.split(",")
        try:
            min_val = int(numbers[0])
            max_val = int(numbers[1])
        except ValueError:
            await ctx.send('Error')
            return
        if min_val > max_val:
            await ctx.send('小さいほうを先に書いてね')
            return
        await ctx.send(f'{random.randint(min_val, max_val)}')
