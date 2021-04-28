
# 共通事前処理

# 余分なワーニングを非表示にする
import warnings
warnings.filterwarnings('ignore')

# 必要ライブラリのimport
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# matplotlib日本語化対応
import japanize_matplotlib

# データフレーム表示用関数
from IPython.display import display

# グラフのデフォルトフォント指定
plt.rcParams["font.size"] = 14

# データ準備
import seaborn as sns
df_iris = sns.load_dataset("iris") 

# 結果確認
display(df_iris.head())

# 散布図x座標用Series
xs = df_iris['sepal_length']

# 散布図y座標用Series
ys = df_iris['sepal_width']


# サイズ設定
plt.rcParams['figure.figsize'] = (6, 6)

# 散布図
plt.scatter(xs, ys)

# 描画
plt.show()

# データ準備

# シグモイド関数の定義
def sigmoid(x, a):
    return 1/(1 + np.exp(-a*x))

# グラフ描画用x座標リスト
xp = np.linspace(-3, 3, 61)


# サイズ設定
plt.rcParams['figure.figsize'] = (6, 6)

# グラフ描画
plt.plot(xp, sigmoid(xp, 1.0))

# 描画
plt.show()
