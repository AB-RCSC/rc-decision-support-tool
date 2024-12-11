import os
import json
from flask import Flask, request, jsonify

# Create the folder for storing JSON files
data_folder = "data_files"
os.makedirs(data_folder, exist_ok=True)

# Flask app to handle HTTP requests
flask_app = Flask(__name__)

@flask_app.route("/save-fingerprint", methods=["POST"])
def save_fingerprint():
    data = request.json
    fingerprint = data.get("fingerprint")
    
    print(f"Received fingerprint: {fingerprint}")  # Debugging line
    
    if fingerprint:
        file_path = os.path.join(data_folder, f"{fingerprint}.json")
        print(f"File path: {file_path}")  # Debugging line
        
        if not os.path.exists(file_path):
            # Save new fingerprint data to JSON
            user_data = {"fingerprint": fingerprint}
            with open(file_path, "w") as json_file:
                print(f"Creating file: {file_path}")  # Debugging line
                json.dump(user_data, json_file, indent=4)
            return jsonify({"message": f"Fingerprint saved: {file_path}"}), 200
        else:
            return jsonify({"message": "Fingerprint already exists."}), 200
    else:
        return jsonify({"error": "No fingerprint provided."}), 400

# Run the Flask app
if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=5000, debug=True)
