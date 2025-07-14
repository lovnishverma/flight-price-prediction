from flask import *
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("flight.html")

@app.route("/flight", methods=["POST"])
def predict():
    try:
        airline = int(request.form.get("airline"))
        source_city = int(request.form.get("source_city"))
        departure_time = int(request.form.get("departure_time"))
        stops = int(request.form.get("stops"))
        arrival_time = int(request.form.get("arrival_time"))
        destination_city = int(request.form.get("destination_city"))
        classs = int(request.form.get("classs"))
    except ValueError:
        return render_template("flight.html", result="Invalid input! Please make sure all fields are filled correctly.")

    url = "fly1.csv"
    data = pd.read_csv(url)

    x = data[["airline", "source_city", "departure_time", "stops", "arrival_time", "destination_city", "classs"]]
    y = data["price"]

    model = RandomForestRegressor()
    model.fit(x, y)

    arr = model.predict([[airline, source_city, departure_time, stops, arrival_time, destination_city, classs]])
    return render_template("flight.html", result=arr[0])

if __name__ == '__main__':
    app.run()
