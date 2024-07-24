import discord
from discord import app_commands
import aiohttp

from model.LocationMap import location_map

url: str = "https://www.jma.go.jp/bosai/forecast/data/forecast/"
json: str = '.json'


async def weather_forecast(interaction: discord.Interaction, region: str, location: str):
    await interaction.response.defer()
    try:
        location_code = location_map[region].get(location)
        if not location_code:
            await interaction.followup.send(f'エラー: {location} の地域コードが見つかりません。', ephemeral=True)
            return

        weather_data = await get_weather(location_code)
        if weather_data:
            embed = create_weather_embed(location, weather_data)
            await interaction.followup.send(embed=embed)
        else:
            await interaction.followup.send('天気情報を取得できませんでした。', ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f'エラーが発生しました: {str(e)}', ephemeral=True)


class Weather(app_commands.Group):
    def __init__(self):
        super().__init__(name="weather", description="天気情報コマンド")

    @app_commands.command(name="hokkaido", description="北海道の明日の天気予報を表示")
    @app_commands.choices(loc=[
        app_commands.Choice(name=key, value=key) for key in location_map["北海道"].keys()
    ])
    async def weather_forecast_hokkaido(self, interaction: discord.Interaction, loc: str):
        await weather_forecast(interaction, "北海道", loc)

    @app_commands.command(name="tohoku", description="東北地方の明日の天気予報を表示")
    @app_commands.choices(loc=[
        app_commands.Choice(name=key, value=key) for key in location_map["東北"].keys()
    ])
    async def weather_forecast_tohoku(self, interaction: discord.Interaction, loc: str):
        await weather_forecast(interaction, "東北", loc)

    @app_commands.command(name="kanto", description="関東地方の明日の天気予報を表示")
    @app_commands.choices(loc=[
        app_commands.Choice(name=key, value=key) for key in location_map["関東"].keys()
    ])
    async def weather_forecast_kanto(self, interaction: discord.Interaction, loc: str):
        await weather_forecast(interaction, "関東", loc)

    @app_commands.command(name="chubu", description="中部地方の明日の天気予報を表示")
    @app_commands.choices(loc=[
        app_commands.Choice(name=key, value=key) for key in location_map["中部"].keys()
    ])
    async def weather_forecast_chubu(self, interaction: discord.Interaction, loc: str):
        await weather_forecast(interaction, "中部", loc)

    @app_commands.command(name="kinki", description="近畿地方の明日の天気予報を表示")
    @app_commands.choices(loc=[
        app_commands.Choice(name=key, value=key) for key in location_map["近畿"].keys()
    ])
    async def weather_forecast_kinki(self, interaction: discord.Interaction, loc: str):
        await weather_forecast(interaction, "近畿", loc)

    @app_commands.command(name="chugoku", description="中国地方の明日の天気予報を表示")
    @app_commands.choices(loc=[
        app_commands.Choice(name=key, value=key) for key in location_map["中国"].keys()
    ])
    async def weather_forecast_chugoku(self, interaction: discord.Interaction, loc: str):
        await weather_forecast(interaction, "中国", loc)

    @app_commands.command(name="shikoku", description="四国地方の明日の天気予報を表示")
    @app_commands.choices(loc=[
        app_commands.Choice(name=key, value=key) for key in location_map["四国"].keys()
    ])
    async def weather_forecast_shikoku(self, interaction: discord.Interaction, loc: str):
        await weather_forecast(interaction, "四国", loc)

    @app_commands.command(name="kyushu", description="九州地方の明日の天気予報を表示")
    @app_commands.choices(loc=[
        app_commands.Choice(name=key, value=key) for key in location_map["九州"].keys()
    ])
    async def weather_forecast_kyushu(self, interaction: discord.Interaction, loc: str):
        await weather_forecast(interaction, "九州", loc)

    @app_commands.command(name="okinawa", description="沖縄の明日の天気予報を表示")
    @app_commands.choices(loc=[
        app_commands.Choice(name=key, value=key) for key in location_map["沖縄"].keys()
    ])
    async def weather_forecast_okinawa(self, interaction: discord.Interaction, loc: str):
        await weather_forecast(interaction, "沖縄", loc)


async def get_weather(location_code: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{url}{location_code}{json}") as response:
            if response.status == 200:
                jma_json = await response.json()
                return parse_weather_data(jma_json)
    return None


def parse_weather_data(jma_json):
    weather_data = []
    time_series = jma_json[0]["timeSeries"][0]
    time_defines = time_series["timeDefines"]
    areas = time_series["areas"]

    for day, time_define in enumerate(time_defines):
        formatted_time = time_define[:16].replace('T', ' ')
        for area in areas:
            area_name = area["area"]["name"].strip()
            weather = area["weathers"][day].strip()
            weather_data.append({
                'time': formatted_time,
                'area_name': area_name,
                'weather': weather
            })
    return weather_data


def create_weather_embed(location: str, weather_data: list):
    embed = discord.Embed(title=f'{location}の天気予報', color=discord.Color.blue())
    for data in weather_data:
        embed.add_field(name=f"{data['time']} - {data['area_name']}",
                        value=f"天気: {data['weather']}",
                        inline=False)
    return embed
