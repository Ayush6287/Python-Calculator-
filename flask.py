from flask import Flask, request, jsonify
from flask_cors import CORS  # Optional: for cross-origin requests
from datetime import datetime
import uuid

app = Flask(__name__)
CORS(app)  # Enable CORS if frontend is separate

# In-memory storage (use SQLite/PostgreSQL for production)
users_db = {}

@app.route('/')
def home():
    return jsonify({"message": "Flask API is running! Use /users for endpoints."})

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users_db.values()))

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users_db.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Name and email required"}), 400
    
    user_id = str(uuid.uuid4())
    user = {
        'id': user_id,
        'name': data['name'],
        'email': data['email'],
        'created_at': datetime.now().isoformat()
    }
    users_db[user_id] = user
    return jsonify(user), 201

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = users_db.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    user.update(data)
    user['updated_at'] = datetime.now().isoformat()
    return jsonify(user)

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users_db:
        del users_db[user_id]
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
