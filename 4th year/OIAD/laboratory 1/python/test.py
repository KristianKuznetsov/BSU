import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import levy
from scipy.stats import levy_stable

#данные для оценки
data = np.array([5.2, 3.1, 5.5, 6.2, 5.4, 4.0, 5.2, 4.4, 5.7, 4.8, 3.6, 6.0, 3.1, 5.0, 2.9, 1.2, 2.1, 3.8, 2.4, 1.1, 1.0, 2.3, 1.5, 1.2, 3.4, 3.4, 3.3, 7.0, 2.0, 4.6, 3.0, 1.3, 1.5, 0.8, 2.5, 1.5, 1.8, 1.4, 0.9, 1.7, 5.4, 2.4, 2.3, 2.7, 1.2, 1.0, 3.6, 3.9, 3.2, 2.3, 0.8, 1.5, 2.8, 3.4, 3.5, 0.9, 3.5, 1.6, 4.1, 2.6, 2.3, 2.4, 3.7, 2.2, 2.1, 2.6, 4.0, 2.5, 2.0, 2.8, 2.3, 2.3, 2.3, 2.9, 1.9, 1.5, 2.4, 1.3, 1.8, 2.0, 2.3, 1.7, 1.8, 1.9, 1.8, 0.8, 1.6, 3.2, 4.3, 2.9, 2.8, 0.9, 1.2, 2.2, 1.1, 2.5, 2.4, 3.5, 7.3, 4.4, 9.9, 6.2, 8.8, 2.7, 4.1, 2.5, 3.0, 0.7, 2.5, 0.8, 1.6, 1.8, 1.2, 0.6, 1.0, 0.9, 1.7, 1.2, 1.0, 1.8, 0.6, 1.4, 0.9, 0.9, 0.7, 0.9, 1.1, 1.0, 0.9, 2.0, 1.1, 2.5, 1.6, 0.5, 1.6, 1.2, 1.7, 1.7, 0.5, 1.4, 1.4, 1.5, 1.4, 1.5, 1.0, 0.9, 0.8, 1.2, 1.0, 0.8, 0.9, 1.1, 1.6, 1.8, 1.0, 2.2, 1.0, 1.2, 1.2, 1.2, 1.1, 2.5, 2.4, 1.5, 1.3, 1.0, 0.7, 1.0, 1.4, 2.0, 1.0, 1.5, 1.2, 0.7, 1.3, 2.0, 1.8, 2.0, 1.3, 2.2, 1.6, 1.4, 0.7, 1.2, 0.9, 1.4, 1.1, 0.9, 1.0, 0.9, 1.0, 1.7, 1.2, 1.2, 1.3, 1.2, 0.8, 0.2, 1.2, 0.3, 0.9, 1.4, 0.8, 0.3, 1.0, 0.9, 0.7, 1.8, 1.8, 2.4, 2.5, 1.5, 1.1, 1.0, 1.3, 3.5, 2.3, 0.3, 0.6, 0.4, 0.8, 1.2, 1.2, 0.8, 0.4, 1.3, 1.8, 1.6, 0.8, 0.8, 0.5, 0.7, 1.2, 1.0, 2.3, 0.3, 1.5, 2.6, 2.4, 3.1, 1.9, 2.2, 1.4, 1.5, 2.3, 0.8, 1.1, 2.9, 0.8, 1.8, 2.2, 1.4, 1.3, 1.2, 1.1, 1.8, 1.1, 1.2, 1.4, 1.1, 0.8, 2.3, 1.9, 0.8, 2.1, 1.0, 1.1, 0.9, 1.3, 2.5, 2.6, 2.1, 1.8, 2.1, 1.4, 1.2, 1.1, 1.2, 1.2, 0.4, 1.6, 0.8, 1.0, 1.1, 2.3, 3.0, 3.0, 0.7, 4.0, 1.8, 1.3, 0.9, 0.5, 0.9, 0.5, 0.4, 2.4, 1.1, 0.7, 0.9, 1.1, 0.6, 1.3, 3.2, 1.6, 1.3, 1.0, 0.7, 0.9, 1.3, 0.8, 1.0, 1.1, 1.4, 1.5, 0.8, 1.0, 0.3, 0.4, 1.6, 0.8, 0.6, 1.5, 0.4, 0.8, 1.5, 0.9, 2.7, 7.2, 1.8, 0.6, 1.3, 3.3, 1.2, 1.5, 0.7, 1.2, 1.1, 2.9, 2.2, 1.2, 2.5, 2.9, 1.1, 2.3, 2.3, 1.8, 3.2, 4.1, 2.6, 1.5, 2.1, 4.4, 3.6, 3.0, 1.9, 1.2, 2.7, 1.6, 2.9, 1.3, 1.7, 1.4, 2.0, 1.4, 1.7, 0.9, 1.2, 1.2, 1.2, 2.1, 2.0, 0.6, 1.0, 2.9, 1.0, 2.0, 1.2, 2.1, 2.0, 1.7, 2.3, 2.4, 1.6, 1.7, 0.9, 0.6, 1.5, 0.8, 1.4, 2.1, 0.8, 3.6, 2.9, 2.3, 1.7, 2.8, 1.8, 1.7, 3.4, 3.2, 1.9, 2.7, 1.9, 1.6, 1.6, 1.7, 1.4, 1.0, 1.9, 1.9, 2.8, 5.0])

# Параметры устойчивого распределения
params = stats.levy_stable.fit(data)
alpha_est, beta_est, location_est, scale_est = params

# Вывод оцененных параметров
print(f"Оцененные параметры:")
print(f"Alpha: {alpha_est:.4f}")
print(f"Beta: {beta_est:.4f}")
print(f"Location: {location_est:.4f}")
print(f"Scale: {scale_est:.4f}")

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
