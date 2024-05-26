import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных из CSV файла
df = pd.read_csv('car_data_with_sales.csv.csv')

# Преобразование столбца sale_date в формат даты
df['sale_date'] = pd.to_datetime(df['sale_date'], errors='coerce')

# Удаление строк с некорректными значениями в столбце sale_date
df = df.dropna(subset=['sale_date'])

# Фильтрация данных за последние 4 года
start_date = pd.Timestamp('2020-01-01')
end_date = pd.Timestamp('2024-12-31')
filtered_df = df[(df['sale_date'] >= start_date) & (df['sale_date'] <= end_date)]

# Создание столбца "год продажи" для группировки
filtered_df['sale_year'] = filtered_df['sale_date'].dt.year

# Вычисление среднего значения цены за каждый год
avg_price_per_year = filtered_df.groupby('sale_year')['price'].mean().reset_index()

# Построение графика
plt.figure(figsize=(10, 6))
sns.lineplot(data=avg_price_per_year, x='sale_year', y='price', marker='o')

# Настройка графика
plt.title('Средняя цена автомобилей за последние 4 года ')
plt.xlabel('Год продажи')
plt.ylabel('Средняя цена ($)')
plt.grid(True)

# Показать график
plt.show()
