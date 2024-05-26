import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns



data = pd.read_csv('dataset/car_csv.csv')
print(data)

df = pd.DataFrame(data)


# Функция для применения инфляции
def apply_inflation(price, start_date, end_date, rate):
    years = (end_date - start_date).days / 365.25
    inflated_price = price * (1 + rate / 100) ** years
    return inflated_price


# Преобразование столбца sale_date в datetime
df['sale_date'] = pd.to_datetime(df['sale_date'])

# Создание новых признаков: year_sold, month_sold
df['year_sold'] = df['sale_date'].dt.year
df['month_sold'] = df['sale_date'].dt.month

# Выбор признаков для обучения модели
X = df[['year', 'kms_driven', 'year_sold', 'month_sold', 'volume']]
y = df['price']

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Добавление столбца sale_date в X_test
X_test['sale_date'] = pd.to_datetime('2024-05-26')  # Примерная текущая дата для прогноза

# Создание и обучение модели линейной регрессии
model = RandomForestRegressor(n_estimators=100, random_state=42)  # Можете настроить параметры
model.fit(X_train, y_train)

# Прогнозирование цен на тестовом наборе для оценки модели
y_pred = model.predict(X_test[['year', 'kms_driven', 'year_sold', 'month_sold', 'volume']])

# Оценка модели
r2 = r2_score(y_test, y_pred)
print(f"R^2 score: {r2}")


# Прогнозирование на год
def predict_price_for_year(model, X, inflation_rate):
    # Получаем последнюю дату продажи
    last_sale_date = X['sale_date'].max()

    # Определяем дату окончания прогноза (год вперед)
    end_date = last_sale_date + timedelta(days=365)

    # Создаем диапазон дат для прогноза
    date_range = pd.date_range(start=last_sale_date, end=end_date, freq='MS')

    # Создаем DataFrame для прогнозов
    X_pred = pd.DataFrame({'sale_date': date_range})

    # Копируем признаки из X, кроме 'sale_date'
    for col in X.columns:
        if col != 'sale_date':
            X_pred[col] = X[col].iloc[0]  # Используем первое значение для каждого признака

    # Создаем новые признаки year_sold и month_sold
    X_pred['year_sold'] = X_pred['sale_date'].dt.year
    X_pred['month_sold'] = X_pred['sale_date'].dt.month

    # Прогнозируем цены
    y_pred = model.predict(X_pred[['year', 'kms_driven', 'year_sold', 'month_sold', 'volume']])

    # Применяем инфляцию к прогнозным ценам
    for i in range(len(y_pred)):
        y_pred[i] = apply_inflation(y_pred[i], last_sale_date, date_range[i], inflation_rate)

    # Добавляем предсказанные цены в X_pred
    X_pred['predicted_price'] = y_pred

    return X_pred[['sale_date', 'predicted_price']]

predicted_prices = predict_price_for_year(model, X_test, 10)

print(predict_price_for_year(model,X_test,7))



