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

---
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
DISCORD_TOKEN=あなたのディスコードボットトークン
```
※「あなたのディスコードトークン」は、先ほどコピーしたBotトークンを入力してください。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。詳細は`LICENSE`ファイルを参照してください。

---

## リンク
- [Discord Developer Portal](https://discord.com/developers/applications)
- [discord.py Documentation (日本語)](https://discordpy.readthedocs.io/ja/latest/discord.html#)

このガイドに従って、HaniwaBotをセットアップし、さまざまな便利な機能をDiscordサーバーで活用してください。