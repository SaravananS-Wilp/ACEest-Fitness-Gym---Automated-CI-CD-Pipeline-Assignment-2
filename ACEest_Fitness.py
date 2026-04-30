from dataclasses import asdict, dataclass
from datetime import datetime
from flask import Flask, jsonify, request, abort
from typing import List

@dataclass
class Member:
    id: int
    name: str
    membership_type: str
    joined_on: str

@dataclass
class Workout:
    id: int
    title: str
    category: str
    duration_minutes: int
    difficulty: str

@dataclass
class Booking:
    id: int
    member_id: int
    workout_id: int
    scheduled_for: str


def create_app() -> Flask:
    app = Flask(__name__)

    members: List[Member] = [
        Member(1, "Samantha", "Premium", "2026-01-18"),
        Member(2, "Marcus", "Standard", "2026-02-05"),
        Member(3, "Aisha", "Premium", "2026-03-09"),
    ]

    workouts: List[Workout] = [
        Workout(1, "Strength Training", "Resistance", 45, "Intermediate"),
        Workout(2, "Yoga Flow", "Flexibility", 60, "Beginner"),
        Workout(3, "HIIT Blast", "Cardio", 30, "Advanced"),
    ]

    bookings: List[Booking] = []

    @app.route("/")
    def home():
        return jsonify({
            "name": "ACEest Fitness & Gym",
            "version": "1.0.0",
            "description": "Fitness management backend for memberships, workouts, and booking automation.",
            "timestamp": datetime.utcnow().isoformat() + "Z",
        })

    @app.route("/api/members")
    def get_members():
        return jsonify([asdict(member) for member in members])

    @app.route("/api/workouts")
    def get_workouts():
        return jsonify([asdict(workout) for workout in workouts])

    @app.route("/api/bookings", methods=["GET"])
    def get_bookings():
        return jsonify([asdict(booking) for booking in bookings])

    @app.route("/api/bookings", methods=["POST"])
    def create_booking():
        payload = request.get_json(force=True)
        if not payload:
            abort(400, description="JSON payload is required.")

        member_id = payload.get("member_id")
        workout_id = payload.get("workout_id")
        scheduled_for = payload.get("scheduled_for")

        if not member_id or not workout_id or not scheduled_for:
            abort(400, description="member_id, workout_id, and scheduled_for are required.")

        if not any(member.id == member_id for member in members):
            abort(404, description="Member not found.")
        if not any(workout.id == workout_id for workout in workouts):
            abort(404, description="Workout not found.")

        booking_id = len(bookings) + 1
        booking = Booking(booking_id, member_id, workout_id, scheduled_for)
        bookings.append(booking)
        return jsonify(asdict(booking)), 201

    @app.route("/api/metrics")
    def metrics():
        active_members = len(members)
        active_workouts = len(workouts)
        today_bookings = sum(
            1 for booking in bookings if booking.scheduled_for.startswith(datetime.utcnow().date().isoformat())
        )
        return jsonify({
            "active_members": active_members,
            "workout_catalog_size": active_workouts,
            "today_bookings": today_bookings,
            "uptime": "continuous",
        })

    @app.route("/api/health")
    def health():
        return jsonify({"status": "healthy", "service": "ACEest Fitness API"})

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
