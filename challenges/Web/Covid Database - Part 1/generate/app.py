from datetime import datetime, timedelta
from flask import Flask, request, jsonify, abort, render_template
import jwt
import account_manager
import data_factory


app = Flask(__name__)


def create_token(user_id: str):
    payload = {
        'exp': (datetime.now() + timedelta(days=0, seconds=100)).timestamp(),
        'iat': datetime.now().timestamp(),
        'user_id': user_id
    }
    encoded = jwt.encode(payload, "covdb", algorithm="HS256")
    return encoded


def validate_token(auth_data: str, admin: bool = False):
    if not auth_data:
        abort(400, "Missing auth data.")
    
    auth_data_split = auth_data.split(" ", 2)
    if len(auth_data_split) != 2:
        abort(400, "No auth type specified.")

    auth_type, token = auth_data_split
    if auth_type != "Beaver":
        abort(400, f"Invalid auth type {auth_type}. Only Beaver supported!")

    try:
        decoded = jwt.decode(token, "covdb", algorithms=["HS256"], options={"verify_signature": admin})
        if admin and decoded.et('user_id') != "43274923":
            abort(401, "Requires admin to access.")
    except:
        abort(401, "Invalid auth token. Did you modify it?")
    
    expire_time = decoded.get("exp")
    if datetime.now().timestamp() > expire_time:
        abort(401, "Auth token expired.")

    user_id = decoded.get("user_id")
    if not account_manager.is_valid_user_id(user_id):
        abort(401, "Invalid user id.")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api')
def api():
    #TODO actual html documentation.
    return render_template("api.html")


@app.route('/api/login', methods=["POST"])
def login():
    login_credentials = request.json
    if not isinstance(login_credentials, dict):
        abort(400)

    user_id = account_manager.get_user_id(login_credentials["username"])
    if not user_id:
        abort(404, "Invalid user.")

    if not account_manager.authenticate_user(user_id, login_credentials["password"]):
        abort(401, f"Invalid password for user {user_id}")

    new_token = create_token(user_id)
    return jsonify({"authorization_token": new_token})


@app.route('/api/data/countries')
def countries():
    auth_data = request.headers.get("Authorization")
    validate_token(auth_data)
    return jsonify(data_factory.get_countries())


@app.route('/api/data/countries/<string:country>')
def country(country):
    auth_data = request.headers.get("Authorization")
    validate_token(auth_data)
    country_data = data_factory.get_country_details(country)
    if not country_data:
        abort(404, "Country not found.")
    return country_data


@app.route('/api/users')
def users():
    auth_data = request.headers.get("Authorization")
    validate_token(auth_data, True)
    return jsonify(account_manager.get_users())


@app.route('/api/users/<string:userid>')
def user(userid):
    auth_data = request.headers.get("Authorization")
    validate_token(auth_data, True)
    user_data = account_manager.get_user_info(userid)
    if not user_data:
        abort(404, "User not found.")
    return jsonify(user_data)


@app.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e)), 400


@app.errorhandler(401)
def unauthorized(e):
    return jsonify(error=str(e)), 401


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


if __name__ == "__main__":
    app.run(debug=True)
