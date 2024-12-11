import os
from flask import Flask, jsonify
from flask_cors import CORS  # Import CORS

# Flask app to handle HTTP requests
flask_app = Flask(__name__)

# Enable CORS for all routes
CORS(flask_app)

@flask_app.route("/print-message", methods=["GET"])
def print_message():
    print("Flask is running and printed this message!")  # This prints on the server side
    return jsonify({"message": "Message printed successfully!"}), 200

if __name__ == "__main__":
    flask_app.run(
    host="0.0.0.0",
    port=5000,
    debug=True,
    ssl_context=('server.crt', 'server_no_pass.key')
)

