from flask import Flask, request, jsonify, send_from_directory
from database import create_tables
from models import add_decision, get_all_decisions
from analytics import mood_pattern
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="../frontend", static_url_path="")
CORS(app)

create_tables()

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<path:path>")
def serve_static(path):
    if os.path.isfile(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, "index.html")

@app.route("/decisions", methods=["GET"])
def fetch_decisions():
    return jsonify(get_all_decisions())

@app.route("/decisions", methods=["POST"])
def create_decision():
    add_decision(request.json)
    return jsonify({"status": "saved"})

@app.route("/analytics", methods=["GET"])
def analytics():
    decisions = get_all_decisions()
    return jsonify(mood_pattern(decisions))

if __name__ == "__main__":
    app.run(debug=True, port=5002)
