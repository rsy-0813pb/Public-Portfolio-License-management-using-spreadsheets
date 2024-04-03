# Portfolio

このリポジトリは、就活のためのポートフォリオとして作成されたPythonプログラムです。

## 機能

1. 管理者権限で実行されているかチェックし、管理者として実行されていない場合はエラーメッセージを表示してプログラムを終了
2. user_settings.cfgファイルからライセンスキーを読み込み、ファイルが存在しない場合はデフォルト設定を作成
3. Google Sheets APIを使用してスプレッドシートからライセンス情報と情報を取得
4. ライセンスキーの有効性をチェックし、有効期限を確認
5. デバイスのHWID（ハードウェアID）を取得し、ライセンスキーとHWIDが一致しているか確認
6. プログラムのバージョンをチェックし、最新バージョンではない場合はアップデートを促す
7. ライセンスキーが無効な場合は、user_settings.cfgファイルからライセンスキーを削除し、プログラムを終了
8. ライセンスキーが有効な場合は、メインプログラムを実行

## 必要な環境

- Python 3.x
- Google Cloud Platform（GCP）のサービスアカウント認証情報（`credentials.json`）
- 以下のPythonライブラリ：
  - `gspread`
  - `oauth2client`
  - `psutil`
  - `colorama`

## Windows環境でのセットアップ

1. このリポジトリをクローンまたはダウンロードします：
   ```
   git clone https://github.com/rsy-0813pb/Public-Portfolio-License-m-u-s.git
   cd Public-Portfolio-License-m-u-s
   ```
2. 必要なライブラリをインポートします：
   ```
   pip install -r requirements.txt
   ```
   もしくは1つ1つ必要なPythonライブラリを指定してインストールします：
   ```
   pip install gspread oauth2client psutil colorama
   ```
3. コードの中のcredentials.json部分とスプレッドシートのキーを任意のものへ変更します。スプレッドシートは下のライセンス管理方法からダウンロードできます。
4. プログラムを実行します：
   ```
   python main.py
   ```

## ライセンス管理方法

1. [スプレッドシートにアクセスします：](https://docs.google.com/spreadsheets/d/1kNSog0H2J_QBX5mIQ9j9UcRbY3q9LpcdG_9upwbNOHs/edit?usp=sharing)
- すべての編集権限があります。気をつけて使用してください。バックアップがあるので破壊しても大丈夫ですが、破壊後は連絡してください：
2. 右上のチェックボックスにチェックを入れるとキーが生成されます：
- 使いやすいように既にいくつかテストキーが生成されています：

## 使用方法

1. プログラムを管理者権限で実行します：
2. ライセンスキーを入力します：
- [スプレッドシートから取得できます：](https://docs.google.com/spreadsheets/d/1kNSog0H2J_QBX5mIQ9j9UcRbY3q9LpcdG_9upwbNOHs/edit?usp=sharing)
3. ライセンスの有効性とアプリケーションのバージョンがチェックされます：
4. ライセンスが有効な場合、メインプログラムが実行されます：

## 注意事項

- このプログラムは、管理者権限で実行する必要があります：
- ライセンスキーは、Google Spreadsheetで管理されています。適切なスプレッドシートのキーと認証情報を設定してください：

## 作者

- 名前：Takagi Yuui

ご不明な点がございましたら、お気軽にお問い合わせください。
