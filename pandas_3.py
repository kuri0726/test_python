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
