#NumPy　ナムパイ
import numpy as np
#浮動小数点の表示制度
np.set_printoptions(suppress=True, precision=4)

a = np.array([1,2,3,4,5,6,7])

b = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])

print(a)
print(b)

print(a.shape)
print(b.shape)

print(len(a))
print(len(b))

#特定列の抽出
c = b[:,0]
print(c)

#[0,1]列
d = b[:,:2]
print(d)

#reshape関数
l = np.array(range(12))
print(l)

#3行4列に変換
m = l.reshape(3,4)
print(m)
