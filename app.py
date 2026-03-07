from flask import Flask, jsonify, request
from fitness_logic import calculate_bmi, membership_status

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "ACEest Fitness DevOps Service"})


@app.route("/bmi")
def bmi():
    weight = float(request.args.get("weight"))
    height = float(request.args.get("height"))

    result = calculate_bmi(weight, height)

    return jsonify({
        "weight": weight,
        "height": height,
        "category": result
    })


@app.route("/membership")
def membership():
    end_date = request.args.get("end")

    status = membership_status(end_date)

    return jsonify({
        "membership_end": end_date,
        "status": status
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)