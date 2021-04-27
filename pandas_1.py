#pandas パンダス
import numpy as np
import pandas as pd

#データフレーム表示用関数
from IPython.display import display
#データフレームでの表示制度　小数点4桁まで表示
pd.options.display.float_format = '{:.4f}'.format
#データフレームですべての項目を表示
pd.set_option("display.max_columns",None)

b = np.array([[1,2,1],[4,5,2],[7,8,2],[10,np.nan,1],[13,10,2]])
print(b)

#データフレームの定義
df = pd.DataFrame(b, columns=['col_a','col_b','col_c'])

#型表示
print(type(df))
#display関数による整形表示
display(df)
