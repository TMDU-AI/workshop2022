# 肺のレントゲンで深層学習
#1) 必要なライブラリの読み込み
import os
import numpy as np
import random
import matplotlib.pyplot as plt
#日本語表示用
from matplotlib import rcParams
rcParams['font.family'] ='sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'IPAexGothic', 'IPAexMincho']

# AIのモジュールを取り込む
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Flatten,Dense,Dropout

# 以下のコードは本来必要ないが、anacondaでのOMP Abort エラーを防ぐために入れた
os.environ['KMP_DUPLICATE_LIB_OK']='True'

# 2) 画像を試しに取り出してみる
test = load_img('./test.jpg', color_mode='rgb')
plt.imshow(test)
plt.show()
print(test)

test2 = load_img('./test.jpg', color_mode='rgb',target_size=(10,10))
plt.imshow(test2)
plt.show()
print(test2)

test2_img = img_to_array(test2)
print(test2_img)
print(test2_img.shape)

test3 = load_img('./test.jpg',color_mode='grayscale',target_size=(10,10))
plt.imshow(test3)
plt.gray()
plt.show()
print(test3)
test3_img = img_to_array(test3)
print(test3_img)
print(test3_img.shape)

print(test3_img[0])
print(test3_img[0][0])

#3)実際の画像を読み込み加工する
#画像ファイル名取得
list_healthy = [i for i in os.listdir('./COVID-NORMAL/healthy') if not i.startswith('.')]
list_covid19 = [i for i in os.listdir('./COVID-NORMAL/covid19') if not i.startswith('.')]
print(list_healthy)
print(list_covid19)

#画像ファイル数
number_of_healthy = len(list_healthy)
number_of_covid19 = len(list_covid19)
number_of_total = number_of_healthy  + number_of_covid19

#データ保管用numpy行列を定義

images_train = np.zeros((number_of_total, 64, 64, 1), dtype=float) #画像 64×64 白黒 0-1浮動小数点
labels_train = np.zeros((number_of_total, 1), dtype=int) #ラベル 0：正常 1:COVID19
print(images_train)
print(images_train.shape)

#画像ファイル取り込み
for i in range(0, number_of_healthy):
    filepath = './COVID-NORMAL/healthy/%s' %list_healthy[i]
    temp = load_img(filepath, color_mode='grayscale', target_size=(64,64), interpolation='lanczos' )
    images_train[i] = img_to_array(temp) / 255.0
    labels_train[i] = 0
for i in range(0, number_of_covid19):
    filepath = './COVID-NORMAL/covid19/%s' %list_covid19[i]
    temp = load_img(filepath, color_mode='grayscale', target_size=(64,64), interpolation='lanczos' )
    images_train[i + number_of_healthy] = img_to_array(temp) / 255.0
    labels_train[i + number_of_healthy] = 1
"""
num_list = np.random.permutation(number_of_total)
print(num_list)
images_train2 = images_train[num_list]
labels_train2 = labels_train[num_list]
print(images_train2)
print(labels_train2)
"""

num_list = np.arange(number_of_total)
np.random.shuffle(num_list)
images_train2 = images_train[num_list]
labels_train2 = labels_train[num_list]
print(images_train2)
print(labels_train2)


#4) データの確認
print(images_train)
print(labels_train)
print(images_train.shape)
print(labels_train.shape)

#5) 神経回路の作成
model = Sequential()
model.add(Flatten(input_shape=(64, 64, 1)))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='Adam', metrics=["accuracy"])
model.summary()

#6) 学習実行　epoch数を繰り返す　2割は検証用に用い学習には使わない
result = model.fit(images_train2, labels_train2, batch_size = 64, epochs = 100, validation_split = 0.2)


#7) 学習過程をグラフ表示する

# Loss(正解との誤差)をloss_valuesに入れる
loss = result.history['loss']
val_loss = result.history['val_loss']
# 正確度をaccに入れる
acc = result.history['accuracy']
val_acc = result.history['val_accuracy']
# 1からepoch数までのリストを作る
epochlist = range(1, len(loss) +1)
#  正確度のグラフを作る
# 'b'は青い線
plt.plot(epochlist, acc, 'bo', label='Accuracy at training')
plt.plot(epochlist, val_acc, 'b', label='Accuracy at validation')
#  Loss(正解との誤差)のグラフを作る
# 'ro'は赤い点  https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
plt.plot(epochlist, loss, 'ro', label='Loss at training')
plt.plot(epochlist, val_loss, 'r', label='Loss at validation')
#  タイトル
plt.title('学習回数と誤差')
plt.ylabel('点は学習、線は検証、赤は損失、青は正解率')
plt.xlabel('学習回数(epoch数)')
plt.legend()
plt.show()

#8) 新たな画像で分類する
img1 = img_to_array(load_img('./covid.jpg', color_mode='grayscale',target_size=(64,64)))/255
img2 = img_to_array(load_img('./NORMAL.jpg', color_mode='grayscale',target_size=(64,64)))/255
check = np.zeros((2,64,64,1))
check[0] = img1
check[1] = img2
myprobs = model.predict(check)
print(myprobs)
print('%.5f' %myprobs[0])
print('%.5f' %myprobs[1])

