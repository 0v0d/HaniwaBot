# HaniwaBot

## 概要
HaniwaBotは、Pythonで作成されたDiscordBotです。スラッシュコマンドをサポートし、計算やランダム選択、天気予報などの機能を提供します。

## コマンド一覧

### 計算コマンド
- **/calc add**: 2項の加算
- **/calc sub**: 2項の減算
- **/calc mul**: 2項の乗算
- **/calc div**: 2項の除算
- **/calc mod**: 2項の剰余

### 装飾コマンド
- **/decorate code**: コードを\`\`\`で囲み、マークダウン化する

### ランダム選択コマンド
- **/random choice**: ユーザーが入力したリストの中からランダムに選択
- **/random number**: 最小値と最大値の範囲でランダムな数字を選択（デフォルト: 0から100）

### 天気予報コマンド
- **/weather forecast**: 気象庁のAPIを使用して、3日間の天気予報を表示

## インストール

### 1. リポジトリをクローン
```sh
git clone https://github.com/0v0d/HaniwaBot.git
```

### 2. ディレクトリに移動
```sh
cd HaniwaBot
```

### 3. 必要なパッケージをインストール
```sh
pip install -r requirements.txt
```

## Botアカウントの作成方法

### 1. Discord Developer Portalにアクセス
[Discord Developer Portal](https://discord.com/developers/applications)にアクセスし、Discordアカウントでログインします。

### 2. 新しいアプリケーションを作成
- 右上の「New Application」をクリックします。
- アプリケーション名を入力し、「Create」をクリックします。

### 3. Botを追加
- 左側のメニューから「Bot」を選択し、「Add Bot」をクリックします。
- 確認ダイアログが表示されたら「Yes, do it!」をクリックします。

### 4. トークンを取得
- 「Click to Reveal Token」をクリックし、表示されたトークンをコピーします。
- トークンは他人に知られないように注意してください。

### 5. 必要な権限を設定
- 左側のメニューから「OAuth2」を選択し、「URL Generator」をクリックします。
- 「SCOPES」で「bot」を選択し、「BOT PERMISSIONS」で必要な権限を選択します（例: Send Messages, Read Message History）。
- 生成されたURLをコピーし、ブラウザで開き、Botを自分のサーバーに追加します。

## 設定ファイルの作成

### 1. `.env`ファイルを作成
リポジトリのルートディレクトリに`.env`ファイルを作成し、以下の内容を追加します:
```env
DISCORD_TOKEN=あなたのディスコードトークン
```
※「あなたのディスコードトークン」は、先ほどコピーしたBotトークンを入力してください。

## デプロイ

HaniwaBotを常時起動するためには、[Render.com](https://render.com/)を使用することをおすすめします。以下の手順でデプロイしてください。

### Render.comを使用してデプロイ
1. [Render.com](https://render.com/)にアクセスし、アカウントを作成します。
2. 「New +」をクリックし、「Web Service」を選択します。
3. GitHubリポジトリを連携し、HaniwaBotのリポジトリを選択します。
4. ビルドコマンドと起動コマンドを設定します。
    - ビルドコマンド: `pip install -r requirements.txt`
    - 起動コマンド: `python bot.py`

詳しいデプロイ手順は[こちらのQiita記事](https://qiita.com/Erytheia/items/2f64c06d6d8a4f802390)を参照してください。

### サーバーを常時起動する方法

#### UptimeRobotを使用する場合
[UptimeRobot](https://uptimerobot.com/)を使用して、定期的にPingを送信し、サーバーを常時起動状態に保ちます。UptimeRobotに登録し、新しいHTTPモニターを設定します。Render.comのURLを入力し、監視間隔を設定します。

#### Google Apps Scriptを使用する場合
Google Apps Scriptを使用して、サーバーを定期的に起動することもできます。以下のスクリプトを使用します:

```js
const SCRIPT_URL = PropertiesService.getScriptProperties().getProperty('renderURL');

function wake() {
  const jsonPayload = createWakePayload();
  send(SCRIPT_URL, jsonPayload);
}

function createWakePayload() {
  return {
    type: 'wake'
  };
}

function send(uri, json) {
  const params = createRequestParams(json);
  const response = UrlFetchApp.fetch(uri, params);
}

function createRequestParams(json) {
  return {
    contentType: 'application/json; charset=utf-8',
    method: 'post',
    payload: JSON.stringify(json),
    muteHttpExceptions: true
  };
}
```

このスクリプトをGoogle Apps Scriptに貼り付け、`SCRIPT_URL`をRender.comのURLに設定します。

## 注意点

ReplitではDiscordBotの常時起動が無料ではできません。常時起動を実現するためには、Render.comや他の有料サービスを利用する必要があります。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。詳細は`LICENSE`ファイルを参照してください。

---

## リンク
- [Discord Developer Portal](https://discord.com/developers/applications)
- [discord.py Documentation (日本語)](https://discordpy.readthedocs.io/ja/latest/discord.html#)
- [Render.com](https://render.com/)
- [UptimeRobot](https://uptimerobot.com/)
- [Qiita記事](https://qiita.com/Erytheia/items/2f64c06d6d8a4f802390)

このガイドに従って、HaniwaBotをセットアップし、さまざまな便利な機能をDiscordサーバーで活用してください。