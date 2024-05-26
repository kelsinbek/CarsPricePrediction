import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Пример данных
data = {
    "ID": [800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816],
    "name": ["Honda Fit"]*17,
    "company": ["Honda"]*17,
    "year": [2020, 2021, 2022, 2023, 2024, 2020, 2021, 2022, 2023, 2024, 2020, 2021, 2022, 2023, 2024, 2020, 2021],
    "price": np.random.randint(4000, 9001, size=17),
    "kms_driven": np.random.randint(100000, 350001, size=17),
    "fuel_type": ["Petrol"]*17,
    "sale_date": pd.date_range(start='2020-01-01', periods=17, freq='MS'),
    "color": np.random.choice(['Red', 'Blue', 'White', 'Black', 'Silver'], size=17),
    "volume": np.random.choice([1.3, 1.5, 1.6], size=17),
}

# Создание DataFrame
df = pd.DataFrame(data)

# Дополнительные данные для 500 строк
for i in range(17, 500):
    year = np.random.choice([2003, 2004, 2005, 2006, 2007])
    price = np.random.randint(4000, 9001)
    kms_driven = np.random.randint(100000, 350001)
    sale_date = (datetime(2020, 1, 1) + timedelta(days=np.random.randint(0, 365 * 4))).strftime("%Y-%m-%d")
    color = np.random.choice(['Red', 'Blue', 'White', 'Black', 'Silver'])
    volume = np.random.choice([1.3, 1.5, 1.6])
    df.loc[i] = [
        800 + i, "Honda Fit", "Honda", year,
        price, kms_driven, "Petrol",
        sale_date, color, volume
    ]

# Вывод данных
print(df[['ID', 'name', 'company', 'year', 'price', 'kms_driven', 'fuel_type', 'sale_date', 'color', 'volume']])

# Сохранение данных в CSV
df.to_csv('car_data_with_sales.csv', index=False)

print("Данные сохранены в 'car_data_with_sales.csv'")
