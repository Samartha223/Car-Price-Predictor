from flask import Flask,render_template,request
import pandas as pd
import pickle


app=Flask(__name__)

model=pickle.load(open("LRegression_car.pkl",'rb'))
car=pd.read_csv('car_dataset_cleaned.csv')
@app.route('/')
def index():
    companies=sorted(car['company'].unique())
    models=sorted(car['name'].unique())
    year=sorted(car['year'].unique(),reverse=True)
    fuel=sorted(car['fuel_type'].unique())
    return render_template('index.html',companies=companies,models=models,years=year,fuels=fuel)

@app.route('/predict', methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('model')   # renamed to avoid conflict
    year = int(request.form.get('year'))
    fuel = request.form.get('fuel')
    kms = float(request.form.get('kms'))

    # Make prediction
    prediction = model.predict(pd.DataFrame([[company, car_model, year, fuel, kms]],
                                            columns=['company','name','year','fuel_type','kms_driven']))
    output = round(prediction[0], 2)

    return render_template('index.html',
                           companies=sorted(car['company'].unique()),
                           models=sorted(car['name'].unique()),
                           years=sorted(car['year'].unique(), reverse=True),
                           fuels=sorted(car['fuel_type'].unique()),
                           prediction_text=f"The estimated price of the car is Rs. {output}",
                           selected_company=company,
                           selected_model=car_model,
                           selected_year=year,
                           selected_fuel=fuel, 
                           selected_kms=kms)
                        
                            


if __name__=='__main__':
    app.run(debug=True)