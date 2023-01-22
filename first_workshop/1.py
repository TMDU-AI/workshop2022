# ←先頭にシャープをつけるとコメントとなりその行はプログラムに反映されません。
'''
上下を('）3つで囲んだ中の文章もコメントとなります。
    
'''

# xという変数名に35という値を代入
x = 35
# xの中身を出力する(コンソールに中身が出力される)
print(x)

# 変数の名前は自分で好きに決めることが出来ます
data = 35
print(data)
data = 45
print(data)
data = 'こんにちは'
print(data)


# 変数名ageに自分の年齢をいれて出力してみましょう
age = 37
print(age)


# 四則演算
# 足し算は+、引き算は-、掛け算は*、割り算は/で行うことが出来ます
# 二乗はアスタリスク2個で**です
a = 5 + 5 - 3
print(a)
b = 10 / 2 * 3
print(b)
c = a * b
print(c)
print(100 * 100)
print(2**3)

# 身長と体重を変数に代入してBMIを計算する式を作ってみましょう

weight = 62
height = 1.68
BMI = weight / (height ** 2)
print(BMI)


'''
(補足)
print(2**2*3) # 12
# **(2乗が先に計算される)ので下のは64ではなく16になる
print(2*2**3) # 16
print((2*2)**3) # 64
'''

# pythonのデータには型という概念があります
# データの型はtype()で調べる事ができます。
x = 35
print(type(x))
x = 3.5
print(type(x))
data = '文字だよ'
print(type(data))

# リストの作成
# リストは変数名=[要素,要素,要素,...]で作ることができます

x = [1,2,3,4,5]
print(x)
print(type(x))
print(x[0])
print(x[4])
x[0] = 10
print(x)

print(len(x))
print(max(x))
print(min(x))
print(sum(x))




