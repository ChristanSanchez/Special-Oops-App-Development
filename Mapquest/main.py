from flask import Flask, render_template, request, jsonify
from backend.mapquest_service import get_route

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/route", methods=["POST"])
def route():
    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "error": "Invalid request."
        }), 400

    origin = data.get("origin", "").strip()
    destination = data.get("destination", "").strip()
    unit = data.get("unit", "k")
    route_type = data.get("route_type", "fastest")

    if unit not in ["k", "m"]:
        unit = "k"

    if route_type not in ["fastest", "shortest"]:
        route_type = "fastest"

    result = get_route(
        origin,
        destination,
        unit,
        route_type
    )

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)