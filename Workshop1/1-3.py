# 線形回帰

from sklearn.linear_model import LinearRegression
x = [[35],[21],[45],[58],[77]]
y = [3,0,6,8,13]
model = LinearRegression()
model.fit(x,y)
print(model.coef_)
print(model.intercept_)
test = [[70]]
num_teeth = model.predict(test)
print('70歳の時の本数は',num_teeth,'本')


# 回帰直線の作図

import matplotlib.pyplot as plt

plt.figure()
plt.title('年齢と歯周病の歯の本数',fontfamily='Meiryo')
plt.xlabel('年齢',fontfamily='Meiryo')
plt.ylabel('歯周病の歯の本数',fontfamily='Meiryo')
plt.grid(True)
plt.scatter(x,y)
plt.plot(x,model.predict(x))
plt.scatter(test,num_teeth)
plt.show()














