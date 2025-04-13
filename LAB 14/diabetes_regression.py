# diabetes_regression.py

from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics as mt
import numpy as np

# 1. Завантаження даних
diabetes = datasets.load_diabetes()
print("Опис датасету:")
print(diabetes.DESCR)

# 2. Підготовка даних
db_df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
db_df['Progression'] = diabetes.target

x = db_df.drop('Progression', axis=1)
y = db_df['Progression']

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.25, random_state=999)
print("Форма тренувальних та тестових вибірок:")
print("Train X:", train_x.shape, "| Test X:", test_x.shape)
print("Train Y:", train_y.shape, "| Test Y:", test_y.shape)

# 3. Створення моделі
lm = LinearRegression()
print("Модель створена:", lm)

# 4. Навчання моделі
lm.fit(train_x, train_y)
predicted_y = lm.predict(test_x)

# 5. Оцінка моделі
print("\nОцінка моделі:")
print("1) Explained Variance Score:", round(mt.explained_variance_score(test_y, predicted_y) * 100, 2), "%")
print("2) Mean Absolute Error:", round(mt.mean_absolute_error(test_y, predicted_y), 2))
print("3) R-Squared:", round(mt.r2_score(test_y, predicted_y), 2))
