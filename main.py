import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#не забудьте скачать все библиотеки (в том числе scipy)

df = pd.read_csv('LINK', header=None)
df
# Вместо зеленой ссылки вставить ту, которая будет у вас на зачете. Скопировать ее через правую кнопку мыши, "скопировать адрес ссылки"


#первое задание
x = df.mean() #среднее значение (х с чертой)
print("X", x)
S = df.var(ddof=1) #S_0^2
print("S", S)


#второе задание
hist = plt.hist(df[0], bins=10) #bins - количество интервалов в гистограмме. проверьте сколько сказано у вас и запишите число вместо 10
plt.show()
print(hist) #смотрите на первый array, берете числа для количества элементов выборки оттуда


#третье задание
theta_1 = df.mean() #если будет нормальное, первое значение
print("theta1", theta_1)

theta_2 = df.var(ddof=1) #если будет нормальное, второе значение
print("theta2", theta_2)

lambd = 1/df.mean() #если будет показательное, то записываете это значение в качестве значения оценки первого параметра
print("lambda", lambd)

min = df.min() #если будет равномерное, первое значение
print("min", min)

max = df.max() #если будет равномерное, второе значение
print("max", max)


#четвертое задание (сделано только для нормального распределения)
from scipy.stats import chi2, t
int1 = df.mean() - t.ppf(1 - 0.05/2, len(df) - 1) * (df.var(ddof=1) ** 0.5)/((len(df) ** 0.5)) #если нормальное и нужна левая граница(-). Если правая, то + вместо - после def.mean
print("int1", int1)
int2 = np.sum((df - df.mean()) ** 2)/chi2.ppf(0.05/2, len(df) - 1) #если нормальное и нужна правая граница(+). Если левая, то 1-0.05/2 вместо 0.05/2
print("int2", int2)

