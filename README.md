# Hos2Tools

個人用のスクリプト保管場所。GitHub の練習です。

## インストール

このリポジトリをクローン後、必要な Python パッケージをインストールします。

```bash
git clone https://github.com/yourusername/Hos2Tools.git
cd Hos2Tools
pip install -r requirements.txt  # まだない
```

## 使い方

### FileFormatTools

`csv_tsv_to_bom_xlsx_converter.py`を使用する場合:

```bash
python FileFormatTools/csv_tsv_to_bom_xlsx_converter.py input.csv
```

### Slack_Utils

`export_slack_channels_to_csv.py`を使用する場合:

```bash
python Slack_Utils/export_slack_channels_to_csv.py
```

## 環境設定

1. `.env.sample`を`.env`としてコピーします。
2. `.env`内の`SLACK_API_KEY`を適切な値に設定します。

```bash
cp .env.sample .env
# .envを編集してSLACK_API_KEYを設定
```
