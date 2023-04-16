from discord.ext import commands


class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.lower() == '(´・ω・｀)' and message.author != self.bot.user:
            await message.channel.send('(´・ω・｀)')

    @commands.command()
    async def dog(self, ctx):
        await ctx.send('ワン！')

    @commands.command()
    async def cat(self, ctx):
        await ctx.send('にゃん！')

    @commands.command()
    async def bard(self, ctx):
        await ctx.send('tweet')