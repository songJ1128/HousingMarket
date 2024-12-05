from flask import Blueprint, jsonify

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    return jsonify({"message": "Login endpoint"})

@auth_blueprint.route('/register', methods=['POST'])
def register():
    return jsonify({"message": "Register endpoint"})
