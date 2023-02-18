#!/usr/bin/env python3
"""Flask Application
"""


from flask import Flask, jsonify, request, make_response, abort
from auth import Auth
from os import getenv


# Create application
app = Flask(__name__)

# instantiate Auth
auth = Auth()


# home route
@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    '''
    '''
    return jsonify({"message": "Bienvenue"}), 200


# users route
@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    '''
    '''
    if request.method == 'POST':
        email = str(request.form.get('email'))
        password = str(request.form.get('password'))
        try:
            auth.register_user(email, password)
            return jsonify({"email": email, "message": "user created"}), 200
        except ValueError:
            return jsonify({"message": "email already registered"}), 200


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    '''
        Login user by setting cookies
    '''
    if request.method == 'POST':
        email = str(request.form.get('email'))
        password = str(request.form.get('password'))
        valid = auth.valid_login(email, password)
        if valid:
            session_id = auth.create_session(email)
            resp = make_response()
            resp.set_cookie('session_id', session_id)
            return jsonify({"email": email, "message": "logged in"}), 200
        else:
            abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    '''
        Log Out user getting cookies and destroying the cookies
    '''
    if request.method == 'DELETE':
        cook = request.cookies.get('session_id')
        user = auth.get_user_from_session_id(cook)
        auth.destroy_session(user.id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
