import time
import os
import sys
import ctypes
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import re
import psutil
import hashlib
from colorama import Fore, Style, init


init()
print(Fore.YELLOW + "Welcome to my portfolio")
print("made by Takagi Yuui [rsy.0813pb@gmail.com]")
print("------------------------------------------" + Style.RESET_ALL)
appver = 11 # コードのバージョン設定

# 管理者権限で実行されているか確認する関数
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# 管理者として実行されていない場合、エラーメッセージを表示して終了
if not is_admin():
    print("このプログラムは管理者として実行してください。")
    time.sleep(5)  # 5秒待機
    sys.exit()  # プログラムを終了

# user_settings.cfgが現在の作業ディレクトリに存在するかチェックする。
config_file_path = os.path.join(os.getcwd(), 'user_settings.cfg')

# 設定ファイルからライセンスキーを読み込む関数
def read_license_key(config_file_path):
    with open(config_file_path, 'r') as file:
        for line in file:
            if "license_key" in line:
                return line.split('"')[1]  # 引用符で囲まれたライセンスキーを取り出す
    return ""  # ライセンスキーが見つからない場合は空文字列を返す

# 新しいライセンスキーを設定ファイルに書き込む関数
def write_license_key(config_file_path, new_license_key):
    with open(config_file_path, 'r') as file:
        lines = file.readlines()
    with open(config_file_path, 'w') as file:
        for line in lines:
            if "license_key" in line:
                # ライセンスキーを含む行を置き換える
                file.write(re.sub(r'license_key\s*".*"', f'license_key "{new_license_key}"', line))
            else:
                file.write(line)

# ファイルが存在しない場合は、デフォルト設定を作成して書き込みます。
if not os.path.exists(config_file_path):
    with open(config_file_path, 'w') as config_file:
        config_file.write('''license_key ""''')

license_key = read_license_key(config_file_path)
if not license_key:
    # ライセンスキーが空の場合は、新しいライセンスキーの入力を求めます。
    new_license_key = input("ライセンスキーを入力してください: ")
    write_license_key(config_file_path, new_license_key)
    license_key = new_license_key  # ライセンスキー変数を新しい値で更新する

# credentials.json の内容を変数に割り当てる
credentials_data = {
### 任意のcredentials.jsonを挿入します
}


# Google API認証情報
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_data, scope)
client = gspread.authorize(creds)

# スプレッドシートのキーを指定
sheet_key = '1kNSog0H2J_QBX5mIQ9j9UcRbY3q9LpcdG_9upwbNOHs'
sheet = client.open_by_key(sheet_key).sheet1
sheet2 = client.open_by_key(sheet_key).worksheet('情報')

# ライセンス情報を取得
licenses = sheet.get_all_records()
information = sheet2.get_all_records()

# デバイスのHWIDを取得する関数
def get_hwid():
    # CPU情報を取得
    cpu_info = psutil.cpu_freq()
    # メインディスクのパーティション情報を取得
    disk_info = psutil.disk_partitions()[0]

    # CPU、ディスク、GPU情報を組み合わせて一意な文字列を生成 #{gpu_id}{gpu_name}
    unique_str = f"{cpu_info.current}{disk_info.device}"

    # SHA256を使用してハッシュ化し、HWIDを生成
    hwid = hashlib.sha256(unique_str.encode()).hexdigest()
    return hwid


# ライセンスの有効性をチェックする関数
def check_license(license_key):
    for index, row in enumerate(licenses, start=2):
        if str(row['ライセンスキー']) == license_key:
            expiration_date = row['許可期限']
            if not expiration_date:
                key_type = row['許可日数区分']
                if key_type == '1day':
                    expiration_date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y/%m/%d %H:%M:%S')
                elif key_type == '3months':
                    expiration_date = (datetime.datetime.now() + datetime.timedelta(days=90)).strftime('%Y/%m/%d %H:%M:%S')
                elif key_type == '6months':
                    expiration_date = (datetime.datetime.now() + datetime.timedelta(days=180)).strftime('%Y/%m/%d %H:%M:%S')
                sheet.update_cell(index, 3, expiration_date)
            else:
                expiration_date = datetime.datetime.strptime(expiration_date, '%Y/%m/%d %H:%M:%S')
                if expiration_date < datetime.datetime.now():
                    print("ライセンスの許可期限が切れています。")
                    return False, None
            hwid = row['HWID']
            if not hwid:
                sheet.update_cell(index, 4, get_hwid())
            else:
                current_hwid = get_hwid()
                if hwid != current_hwid:
                    print("HWIDが違います。")
                    print("ライセンスキーと紐づけたHWIDを変更したい場合は管理者に問い合わせてください。")
                    return False, None
            return True, expiration_date  # 有効期限を返す
    print("入力したライセンスキーは存在しません。")
    return False, None

# 情報を通知する関数
def check_information():
    for index, row in enumerate(information, start=2):
        current_appver = row['最新バージョン']
        if appver != current_appver:
            print(f"アップデートしてください 最新:[{current_appver}]/現在:[{appver}]")
            return False, None
        if appver == current_appver:
            print(f"バージョン{appver}")
            return False, None
        return True, expiration_date  # 有効期限を返す
    return 0

# ライセンスキーを使用して処理を進める
is_license_valid, expiration_date = check_license(license_key)  # ライセンスキーの検証
check_information()

if is_license_valid:
    print("ライセンス:" + Fore.GREEN + "有効" + Style.RESET_ALL + f" / 許可期限:[{expiration_date}]")  # 許可期限出力
    print("----------------------------------------------\n")
else:
    print("プログラムを終了します。")
    write_license_key(config_file_path, "")  # ライセンスキーをデフォルトに戻す
    time.sleep(5)  # 5秒待機
    sys.exit()  # プログラムを終了


# メインコード

def main():
        while True:
            print("Say Hello")
            time.sleep(5)

if __name__ == "__main__":
    main()
