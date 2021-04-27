#pandas パンダス



# CSVファイルからの読み込み

# 読み込み元URL
csv_url = 'https://github.com/makaishi2/sample-data\
/raw/d2b5d7e7c3444d995a1fed5bdadf703709946c75/data/df-sample.csv'

# データ読み込み
df_csv = pd.read_csv(csv_url)

# 結果確認
display(df_csv)

# ファイル読み込み後の列名変更
columns = ['A列', 'B列', 'C列']
df_csv.columns = columns

# 結果確認
display(df_csv)



# Excelファイルからの読み込み

# 読み込み元URL
excel_url = 'https://github.com/makaishi2/sample-data\
/raw/d2b5d7e7c3444d995a1fed5bdadf703709946c75/data/df-sample.xlsx'

# データ読み込み
df_excel = pd.read_excel(excel_url)

# 結果確認
display(df_excel)

