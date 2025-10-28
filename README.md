"# Car-Price-Predictor" 
🚗 Car Price Prediction Web App
📖 Project Description

This project is a machine learning–powered web application that predicts the estimated price of a used car based on user inputs such as company, model, year of manufacture, fuel type, and kilometers driven.
The application is built using Flask (Python) for the backend and HTML, CSS, and JavaScript for the frontend. It features dynamic dropdown filters, where selecting a car company automatically filters the models that belong to that company.
Users can enter their car details, and the app displays both the predicted price and a summary of all the selected features.

⚙️ Tech Stack
Python (Flask) – Backend framework
Pandas, Scikit-learn – Data handling and model prediction
HTML, CSS, JavaScript (Jinja2) – Frontend and template rendering
Bootstrap – Styling and responsive UI
Pickle – Model serialization
CSV Dataset – Cleaned dataset of used cars

💡 Key Features
✅ Machine learning model trained to predict car prices
✅ Flask-based web application with form handling
✅ Dynamic dropdown: car models filtered by selected company
✅ Displays all selected inputs with the predicted result
✅ Easy to use and extend with any regression model

🧠 How It Works
User selects:
Car company
Car model
Year of manufacture
Fuel type
Kilometers driven
The app sends these inputs to the Flask backend.
The trained regression model predicts the estimated price.
The result and all selected features are displayed neatly on the web page.

🧩 Project Structure
Car_Price_Prediction/
│
├── app.py                     # Flask backend
├── LReression_car.pkl         # Trained ML model (pickle file)
├── car_dataset_cleaned.csv    # Dataset used for training
├── templates/
│   └── index.html             # Frontend HTML template
├── static/                    # (Optional) CSS or JS files
└── README.md                  # Project description

🚀 How to Run the Project Locally
1. Clone the Repository
git clone https://github.com/yourusername/car-price-prediction.git
cd car-price-prediction

2. Install Dependencies
pip install flask pandas scikit-learn

3. Run the Application
python app.py

4. Open in Browser

Go to → http://127.0.0.1:5000/

📊 Example Output
After entering the details:

Company: Hyundai  
Model: Hyundai Santro Xing  
Year: 2016  
Fuel Type: Petrol  
KMs Driven: 45,000  


The app  displays:

💰 Estimated Price: Rs. 3.45 Lakhs

🧠 Future Improvements
Add visualizations for price trends by brand or year
Improve model accuracy with feature engineering

Add authentication for saving user history
Deploy on Render, Heroku, or AWS
