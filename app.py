from utils.db_config import app

# 用户模块
from routes.user import user
app.register_blueprint(user, url_prefix="/user")

# 垃圾模块
from routes.garbage import garbage
app.register_blueprint(garbage, url_prefix="/garbage")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
