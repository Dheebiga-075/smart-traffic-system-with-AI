from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():

    vehicle_count = random.randint(5,50)

    if vehicle_count <= 10:
        signal_time = 15
    elif vehicle_count <= 25:
        signal_time = 30
    else:
        signal_time = 60

    return render_template("index.html",
                           vehicles=vehicle_count,
                           signal=signal_time)

if __name__ == "__main__":
    app.run(debug=True)