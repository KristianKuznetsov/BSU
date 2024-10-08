import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Задача 3

# Генерация случайных данных
data = np.array([5.2, 3.1, 5.5, 6.2, 5.4, 4.0, 5.2, 4.4, 5.7, 4.8, 3.6, 6.0, 3.1, 5.0, 2.9, 1.2, 2.1, 3.8, 2.4, 1.1, 1.0, 2.3, 1.5, 1.2, 3.4, 3.4, 3.3, 7.0, 2.0, 4.6, 3.0, 1.3, 1.5, 0.8, 2.5, 1.5, 1.8, 1.4, 0.9, 1.7, 5.4, 2.4, 2.3, 2.7, 1.2, 1.0, 3.6, 3.9, 3.2, 2.3, 0.8, 1.5, 2.8, 3.4, 3.5, 0.9, 3.5, 1.6, 4.1, 2.6, 2.3, 2.4, 3.7, 2.2, 2.1, 2.6, 4.0, 2.5, 2.0, 2.8, 2.3, 2.3, 2.3, 2.9, 1.9, 1.5, 2.4, 1.3, 1.8, 2.0, 2.3, 1.7, 1.8, 1.9, 1.8, 0.8, 1.6, 3.2, 4.3, 2.9, 2.8, 0.9, 1.2, 2.2, 1.1, 2.5, 2.4, 3.5, 7.3, 4.4, 9.9, 6.2, 8.8, 2.7, 4.1, 2.5, 3.0, 0.7, 2.5, 0.8, 1.6, 1.8, 1.2, 0.6, 1.0, 0.9, 1.7, 1.2, 1.0, 1.8, 0.6, 1.4, 0.9, 0.9, 0.7, 0.9, 1.1, 1.0, 0.9, 2.0, 1.1, 2.5, 1.6, 0.5, 1.6, 1.2, 1.7, 1.7, 0.5, 1.4, 1.4, 1.5, 1.4, 1.5, 1.0, 0.9, 0.8, 1.2, 1.0, 0.8, 0.9, 1.1, 1.6, 1.8, 1.0, 2.2, 1.0, 1.2, 1.2, 1.2, 1.1, 2.5, 2.4, 1.5, 1.3, 1.0, 0.7, 1.0, 1.4, 2.0, 1.0, 1.5, 1.2, 0.7, 1.3, 2.0, 1.8, 2.0, 1.3, 2.2, 1.6, 1.4, 0.7, 1.2, 0.9, 1.4, 1.1, 0.9, 1.0, 0.9, 1.0, 1.7, 1.2, 1.2, 1.3, 1.2, 0.8, 0.2, 1.2, 0.3, 0.9, 1.4, 0.8, 0.3, 1.0, 0.9, 0.7, 1.8, 1.8, 2.4, 2.5, 1.5, 1.1, 1.0, 1.3, 3.5, 2.3, 0.3, 0.6, 0.4, 0.8, 1.2, 1.2, 0.8, 0.4, 1.3, 1.8, 1.6, 0.8, 0.8, 0.5, 0.7, 1.2, 1.0, 2.3, 0.3, 1.5, 2.6, 2.4, 3.1, 1.9, 2.2, 1.4, 1.5, 2.3, 0.8, 1.1, 2.9, 0.8, 1.8, 2.2, 1.4, 1.3, 1.2, 1.1, 1.8, 1.1, 1.2, 1.4, 1.1, 0.8, 2.3, 1.9, 0.8, 2.1, 1.0, 1.1, 0.9, 1.3, 2.5, 2.6, 2.1, 1.8, 2.1, 1.4, 1.2, 1.1, 1.2, 1.2, 0.4, 1.6, 0.8, 1.0, 1.1, 2.3, 3.0, 3.0, 0.7, 4.0, 1.8, 1.3, 0.9, 0.5, 0.9, 0.5, 0.4, 2.4, 1.1, 0.7, 0.9, 1.1, 0.6, 1.3, 3.2, 1.6, 1.3, 1.0, 0.7, 0.9, 1.3, 0.8, 1.0, 1.1, 1.4, 1.5, 0.8, 1.0, 0.3, 0.4, 1.6, 0.8, 0.6, 1.5, 0.4, 0.8, 1.5, 0.9, 2.7, 7.2, 1.8, 0.6, 1.3, 3.3, 1.2, 1.5, 0.7, 1.2, 1.1, 2.9, 2.2, 1.2, 2.5, 2.9, 1.1, 2.3, 2.3, 1.8, 3.2, 4.1, 2.6, 1.5, 2.1, 4.4, 3.6, 3.0, 1.9, 1.2, 2.7, 1.6, 2.9, 1.3, 1.7, 1.4, 2.0, 1.4, 1.7, 0.9, 1.2, 1.2, 1.2, 2.1, 2.0, 0.6, 1.0, 2.9, 1.0, 2.0, 1.2, 2.1, 2.0, 1.7, 2.3, 2.4, 1.6, 1.7, 0.9, 0.6, 1.5, 0.8, 1.4, 2.1, 0.8, 3.6, 2.9, 2.3, 1.7, 2.8, 1.8, 1.7, 3.4, 3.2, 1.9, 2.7, 1.9, 1.6, 1.6, 1.7, 1.4, 1.0, 1.9, 1.9, 2.8, 5.0])


