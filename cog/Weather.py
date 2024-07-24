import discord
from discord import app_commands
import aiohttp

url: str = "https://www.jma.go.jp/bosai/forecast/data/forecast/"
json: str = '.json'
location_map = {
    "北海道": "016000",
    "青森": "020000",
    "岩手": "030000",
    "宮城": "040000",
    "秋田": "050000",
    "山形": "060000",
    "福島": "070000",
    "茨城": "080000",
    "栃木": "090000",
    "群馬": "100000",
    "埼玉": "110000",
    "千葉": "120000",
    "東京": "130000",
    "神奈川": "140000",
    "新潟": "150000",
    "富山": "160000",
    "石川": "170000",
    "福井": "180000",
    "山梨": "190000",
    "長野": "200000",
    "岐阜": "210000",
    "静岡": "220000",
    "愛知": "230000",
    "三重": "240000",
    "滋賀": "250000",
    "京都": "260000",
    "大阪": "270000",
    "兵庫": "280000",
    "奈良": "290000",
    "和歌山": "300000",
    "鳥取": "310000",
    "島根": "320000",
    "岡山": "330000",
    "広島": "340000",
    "山口": "350000",
    "徳島": "360000",
    "香川": "370000",
    "愛媛": "380000",
    "高知": "390000",
    "福岡": "400000",
    "佐賀": "410000",
    "長崎": "420000",
    "熊本": "430000",
    "大分": "440000",
    "宮崎": "450000",
    "鹿児島": "460100",
    "沖縄": "471000",
}


class Weather(app_commands.Group):
    def __init__(self):
        super().__init__(name="weather", description="天気情報コマンド")

    @app_commands.command(name="forecast", description="明日の天気予報を表示")
    @app_commands.choices(location=[
        app_commands.Choice(name=key, value=key) for key in location_map.keys()
    ])
    async def weather_forecast(self, interaction: discord.Interaction, location: str):
        await interaction.response.defer()
        try:
            location_code = location_map.get(location)
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
