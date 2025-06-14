#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity
)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "your-very-secret-key"  # Set a strong secret key for JWT

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory user store with hashed passwords and roles
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    # Return access granted message if basic auth credentials are valid
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    # Accept JSON payload and return JWT token if credentials are valid
    data = request.get_json(force=True)
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Create JWT token embedding username and role
    access_token = create_access_token(identity={"username": username, "role": user["role"]})
    return jsonify(access_token=access_token)

@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    # Return access granted if valid JWT token provided
    return "JWT Auth: Access Granted"

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    # Check if current user has admin role, else return 403
    identity = get_jwt_identity()
    if identity.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# Custom error handlers for JWT errors, all return 401 Unauthorized
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == "__main__":
    # Run the Flask development server
    app.run()
