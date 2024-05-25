import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

df=pd.read_csv('dataset/car_sales_with_dates.csv')
# Преобразование столбца sale_date в формат datetime
df['sale_date'] = pd.to_datetime(df['sale_date'])

# Группировка данных по месяцам и вычисление средней цены
df['month'] = df['sale_date'].dt.to_period('M')
monthly_prices = df.groupby('month')['price'].mean()

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(monthly_prices.index.astype(str), monthly_prices.values, marker='o')
plt.title('Средняя цена на Honda Fit за последние 2 года')
plt.xlabel('Месяц')
plt.ylabel('Средняя цена ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
