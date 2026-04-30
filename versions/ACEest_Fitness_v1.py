from flask import Flask, jsonify

app = Flask(__name__)

members = [
    {"id": 1, "name": "Samantha", "membership_type": "Premium"},
    {"id": 2, "name": "Marcus", "membership_type": "Standard"},
]

@app.route("/")
def home():
    return jsonify({"service": "ACEest Fitness v1", "status": "ok"})

@app.route("/api/members")
def get_members():
    return jsonify(members)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
