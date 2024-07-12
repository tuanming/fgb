from models.user import User
from flask import jsonify
# 依赖数据模型类model类
class User_operation():
    def __init__(self):
        self.__fields__ = ['id', 'username', 'password']

    def login(self, name, pwd):
        code = 0
        u = User.query.filter_by(username=name).first()
        if u is None:
            return jsonify({'code': -1, 'message': '用户不存在', 'data': {}})

        u_data = u.to_dict()
        if u_data['password'] != pwd:
            return jsonify({'code': -2, 'message': '密码错误', 'data': {}})

        return jsonify({'code': 0, 'message': '登录成功', 'data': u_data})


