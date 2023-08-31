import pandas as pd
import sys
import chardet
import openpyxl
import re
import os

if len(sys.argv) != 2:
    print("使用法: python csv_tsv_to_bom_xlsx_converter.py input.csv or input.tsv")
    sys.exit(1)

input_file = sys.argv[1]
file_extension = input_file.rsplit('.', 1)[1]
if file_extension not in ('csv', 'tsv'):
    print("ファイル形式はcsvまたはtsvでなければなりません。")
    sys.exit(1)

# 出力ディレクトリの設定
output_directory = "output/"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

csv_output_file = output_directory + input_file.rsplit('/', 1)[-1].rsplit('.', 1)[0] + "_bom.csv"
xlsx_output_file = output_directory + input_file.rsplit('/', 1)[-1].rsplit('.', 1)[0] + "_bom.xlsx"

# ファイルのエンコーディングを確認
with open(input_file, 'rb') as f:
    result = chardet.detect(f.read())
print(f"Detected encoding: {result['encoding']}")

# CSV/TSVファイルの読み込み
if file_extension == 'csv':
    df = pd.read_csv(input_file, dtype=str)
else:  # 'tsv'
    df = pd.read_csv(input_file, sep='\t', dtype=str)

# 読み込んだデータの行数を表示して確認
print(f"読み込んだデータの行数: {len(df)}")

# BOMがすでに付いているかどうかをチェック
with open(input_file, 'rb') as f:
    bom_check = f.read(3)
    has_bom = bom_check == b'\xef\xbb\xbf'

# BOM付きCSVファイルの書き込み
if not has_bom:
    with open(csv_output_file, 'w', encoding='utf-8-sig') as f:
        df.to_csv(f, index=False)
else:
    with open(csv_output_file, 'w', encoding='utf-8') as f:
        df.to_csv(f, index=False)

def remove_illegal_chars(val):
    if isinstance(val, str):
        # Excelがサポートしていない文字を削除
        return re.sub(r'[\000-\010]|[\013-\037]|[\177-\237]', '', val)
    else:
        return val

# データフレーム内の全ての文字列データに対して適用
df = df.applymap(remove_illegal_chars)

# XLSXファイルの書き込み
df.to_excel(xlsx_output_file, index=False)

# XLSXファイルの行数を取得
wb = openpyxl.load_workbook(xlsx_output_file)
sheet = wb.active
xlsx_row_count = sheet.max_row - 1  # ヘッダー行を除外

# CSVの実際のレコード数とXLSXの行数を比較
if len(df) != xlsx_row_count:
    print(f"警告: CSVのレコード数 ({len(df)}) とXLSXの行数 ({xlsx_row_count}) が一致していません！")
else:
    print(f"CSVのレコード数 ({len(df)}) とXLSXの行数 ({xlsx_row_count}) が一致しています。")

print(f"BOM付きファイルが作成されました: {csv_output_file}")
print(f"XLSXファイルが作成されました: {xlsx_output_file}")
