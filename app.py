from flask import Flask, jsonify, request, render_template
from fitness_logic import calculate_bmi,calculate_bmi_value

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    bmi = None
    category = None
    error = None

    if request.method == "POST":
        try:
            if "weight" in request.form:
                weight = float(request.form["weight"])
                height = float(request.form["height"])

                bmi_value = calculate_bmi_value(weight, height)
                bmi = round(bmi_value, 2)
                category = calculate_bmi(weight, height)

        except ValueError as e:
            error = str(e)
        except Exception:
            error = "Invalid input"

    return render_template(
        "index.html",
        bmi=bmi,
        category=category,
        error=error,
    )

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)