from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

# Load data once when the app starts, not on every request
DATA_PATH = "fly1.csv"
data = pd.read_csv(DATA_PATH)

X = data[["airline", "source_city", "departure_time", "stops", "arrival_time", "destination_city", "classs"]]
y = data["price"]

# Train model only once
model = RandomForestRegressor(random_state=42)
model.fit(X, y)

@app.route('/')
def home():
    return render_template("flight.html", result=None)

@app.route("/flight", methods=["POST"])
def predict():
    try:
        # Fetch form inputs
        airline = int(request.form.get("airline"))
        source_city = int(request.form.get("source_city"))
        departure_time = int(request.form.get("departure_time"))
        stops = int(request.form.get("stops"))
        arrival_time = int(request.form.get("arrival_time"))
        destination_city = int(request.form.get("destination_city"))
        classs = int(request.form.get("classs"))

        # Perform prediction
        prediction = model.predict([[airline, source_city, departure_time, stops, arrival_time, destination_city, classs]])
        price = round(prediction[0], 2)

        return render_template("flight.html", result=f"Predicted Flight Price: ₹{price}")

    except (ValueError, TypeError):
        return render_template("flight.html", result="Invalid input! Please ensure all fields contain valid numeric values.")

if __name__ == '__main__':
    app.run(debug=True)