# Построение boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(data=data)
plt.title('Диаграмма с усами (Boxplot)')
plt.ylabel('Значения')
plt.show()

#Задача 4

# Генерация второго набора данных
data2 = np.array([4.7, 5.8, 6.3, 4.1, 5.7, 1.0, 6.1, 3.0, 0.9, 0.8, 0.6, 0.4, 1.7, 2.7, 0.8, 0.7, 2.5, 1.1, 2.7, 0.6, 2.4, 0.4, 10.5, 5.6, 9.3, 4.8, 4.1, 0.3, 1.2, 0.7, 2.5, 0.7, 0.5, 2.4, 1.7, 1.6, 0.8, 1.1, 2.5, 2.5, 1.0, 0.8, 1.9, 2.4, 1.9, 3.2, 1.6, 4.6, 0.7, 2.3, 0.9, 2.3, 5.8, 1.5, 3.6, 1.0, 4.4, 2.0, 3.2, 5.8, 4.5, 3.5, 2.2, 1.4, 2.2, 3.0, 2.8, 3.0, 1.5, 3.0, 1.2, 0.8, 4.1, 1.2, 0.8, 6.3, 5.3, 4.5, 6.5, 4.5, 0.8, 1.2, 0.5, 0.6, 1.0, 1.3, 0.7, 0.3, 0.4, 0.6, 1.1, 1.3, 0.8, 1.3, 1.6, 1.1, 1.7, 1.1, 1.0, 1.6, 0.2, 0.1, 1.1, 0.5, 0.5, 1.0, 1.4, 0.6, 1.7, 1.9, 0.9, 0.9, 1.9, 1.3, 0.9, 0.9, 1.0, 0.9, 1.0, 1.6, 1.1, 1.1, 1.3, 0.6, 0.8, 4.4, 0.3, 0.2, 0.3, 1.8, 5.2, 1.5, 0.6, 0.5, 0.9, 1.1, 0.8, 0.6, 0.9, 0.8, 0.8, 0.7, 0.4, 0.9, 0.6, 1.5, 2.8, 2.3, 1.5, 1.3, 22.0, 18.4, 1.8, 0.5, 1.0, 0.6, 0.5, 8.3, 0.5, 2.1, 0.6, 0.7, 0.9, 24.5, 17.0, 18.0, 8.2, 0.7, 0.7, 0.3, 1.0, 0.3, 0.6, 0.5, 2.7, 18.5, 11.3, 15.8, 3.1, 0.7, 1.4, 1.0, 1.2, 1.1, 0.8, 0.9, 0.1, 1.0, 0.6, 0.9, 0.7, 1.7, 0.9, 0.9, 0.5, 0.2, 0.5, 0.5, 0.5, 0.5, 1.8, 1.5, 4.8, 0.9, 3.1, 2.8, 2.3, 0.9, 1.3, 6.2, 1.1, 1.1, 0.7, 4.3, 1.6, 1.7, 1.6, 0.7, 0.8, 1.5, 0.9, 0.6, 0.6, 0.5, 11.0, 1.9, 1.5, 1.9, 1.7, 2.5, 1.4, 0.8, 1.1, 0.4, 2.9, 1.7, 0.3, 0.9, 0.8, 0.9, 0.5, 1.1, 1.3, 0.9, 1.4, 1.0, 1.2, 1.3, 2.0, 1.4, 1.3, 1.3, 0.8, 0.9, 2.8, 2.9, 1.9, 2.5, 2.0, 1.1, 1.8, 0.9, 1.2, 0.8, 1.3, 0.6, 1.0, 0.9, 1.3, 0.5, 0.6, 1.2, 1.3, 1.2, 1.7, 0.8, 0.7, 0.2, 0.9, 1.5, 1.3, 1.6, 1.0, 0.9, 0.8, 0.4, 1.9, 1.3, 0.6, 0.6, 2.5, 0.8, 0.5, 0.5, 0.8, 0.4, 3.7, 3.9, 2.3, 2.4, 3.2, 1.5, 2.5, 3.9, 2.6, 3.9, 2.2, 1.3, 0.9, 1.3, 1.3, 2.2, 1.1, 2.0, 0.4, 0.8, 0.5, 0.7, 0.7, 2.9, 0.8, 0.4, 0.7, 0.9, 0.4, 2.2, 2.8, 3.5, 0.8, 3.6, 0.6, 1.2, 0.3, 0.8, 3.1, 0.6, 0.6, 0.3, 0.2, 1.2, 0.3, 1.1, 0.9, 1.3, 1.0, 1.0, 1.0, 1.3, 1.3, 0.8, 0.6, 1.0, 0.9, 1.8, 1.0, 0.7, 1.5, 0.6, 0.7, 0.6, 0.7, 0.8, 0.7, 1.2, 1.3, 2.5, 0.7, 0.9, 0.9, 0.4, 1.1, 0.8, 0.8, 1.3, 0.8, 1.7, 0.6, 3.7, 1.1, 3.0, 3.9, 2.5, 1.0, 0.6, 8.5, 17.7, 3.1, 5.4, 7.5, 1.6, 0.7, 0.6, 2.6, 2.8, 0.2, 4.3, 0.5, 0.6, 0.4, 0.7, 0.5, 0.4, 0.7, 1.2, 1.1, 1.5, 0.5, 0.7, 0.6, 1.1, 0.7, 2.9, 0.7, 1.6, 0.8, 1.7, 0.4, 1.2, 0.5, 0.6, 0.8, 0.8, 0.6, 0.8, 1.2, 0.7, 2.0, 0.6, 0.5, 2.4, 0.4, 2.2, 2.0, 3.6, 1.5, 0.6, 1.1, 1.0, 1.0, 0.3, 2.0, 3.2, 1.2, 1.1, 1.2, 3.1, 1.9, 1.1, 0.7, 1.3, 1.2, 1.0, 1.3, 1.0, 0.4, 1.1, 1.7, 2.0, 2.6, 2.2, 0.9, 0.9, 0.7, 1.5, 0.3, 1.4, 4.0, 3.3, 11.3, 6.8, 1.9, 0.6, 2.3, 1.3, 0.3, 1.3, 0.7, 1.1, 2.0, 0.8, 1.0, 1.1, 0.5, 0.7, 0.7, 1.2, 0.6, 1.1, 0.8, 0.7, 1.6, 0.1, 0.6, 0.3, 0.7, 0.1, 0.4, 0.6, 0.8, 0.4, 0.5, 0.8, 0.7, 1.0, 0.8, 0.3, 0.5, 1.0, 0.4, 0.7, 0.5, 0.7, 0.5, 0.4, 1.7, 0.7, 0.8, 0.7, 0.7, 0.5, 0.5, 1.7, 0.4, 0.3, 1.0, 1.3, 10.2, 10.1, 0.8])


