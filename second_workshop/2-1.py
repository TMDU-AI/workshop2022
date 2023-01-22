# ライブラリの読み込み

import pandas as pd

# pd.read_csv('ファイル名')でcsvファイルをpandasのデータフレームという型で読み込む
# データフレームは行列の形で扱うかとができる
iris = pd.read_csv('2.csv')

#　行の操作
# データフレーム[a:b]でa行目(以上)からb行目(未満)までを取り出す
a = iris[0:4]
print(a)
# データフレーム.shapeで行列(2次元配列)の形状を調べることが出来る
print(iris.shape)
print(a.shape)
# 列の操作
# 1列のみを取り出すにはデータフレーム[列の名前]で取り出す
b = iris['がく片の長さ']
print(b)
print(b.shape)
# 2列以上を取り出すにはデータフレーム[['列の名前','列の名前']]で取り出す
c = iris[['がく片の長さ','がく片の幅']]
print(c)
print(c.shape)
# データフレーム['列の名前']だと行列の形(2次元配列)ではなくなる
# 2次元配列として取り出すには1列のみ取り出すとしてもデータフレーム[['列の名前']]とする
d = iris[['がく片の長さ']]
print(d)
print(d.shape)

from sklearn.linear_model import LogisticRegression

df = iris[0:100]
x = df[['がく片の長さ']]
y = df['アヤメの種類_数字']
print(x)
print(y)

# xとyをnumpy配列にする
# そのままデータフレームの形でも学習できるが、次の予測(model.predict)の際にリストを入力すると警告が出る
# さらにtolist()でリストに変換してもよい
x2 = x.to_numpy()
y2 = y.to_numpy()

model2 = LogisticRegression()
model2.fit(x2,y2)

print(model2.coef_)
print(model2.intercept_)

test1 = [[4.5]]
test2 = [[5.0]]
test3 = [[7.0]]
result1 = model2.predict(test1)
result2 = model2.predict(test2)
result3 = model2.predict(test3)
print("がく片の長さが4.5の時の予測結果は:",result1)
print("がく片の長さが5.0の時の予測結果は:",result2)
print("がく片の長さが7.0の時の予測結果は:",result3)
test4 = [[4.5],[5.0],[7.0]]
result4 = model2.predict(test4)
print(result4)
print("がく片の長さが4.5の時の予測結果は:",result4[0])
print("がく片の長さが5.0の時の予測結果は:",result4[1])
print("がく片の長さが7.0の時の予測結果は:",result4[2])
result5 = model2.predict_proba(test4)
print(result5)
print("がく片の長さが4.5の時のヒオウギアヤメとブルーフラッグの確率は:",result5[0])
print("がく片の長さが5.0の時のヒオウギアヤメとブルーフラッグの確率は:",result5[1])
print("がく片の長さが7.0の時のヒオウギアヤメとブルーフラッグの確率は:",result5[2])


# がく片の長さとがく片の幅（説明変数２つ）

x = df[['がく片の長さ','がく片の幅']]
y = df['アヤメの種類_数字']

# xとyをnumpy配列にする
# そのままデータフレームの形でも学習できるが、次の予測(model.predict)の際にリストを入力すると警告が出る
# さらにtolist()でリストに変換してもよい
x2 = x.to_numpy()
y2 = y.to_numpy()

model2 = LogisticRegression()
model2.fit(x2,y2)

test = [[4.5,3.2],[6.0,2.5],[7.0,6.0]]
result = model2.predict_proba(test)
print(result)

# 深層学習
rand = df.sample(n=100,random_state=1)
rand_train = rand[0:80]
rand_test = rand[80:100]
x_train = rand_train[['がく片の長さ','がく片の幅','花びらの長さ','花びらの幅']]
y_train = rand_train['アヤメの種類_数字']
x_test = rand_test[['がく片の長さ','がく片の幅','花びらの長さ','花びらの幅']]
y_test = rand_test['アヤメの種類_数字']

x_train = x_train.to_numpy()
y_train = y_train.to_numpy()
x_test = x_test.to_numpy()
y_test = y_test.to_numpy()

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

dl_model = Sequential()
dl_model.add(Dense(4,activation='relu',input_shape=(4,)))
dl_model.add(Dense(4,activation='relu'))
dl_model.add(Dense(4,activation='relu'))
dl_model.add(Dense(1,activation='sigmoid'))
dl_model.compile(loss='binary_crossentropy',optimizer='Adam',metrics=['accuracy'])
dl_model.summary()

result = dl_model.fit(x_train,y_train,epochs=300)

score = dl_model.evaluate(x_test,y_test)
print(score)
print("testの誤差は：",score[0],"testの正解率は:",score[1])

# 学習結果の図示
import matplotlib.pyplot as plt

loss = result.history['loss']
acc = result.history['accuracy']
epochs = list(range(0,300))
plt.plot(epochs,loss,marker='.',label='loss')
plt.plot(epochs,acc,marker='.',label='accuracy')
plt.legend()
plt.show()

print(result.history['accuracy'])









