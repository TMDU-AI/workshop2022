# numpy


# numpyの配列を作るにはnp.arrayと書きます
import numpy as np
test = np.array([1,2,3,4,5])
test2 = [1,2,3,4,5]
print(test)
print(type(test))


test = test * 2
test2 = test2 * 2
print(test)
print(test2)
test = test + 2
print(test)
test2 = test2 + 2


# numpy配列の連続した配列(連番)を作るにはnp.arangeを使います
# np.arange(数字)で0から数字（未満)の要素を作ります
# a = np.arange(10)
# print(a)
# np.arange(始点,終点)で始点(以上)から終点(未満)までの要素を作ります
b = np.arange(3,8)
print(b)
# np.arange(始点,終点,間隔)で決めた間隔おきに要素を作ります
c = np.arange(1,15,2)
print(c)
d = np.arange(1,15,3)
print(d)

# 2次元配列は次のようにして作成します
e = np.array([[1,2,3],[4,5,6]])
print(e)
# np配列.shapeで配列の形状を調べる事ができます
print(e.shape)
# np配列.reshape()で形状を変えることが出来ます
f = e.reshape(3,2)
print(f)
print(f.shape)
g = e.reshape(6,1)
print(g)
print(g.shape)


# matplotlibの読み込み
import matplotlib.pyplot as plt
# xに年齢、yに歯周病の歯の本数を代入
x = [35,21,45,58,77]
y = [3,0,6,8,13]
# 図を作るという指示(図の枠を作成)
plt.figure()
# x軸にx,y軸にyをプロットするという指示
plt.scatter(x,y)
# 上記内容を表示するという指示
plt.show()


# グリッド線とx軸、y軸、図のタイトルを追加
import matplotlib.pyplot as plt
# xに年齢、yに歯周病の歯の本数を代入
x = [35,21,45,58,77]
y = [3,0,6,8,13]
plt.figure()
plt.scatter(x,y)
plt.title('age and number of teeth affected by periodontitis')
plt.xlabel('age')
plt.ylabel('number of teeth affected by periodontitis')
plt.grid(True)
plt.show()





# 日本語の表記を可能にする
import matplotlib.pyplot as plt
x = [35,21,45,58,77]
y = [3,0,6,8,13]
plt.figure()
plt.plot(x,y)
plt.title('年齢と歯周病の歯の本数',fontfamily='Meiryo')
plt.xlabel('年齢',fontfamily='Hiragino Maru Gothic Pro')
plt.ylabel('歯周病の歯の本数',fontfamily='Hiragino Maru Gothic Pro')
plt.grid(True)
plt.show()


import matplotlib.pyplot as plt
x = [35,21,45,58,77]
y = [3,0,6,8,13]
plt.figure()
plt.scatter(x,y)
plt.title('年齢と歯周病の歯の本数',fontfamily='MS Gothic')
plt.xlabel('年齢',fontfamily='MS Gothic')
plt.ylabel('歯周病の歯の本数',fontfamily='MS Gothic')
plt.grid(True)
plt.show()







