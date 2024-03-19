# Portfolio

このリポジトリは、就活のためのポートフォリオとして作成されたPythonプログラムです。

## 機能

- Google SpreadsheetのAPIを使用してライセンス情報を管理
- デバイスのハードウェアIDを取得し、ライセンス認証に使用
- ライセンスキーの有効性チェックと期限管理
- アプリケーションのバージョン管理と更新通知
- メインプログラムの実行

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
   git clone https://github.com/rsy-0813pb/Portfolio-License-management-using-spreadsheets.git
   cd Portfolio-License-management-using-spreadsheets
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
3. 右上のチェックボックスにチェックを入れるとキーが生成されます：
- 使いやすいように既にいくつかテストキーが生成されています：

## 使用方法

1. プログラムを管理者権限で実行します：
2. ライセンスキーを入力します：
- [スプレッドシートから取得できます：](https://docs.google.com/spreadsheets/d/1kNSog0H2J_QBX5mIQ9j9UcRbY3q9LpcdG_9upwbNOHs/edit?usp=sharing)
4. ライセンスの有効性とアプリケーションのバージョンがチェックされます：
5. ライセンスが有効な場合、メインプログラムが実行されます：

## 注意事項

- このプログラムは、管理者権限で実行する必要があります：
- ライセンスキーは、Google Spreadsheetで管理されています。適切なスプレッドシートのキーと認証情報を設定してください：

## ライセンス

このプロジェクトは、MITライセンスの下で公開されています。

## 作者

- 名前：Takagi Yuui

ご不明な点がございましたら、お気軽にお問い合わせください。
