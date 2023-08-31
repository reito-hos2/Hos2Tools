# Slack Channel List Exporter

この Python スクリプトは Slack の API を使用して、Slack のチャンネル情報を CSV ファイルに出力します。

## 主な機能

- Slack の API を使用してチャンネル情報を取得。
- 取得したチャンネル情報を CSV 形式で保存。
- 各チャンネルに関する以下のデータを出力:
  - ID
  - 名前
  - 作成日
  - プライベートかどうか
  - アーカイブされているか
  - 一般チャンネルかどうか
  - トピック
  - 目的（Purpose）
  - メンバー数

## 使用方法

1. Slack API トークンを`.env`に設定。
2. スクリプトを実行。

```bash
python export_slack_channels_to_csv.py
```

CSV ファイル`slack_channels.csv`が同ディレクトリ内に出力されます。
