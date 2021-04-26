#NumPy　ナムパイ
import numpy as np
#浮動小数点の表示制度
np.set_printoptions(suppress=True, precision=4)

a = np.array([1,2,3,4,5,6,7])

b = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])


print(f'元の変数:{a}')

a_sum = np.sum(a)
print(f'和:{a_sum}')

a_mean = np.mean(a)
print(f'平均:{a_mean}')

a_max = np.max(a)
print(f'最大値:{a_max}')

a_min = a.min()
print(f'最小値:{a}')
