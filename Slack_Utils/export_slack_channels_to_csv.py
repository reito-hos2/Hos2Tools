import csv
import os
from slack_sdk import WebClient
from datetime import datetime, timezone, timedelta
from dotenv import load_dotenv
import os

# Slack APIクライアントの初期化
load_dotenv()

api_key = os.environ.get('SLACK_API_KEY')

if api_key is None:
    print("環境変数 SLACK_API_KEY が設定されていません。")
    exit(1)

client = WebClient(token=api_key)

jst = timezone(timedelta(hours=+9), 'JST')

# 出力ディレクトリが存在しない場合は作成
output_dir = './output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# CSVファイルへの出力設定
fieldnames = ['id', 'name', 'created', 'is_private', 'is_archived', 'is_general', 'topic', 'purpose', 'num_members']
output_path = os.path.join(output_dir, 'slack_channels.csv')

with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # APIリクエストのカーソルを初期化
    cursor = None

    while True:
        # APIからチャンネル情報を取得
        result = client.conversations_list(cursor=cursor)
        
        # チャンネル情報を処理
        for channel in result['channels']:
            created_date = datetime.fromtimestamp(channel['created'], tz=timezone.utc).astimezone(jst)
            writer.writerow({
                'id': channel['id'],
                'name': channel['name'],
                'created': created_date.strftime('%Y-%m-%d %H:%M:%S'),
                'is_private': channel.get('is_private', ''),
                'is_archived': channel.get('is_archived', ''),
                'is_general': channel.get('is_general', ''),
                'topic': channel['topic'].get('value', ''),
                'purpose': channel['purpose'].get('value', ''),
                'num_members': channel.get('num_members', '')
            })
        
        # 次のページのカーソルを取得
        cursor = result.get('response_metadata', {}).get('next_cursor')

        # 次のページがない場合はループを抜ける
        if not cursor:
            break
