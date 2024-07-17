import discord

from discord import app_commands


class DecorateText(app_commands.Group):
    def __init__(self):
        super().__init__(name="decorate", description="テキスト装飾コマンド")

    @app_commands.command(name="code", description="コードを装飾")
    @app_commands.choices(language=[
        app_commands.Choice(name="Python", value="py"),
        app_commands.Choice(name="C++", value="cpp"),
        app_commands.Choice(name="C#", value="cs"),
        app_commands.Choice(name="Java", value="java"),
        app_commands.Choice(name="TypeScript", value="ts"),
        app_commands.Choice(name="JavaScript", value="js"),
        app_commands.Choice(name="Markdown", value="md"),
        app_commands.Choice(name="Diff", value="diff")
    ])
    async def decorate_code(
            self,
            interaction: discord.Interaction,
            language: app_commands.Choice[str],
            code: str
    ):
        try:
            formatted_code = f'```{language.value}\n{code}\n```'
            if len(formatted_code) > 2000:
                await interaction.response.send_message(
                    "エラー: コードが2000文字を超えています。より短いコードを入力してください。", ephemeral=True)
            else:
                await interaction.response.send_message(formatted_code)
        except Exception as e:
            await interaction.response.send_message(f"エラーが発生しました: {str(e)}", ephemeral=True)
