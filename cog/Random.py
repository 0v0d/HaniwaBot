import random
import discord
from discord import app_commands


class RandomGenerator(app_commands.Group):
    def __init__(self):
        super().__init__(name="random", description="ランダム生成コマンド")

    @app_commands.command(name="number", description="ランダムな整数を生成")
    async def random_number(
            self,
            interaction: discord.Interaction,
            min_val: int = 1,
            max_val: int = 100
    ):
        if min_val > max_val:
            await interaction.response.send_message(
                'エラー: 最小値が最大値より大きいです。値を入れ替えて処理を続行します。', ephemeral=True)
            min_val, max_val = max_val, min_val

        result = random.randint(min_val, max_val)
        await interaction.response.send_message(f'生成された数字: {result}\n範囲: {min_val} から {max_val}')

    @app_commands.command(name="choice", description="リストからランダムに要素を選択")
    async def random_choice(
            self,
            interaction: discord.Interaction,
            choices: str
    ):
        choice_list = [choice.strip() for choice in choices.split(',') if choice.strip()]

        if not choice_list:
            await interaction.response.send_message(
                'エラー: 有効な選択肢がありません。カンマ区切りで選択肢を入力してください。', ephemeral=True)
            return

        result = random.choice(choice_list)
        await interaction.response.send_message(f'選ばれた要素: {result}\n選択肢: {", ".join(choice_list)}')


# メインファイルでこのように追加します
