from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
cors = CORS(app)
model = pickle.load(open('RandomForestRegressionModel.pkl', 'rb'))

car = pd.read_csv('dataset/_cleaned_data_cars.csv')


@app.route('/', methods=['GET', 'POST'])
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = car['fuel_type'].unique()
    colors = car['color'].unique()
    volumes = sorted(car['volume'].unique())

    companies.insert(0, 'Выбор бренда')
    return render_template('index.html', companies=companies,
                           car_models=car_models, years=year, fuel_types=fuel_type,
                           colors=colors, volumes=volumes)


@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    company = request.form.get('company')

    car_model = request.form.get('car_models')
    year = request.form.get('year')
    fuel_type = request.form.get('fuel_type')
    driven = request.form.get('kilo_driven')
    color = request.form.get('color')
    volume = request.form.get('volume')

    # Predict current price
    current_features = pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type', 'color', 'volume'],
                                    data=np.array([car_model, company, year, driven, fuel_type, color, volume]).reshape(
                                        1, 7))
    current_price = model.predict(current_features)[0]

    # Calculate future price
    future_kms_driven = int(driven) + 25000
    future_features = pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type', 'color', 'volume'],
                                   data=np.array(
                                       [car_model, company, year, future_kms_driven, fuel_type, color, volume]).reshape(
                                       1, 7))
    future_price_without_inflation = model.predict(future_features)[0]
    inflation_rate = 0.05
    future_price = future_price_without_inflation * (1 + inflation_rate)

    response = (f"Приблизительная текущая цена автомобиля: {current_price:.2f} $. "
                f"Прогнозируемая цена через год: {future_price:.2f} $.")

    return response



if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
