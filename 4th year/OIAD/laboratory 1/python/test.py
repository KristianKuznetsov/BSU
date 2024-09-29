import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import levy
from scipy.stats import levy_stable

# Параметры устойчивого распределения
alpha = 1  # параметр стабильности (0 < alpha <= 2)
beta = 0.7   # асимметрия (−1 ≤ beta ≤ 1)
loc = 10      # сдвиг (location)
scale = 2    # масштаб (scale)
size = 413  # количество случайных чисел

# Генерация случайных чисел
data = levy_stable.rvs(alpha, beta, loc=loc, scale=scale, size=size)


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