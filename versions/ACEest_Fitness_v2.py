from flask import Flask, jsonify, request, abort

app = Flask(__name__)

members = [
    {"id": 1, "name": "Samantha", "membership_type": "Premium"},
    {"id": 2, "name": "Marcus", "membership_type": "Standard"},
]
workouts = [
    {"id": 1, "title": "Strength Training", "duration": 45},
    {"id": 2, "title": "Yoga Flow", "duration": 60},
]
bookings = []

@app.route("/")
def home():
    return jsonify({"service": "ACEest Fitness v2", "status": "ok"})

@app.route("/api/workouts")
def get_workouts():
    return jsonify(workouts)

@app.route("/api/bookings", methods=["POST"])
def book_workout():
    data = request.get_json(force=True)
    if not data or "member_id" not in data or "workout_id" not in data:
        abort(400, description="member_id and workout_id are required")
    booking = {"id": len(bookings) + 1, **data}
    bookings.append(booking)
    return jsonify(booking), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
