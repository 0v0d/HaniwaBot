from discord.ext import commands


class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ARGUMENTS_ERROR_MESSAGE = "引数が少なすぎます。2つ以上の数値を入力してください。"
    NUMERIC_ERROR_MESSAGE = "数値以外の入力がありました。数値を入力してください。"
    ZERO_DIVISION_ERROR_MESSAGE = "0で割ることはできません。別の数値を入力してください。"

    async def check_args(self,ctx, args):
        numbers = args.split(",")
        if not len(numbers) >= 2:
            await ctx.send(self.ARGUMENTS_ERROR_MESSAGE+f"{ctx.command.name}")
            return None
        try:
            numbers = list(map(float, numbers))
        except ValueError:
            await ctx.send(self.NUMERIC_ERROR_MESSAGE)
            return None
        return numbers

    @commands.command(name='add')
    async def add_command(self, ctx, args):
        numbers = await self.check_args(ctx, args)
        if numbers is None:
            return
        result = sum(numbers)
        await ctx.send(f"結果は{result}")

    @commands.command(name='sub')
    async def sub_command(self, ctx, args):
        numbers = await self.check_args(ctx, args)
        if numbers is None:
            return
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        await ctx.send(f"結果は{result}")

    @commands.command(name='mul')
    async def mul_command(self, ctx, args):
        numbers = await self.check_args(ctx, args)
        if numbers is None:
            return
        result = 1
        for num in numbers:
            result *= num
        await ctx.send(f"結果は{result}")

    @commands.command(name='div')
    async def div_command(self, ctx, args):
        numbers = await self.check_args(ctx, args)
        if numbers is None:
            return
        if 0 in numbers[1:]:
            await ctx.send(self.ZERO_DIVISION_ERROR_MESSAGE)
            return
        result = numbers[0]
        for num in numbers[1:]:
            result /= num
        await ctx.send(f"結果は{result}")
