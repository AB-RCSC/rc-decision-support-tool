# import os
from flask import Flask, jsonify

# Flask app to handle HTTP requests
flask_app = Flask(__name__)

@flask_app.route("/print-message", methods=["GET"])
def print_message():
    print("Flask is running and printed this message!")  # This prints on the server side
    return jsonify({"message": "Message printed successfully!"}), 200

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=5000, debug=True)
