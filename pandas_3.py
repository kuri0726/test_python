import numpy as np
import pandas as pd
from IPython.display import display
pd.options.display.float_format = '{:.4f}'.format
pd.set_option("display.max_columns",None)
b = np.array([[1, 2, 1], [4, 5, 2], [7, 8, 2],
    [10,np.nan, 1], [13, 10, 2]])
df = pd.DataFrame(b, columns=['col_a', 'col_b', 'col_c'])



# 1次元NumPy配列の定義
a = np.array(['male', 'male', 'female', 'male', 'female'])

# 結果確認
print(a)

# Seriesの定義
ser = pd.Series(a, name='col_d')

print(type(ser))

print(ser)

# データフレームからSeriesを生成
ser2 = df['col_b']

print(type(ser2))

print(ser2)

# データフレームと2次元NumPy配列の関係

# データフレームから2次元NumPy配列を取得
ar = df.values

# 2次元NumPy配列からデータフレームを生成
df0 = pd.DataFrame(ar)

# データフレームのshapeとlen関数
# shapeとlen関数は、内部のNumPyの結果がそのまま返る

print(df.shape)
print(len(df))


# 列リストで部分表を抽出

cols = ['col_a', 'col_c']
df2 = df[cols]

display(df2)

# データフレームの特定列をNumPy配列として抽出

y = df['col_a'].values
print(y)


# head関数で行の範囲指定
display(df.head(2))

# 行の範囲を数値指定
display(df[0:2])

# idx:「col_aが奇数」を判定
idx = (df['col_a'] % 2 == 1)
print(idx)

# idx で行を絞り込む
df3 = df[idx]
display(df3)


# まとめて1行で表現
df4 = df[df['col_a'] % 2 == 1]
display(df4)

# 列削除
df5 = df.drop('col_a', axis=1)
display(df5)

# 欠損値のある行を削除
df6 = df.dropna(subset = ['col_b'])
display(df6)

# 列連結
df7 = pd.concat([df, ser], axis=1)
display(df7)

#  特定列に対する統計関数
a_mean = df['col_a'].mean()
a_max = df['col_a'].max()
a_min = df['col_a'].min()

print(f'平均: {a_mean}  最大:{a_max}  最小:{a_min}')

# データフレーム全体にmean関数呼び出し
print(df.mean())

# 項目ごとの統計情報取得
display(df.describe())

# 項目値の個数集計
df7['col_d'].value_counts()

# NULL値チェック
display(df.isnull())

# 列単位の欠損値集計
print(df.isnull().sum())

# groupby関数でcol_dの項目値ごとの集計
df8 = df7.groupby('col_d').mean()
display(df8)

# map関数でmale/femaleを1/0に置き換え
df9 = df7.copy()
mf_map = {'male': 1, 'female': 0}
df9['col_d'] = df9['col_d'].map(mf_map)
display(df9)
