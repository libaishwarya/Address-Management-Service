from ipaddress import ip_address
from time import sleep
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# In-memory array to store student data
address = {}

# Get the port from the environment variable, default to 5000
port = int(os.environ.get('FLASK_PORT', 5000))

@app.route('/address', methods=['GET'])
def get_addresses():
    return jsonify({'address': address})

@app.route('/students/<int:student_id>/address', methods=['GET'])
def get_student_address(student_id):
    studentAddress = address[student_id]
    if address:
        return jsonify({'address': studentAddress})
    else:
        return jsonify({'message': 'Student address not found'}), 404

@app.route('/students/<int:student_id>/address', methods=['POST'])
def add_student(student_id):
    data = request.get_json()

    if 'city' not in data:
        return jsonify({'message': 'City is required'}), 400

    address[student_id] = {"city": data["city"]}
    return jsonify({'message': 'Student address added successfully', 'address': {"city": data["city"]}}), 201

if __name__ == '__main__':
    app.run(debug=True, port=port, host="0.0.0.0")
