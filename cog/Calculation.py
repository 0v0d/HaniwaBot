from discord.ext import commands


class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='add')
    async def add_command(self, ctx, args):
        numbers = args.split(",")
        if len(numbers) < 2:
            await ctx.send("引数が少なすぎます。2つ以上の数値を入力してください。add")
            return
        try:
            result = sum(map(float, numbers))
            await ctx.send(f"結果は{result}")
        except ValueError:
            await ctx.send("数値以外の入力がありました。数値を入力してください。")

    @commands.command(name='sub')
    async def sub_command(self, ctx, args):
        numbers = args.split(",")
        if len(numbers) < 2:
            await ctx.send("引数が少なすぎます。2つ以上の数値を入力してください。sub")
            return
        try:
            result = float(numbers[0])
            for num in numbers[1:]:
                result -= float(num)
            await ctx.send(f"結果は{result}")
        except ValueError:
            await ctx.send("数値以外の入力がありました。数値を入力してください。")

    @commands.command(name='mul')
    async def mul_command(self, ctx, args):
        numbers = args.split(",")
        if len(numbers) < 2:
            await ctx.send("引数が少なすぎます。2つ以上の数値を入力してください。mul")
            return
        try:
            result = 1
            for num in numbers:
                result *= float(num)
            await ctx.send(f"結果は{result}")
        except ValueError:
            await ctx.send("数値以外の入力がありました。数値を入力してください。")

    @commands.command(name='div')
    async def div_command(self, ctx, args):
        numbers = args.split(",")
        if len(numbers) < 2:
            await ctx.send("引数が少なすぎます。2つ以上の数値を入力してください。div")
            return
        try:
            result = float(numbers[0])
            for num in numbers[1:]:
                result /= float(num)
            await ctx.send(f"結果は{result}")
        except ValueError:
            await ctx.send("数値以外の入力がありました。数値を入力してください。")
        except ZeroDivisionError:
            await ctx.send("0で割ることはできません。別の数値を入力してください。")
