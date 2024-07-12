# python
# 原生操作：pymysql库
# ORM：flask_sqlalchemy pip install Flask-SQLAlchemy
from flask_sqlalchemy  import SQLAlchemy
from flask import Flask
app = Flask(__name__) #
#数据库配置                                                  用户名:密码@ip:port/数据库名
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1822@127.0.0.1:3306/garbage'
# 数据初始化对象
db_init = SQLAlchemy(app)
