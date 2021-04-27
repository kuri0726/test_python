
# CSVファイルからの読み込み

# 読み込み元URL
csv_url = 'https://github.com/makaishi2/sample-data\
/raw/d2b5d7e7c3444d995a1fed5bdadf703709946c75/data/df-sample.csv'

# データ読み込み
df_csv = pd.read_csv(csv_url)

# 結果確認
display(df_csv)
