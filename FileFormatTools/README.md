# CSV/TSV to BOM-Added CSV/XLSX Converter

このスクリプトは CSV または TSV（タブ区切りテキスト）ファイルを入力として、BOM（バイトオーダーマーク）付きの CSV および XLSX（Excel）ファイルを /output に出力します。

## 主な機能

- 入力された CSV/TSV ファイルのエンコーディングを自動で判別。
- BOM が既に付与されているかどうかを確認。
- BOM を追加した CSV ファイルを出力。
- Excel がサポートしていない特殊文字を削除した XLSX ファイルを出力。
- 出力された CSV と XLSX の行数を確認。

## 使用方法

コマンドラインから以下のように実行します。

```
python csv_tsv_to_bom_xlsx_converter.py [input.csv or input.tsv]
```

### 引数:

- `input.csv or input.tsv`: 変換したい CSV または TSV ファイルの名前。

### 出力:

- BOM 付きの CSV ファイル
- 特殊文字を削除した XLSX ファイル

## 注意事項

- 入力ファイルの形式は CSV または TSV でなければなりません。
- ファイルが大きい場合、処理に時間がかかる可能性があります。

## エラーメッセージとトラブルシューティング

- `使用法: python csv_tsv_to_bom_xlsx_converter.py input.csv or input.tsv`: コマンドライン引数が不正または存在しない場合。
- `ファイル形式はcsvまたはtsvでなければなりません。`: 入力ファイルが CSV または TSV 形式でない場合。
- `警告: CSVのレコード数とXLSXの行数が一致していません！`: 出力された CSV と XLSX の行数が一致しない場合。この場合、データの整合性を確認してください。
