from flask import Flask, render_template


app = Flask("website")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperature = 16
    return {"station": station,
            "date": date,
            "temperature": temperature}

app.run(debug=True)