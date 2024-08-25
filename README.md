
# Cars Price Prediction

Description: This project is designed to predict the prices of used cars in Kyrgyzstan. It analyzes various car characteristics and provides a price forecast for the next year, taking into account inflation and market changes.

## Features

- Price prediction based on various car characteristics such as model name, car manufacturer, year of manufacture, car price, mileage, fuel type, and color.
- Data updating to account for inflation and market changes.
- An interface for inputting car data and obtaining a price forecast for the next year.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/kelsinbek/CarsPricePrediction.git
cd CarsPricePrediction
```

### 2. Create a virtual environment

```bash
python -m venv venv
```
  - Activate the virtual environment
  - On Windows
   ```bash
   venv\Scripts\activate
   ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```
Open your browser and go to http://localhost:8080/ to view the web application.

## Usage
On the main page of the application, you can enter the following car characteristics:

- **Model Name**: The model name of the car.
- **Manufacturer**: The manufacturer of the car.
- **Year of Manufacture**: The year the car was made.
- **Car Price**: The price of the car at the time of sale.
- **Mileage**: The car's mileage in kilometers.
- **Fuel Type**: The type of fuel (e.g., gasoline, diesel).
- **Color**: The color of the car.

After entering the data, click the button to get a price forecast for the next year.

![Alt text](documentation/screen.png)

## Project Structure

- CarsPricePrediction/
- │
- ├── dataset/
- │   ├── cars.csv
- │   └── _cleaned_data_cars.csv
- ├── documentation/
- ├── static/
- │   ├── css/
- │   │   └── style.css
- │   └── image/
- │       └── car_img.jpg
- ├── templates/
- │   └── index.html
- ├── analyse_cars.ipynb
- ├── LinearRegressionModel.pkl
- ├── main.py
- ├── RandomForestRegression.pkl
- ├── requirements.txt
- └── README.md
