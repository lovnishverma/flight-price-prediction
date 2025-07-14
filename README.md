# ✈️ Flight Fare Prediction (Machine Learning + Flask)

A **Machine Learning Web Application** built with **Flask** to predict flight fares based on user-selected options like airline, city, departure time, number of stops, class, etc.

This project demonstrates:

* End-to-end integration of **ML models** within a **Flask web app**.
* Clean and user-friendly **Bootstrap-based UI**.
* Use of **Random Forest Regressor** for prediction.

---

## 🚀 Live Demo

*(Optional: Add if hosted, otherwise remove this section)*
[https://your-live-demo-link.com](#)

---

## 📂 Project Structure

```
flight-price-prediction/
│
├── app.py                # Main Flask App
├── fly1.csv               # Dataset (Encoded CSV)
├── requirements.txt       # Python dependencies
│
├── templates/
│   └── flight.html        # Frontend HTML (Bootstrap + Styling)
│
└── static/
    └── style.css (optional) # You used inline CSS in flight.html
```

---

## 🛠️ Tech Stack

* **Python**
* **Flask**
* **Pandas**
* **Scikit-Learn**
* **HTML / CSS / Bootstrap 4**

---

## 📊 Dataset (fly1.csv)

Your dataset contains categorical numerical encodings:

| Column Name        | Description                     |
| ------------------ | ------------------------------- |
| `airline`          | Airline (Encoded ID)            |
| `source_city`      | Source City (Encoded ID)        |
| `departure_time`   | Departure Time (Encoded)        |
| `stops`            | Stops (Encoded)                 |
| `arrival_time`     | Arrival Time (Encoded)          |
| `destination_city` | Destination (Encoded)           |
| `classs`           | Class (1: Economy, 2: Business) |
| `price`            | Ticket Price (Target)           |

---

## 🔥 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/flight-price-prediction.git
cd flight-price-prediction
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask App

```bash
python app.py
```

Visit: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📷 Screenshots

| Home Page                                                        | Prediction Result                                                         |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------- |
| ![Home Page](https://via.placeholder.com/400x300?text=Home+Page) | ![Prediction](https://via.placeholder.com/400x300?text=Prediction+Result) |

---

## 📌 Sample Prediction Flow

1. Select **Airline**, **Source**, **Destination**, etc.
2. Submit the form.
3. App predicts & shows estimated fare in INR.

---

## 🛡️ Requirements (requirements.txt)

```txt
flask
pandas
scikit-learn
```

---

## 🧑‍💻 Author

**Lovnish Verma**
[GitHub](https://github.com/lovnishverma)

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and share.

---

# 🚀 Deployment Guide: Flask ML App on **Render.com**

---

## ✅ Prerequisites:

1. **Render Account**: Sign up at [https://render.com](https://render.com)
2. Your **project must be pushed to GitHub** (Public or Private).

---

## 📂 Recommended Project Structure (Render-friendly)

```
flight-price-prediction/
│
├── app.py
├── fly1.csv
├── requirements.txt
├── templates/
│   └── flight.html
├── static/
│   └── style.css (optional)
└── .render.yaml      <-- Important for auto-deployment (optional)
```

---

## 🔧 1️⃣ Ensure These Files Exist:

### `requirements.txt` ✅

```txt
flask
pandas
scikit-learn
```

### `.render.yaml` (Optional for automated deployment)

```yaml
services:
  - type: web
    name: flight-fare-app
    env: python
    buildCommand: ""
    startCommand: python app.py
    plan: free
```

---

## 📝 2️⃣ Update `app.py` for Production

Change:

```python
app.run(debug=True)
```

To:

```python
app.run(host='0.0.0.0', port=10000)
```

Render exposes port `10000` by default.

---

## 🪄 3️⃣ Deploy on **Render**

### Step-by-step:

1. Go to: [https://dashboard.render.com/](https://dashboard.render.com/)
2. Click **"New Web Service"**
3. Connect to **GitHub Repository**
4. Fill in the details:

   * **Name**: `flight-fare-app` (or your choice)
   * **Environment**: `Python`
   * **Build Command**: *leave empty* (`requirements.txt` handles it)
   * **Start Command**:

     ```bash
     python app.py
     ```
   * **Environment Variables**: Not needed here.
5. Click **Create Web Service**
6. Wait for deployment (Render will auto-install dependencies).

---

## 🚨 Common Issue on Render:

* **Static / Templates not found:** Ensure your folder names are exactly `templates/` and `static/`
* **File not found (CSV):** Ensure `fly1.csv` is committed and in the **root directory**.

---

## 🌐 4️⃣ Access Your App

Render will provide you a live URL like:

```
https://flight-fare-app.onrender.com
```

---

## 📌 5️⃣ Optional `.gitignore`

```txt
venv/
__pycache__/
*.pyc
```

---

## ✅ Final Checklist Before Push to GitHub:

* [x] `app.py`
* [x] `requirements.txt`
* [x] `templates/flight.html`
* [x] `fly1.csv`
* [x] `.render.yaml` (optional but clean)
* [x] `static/style.css` (optional)
* [x] `.gitignore`

---

## 🏁 Example Final URL:

```
https://flight-fare-app.onrender.com
```

---
