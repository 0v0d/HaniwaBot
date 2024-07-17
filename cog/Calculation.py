from discord import app_commands


class Calculator(app_commands.Group):
    ZERO_DIVISION_ERROR_MESSAGE = "0で割ることはできません。別の数値を入力してください。"

    def __init__(self):
        super().__init__(name="calc", description="計算機能")

    @app_commands.command(description="加算")
    async def add(self, interaction, a: float, b: float):
        await interaction.response.send_message(f"結果は{a + b}")

    @app_commands.command(description="減算")
    async def sub(self, interaction, a: float, b: float):
        await interaction.response.send_message(f"結果は{a - b}")

    @app_commands.command(description="乗算")
    async def mul(self, interaction, a: float, b: float):
        await interaction.response.send_message(f"結果は{a * b}")

    @app_commands.command(description="除算")
    async def div(self, interaction, a: float, b: float):
        if b == 0:
            return await interaction.response.send_message(self.ZERO_DIVISION_ERROR_MESSAGE)
        await interaction.response.send_message(f"結果は{a / b}")

    @app_commands.command(description="商算")
    async def mod(self, interaction, a: float, b: float):
        if b == 0:
            return await interaction.response.send_message(self.ZERO_DIVISION_ERROR_MESSAGE)
        await interaction.response.send_message(f"結果は{a % b}")
