#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route("/", methods=["GET"])
def home():
    # Return a welcome message for the root endpoint
    return "Welcome to the Flask API!"

@app.route("/data", methods=["GET"])
def get_data():
    # Return a JSON list of all usernames stored in the users dictionary
    return jsonify(list(users.keys()))

@app.route("/status", methods=["GET"])
def status():
    # Return a simple OK status message
    return "OK"

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    # Retrieve user data by username, return error if not found
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    # Parse JSON data from the request and add a new user
    data = request.get_json(force=True)
    username = data.get("username")
    if not username:
        # Return error if username is missing
        return jsonify({"error": "Username is required"}), 400
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    # Return confirmation with added user data
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    # Run the Flask development server
    app.run()
