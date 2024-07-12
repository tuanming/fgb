from flask import Blueprint, request, jsonify
from PIL import Image
# import json
garbage = Blueprint('garbage', __name__)
# from services.user import User_operation


@garbage.route("/classfy", methods=['POST'])
def classfy():
    file = request.files['image']
    file.save(file.filename)
    file_stream = file.stream
    img = Image.open(file_stream)
    # ai接口
    # user services
    # 逻辑
    return 'result'