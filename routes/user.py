from flask import Blueprint, request
import json
user = Blueprint('user', __name__)
from services.user import User_operation


@user.route("/login", methods=['POST'])
def login():
    data = json.loads(request.data)
    username = data['username']
    password = data['password']
    u_o = User_operation()
    result = u_o.login(username, password)
    return result