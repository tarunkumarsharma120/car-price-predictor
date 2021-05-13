from flask import Flask,render_template
import pandas as pd
app=Flask(__name__)
car=pd.read_csv('fullclear_car.csv')
@app.route('/')

def index():
    companies=sorted(car['company'].unique())
    car_models=sorted(car['names'].unique())
    year=sorted(car['years'].unique())
    fuel_type=sorted(car['fuel_type'].unique())

    return render_template('index.html',companies=companies,car_models=car_models,year=year,fuel_type=fuel_type)
app.run(debug=True)