# Построение boxplot для двух наборов данных
plt.figure(figsize=(8, 6))
sns.boxplot(data=[data, data2])
plt.title('Сравнение двух наборов данных (Boxplot)')
plt.xticks([0, 1], ['DB (карликовая берёза)', 'W (ива)'])
plt.ylabel('Значения')
plt.show()

#Задача 5

# Эмпирическая функция распределения
def empirical_cdf(data):
    x = np.sort(data)
    y = np.arange(1, len(data) + 1) / len(data)
    return x, y

# Построение ECDF
x, y = empirical_cdf(data)

plt.figure(figsize=(8, 6))
plt.step(x, y, label='Эмпирическая CDF', where='post')
plt.title('Эмпирическая функция распределения')
plt.xlabel('Значения')
plt.ylabel('CDF')
plt.grid()
plt.legend()
plt.show()


# Воспользуемся функцией из библиотеки
from statsmodels.distributions.empirical_distribution import ECDF

ecdf = ECDF(data)
plt.figure(figsize=(8, 6))
plt.step(ecdf.x, ecdf.y, label='ECDF (statsmodels)', where='post')
plt.title('Эмпирическая функция распределения (statsmodels)')
plt.xlabel('Значения')
plt.ylabel('CDF')
plt.grid()
plt.legend()
plt.show()

#Задача 6
import seaborn as sns

plt.figure(figsize=(8, 6))
sns.histplot(data, bins=30, kde=True, stat="probability")
plt.title('Гистограмма вероятностей с KDE')
plt.xlabel('Значения')
plt.ylabel('Вероятность')
plt.show()

#Задача 7

import scipy.stats as stats

plt.figure(figsize=(8, 6))
stats.probplot(data, dist="norm", plot=plt)
plt.title('QQ-Plot')
plt.xlabel('Квантиль теоретического распределения')
plt.ylabel('Квантиль выборки')
plt.grid()
plt.show()