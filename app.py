'''
flask 用户登录认证 https://www.cnblogs.com/ityouknow/p/12993209.html
'''
from flask import Flask , session, redirect, url_for, escape, request
from flask_login import LoginManager
from flask_login import login_user

import sys
sys.path.append('.\\test')
from test.setting import *

from werkzeug.security import generate_password_hash
import uuid

from wtforms import StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo

from flask import render_template, url_for
from flask_login import current_user, login_required

# ...
app = Flask(__name__)  # 创建 Flask 应用
app.secret_key = 'abc'  # 设置表单交互密钥
login_manager = LoginManager()  # 实例化登录管理对象
login_manager.init_app(app)  # 初始化应用
login_manager.login_view = 'login'  # 设置用户登录视图函数 endpoint


# ...
def create_user(user_name, password):
    """创建一个用户"""
    user = {
        "name": user_name,
        "password": generate_password_hash(password),
        "id": uuid.uuid4()
    }
    USERS.append(user)

def get_user(user_name):
    """根据用户名获得用户记录"""
    for user in USERS:
        if user.get("name") == user_name:
            return user
    return None

from flask_login import UserMixin  # 引入用户基类
from werkzeug.security import check_password_hash
# ...
class User(UserMixin):
    """用户类"""
    def __init__(self, user):
        self.username = user.get("name")
        self.password_hash = user.get("password")
        self.id = user.get("id")

    def verify_password(self, password):
        """密码验证"""
        if self.password_hash is None:
            return False
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        """获取用户ID"""
        return self.id

    @staticmethod
    def get(user_id):
        """根据用户ID获取用户实体，为 login_user 方法提供支持"""
        if not user_id:
            return None
        for user in USERS:
            if user.get('id') == user_id:
                return User(user)
        return None

@login_manager.user_loader  # 定义获取登录用户的方法
def load_user(user_id):
    return User.get(user_id)

# ...
class LoginForm(FlaskForm):
    """登录表单类"""
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])


from datetime import datetime, timedelta
@app.route('/login/', methods=('GET', 'POST'))  # 登录
def login():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)

    form = LoginForm()
    emsg = None
    if form.validate_on_submit():
        user_name = form.username.data
        password = form.password.data
        user_info = get_user(user_name)  # 从用户数据中查找用户记录
        print(user_info)
        if user_info is None:
            emsg = "用户名或密码密码有误"
        else:
            user = User(user_info)  # 创建用户实体
            print(user)
            if user.verify_password(password):  # 校验密码
                global s
                s=login_user(user) # 创建用户 Session


                print("------>")
                print(type(s),s)
                print(session)

                # 如果应用第三方sso认证，可以将sso的session添加到flask.seesion中，如果第三方需要获取该session，则用session.get('sso')

                session['sso'] = "hello world"
                return redirect(request.args.get('next') or url_for('index'))
            else:
                emsg = "用户名或密码密码有误"
    return render_template('login.html', form=form, emsg=emsg)

# ...
@app.route('/')  # 首页
@login_required  # 需要登录才能访问
def index():
    # return render_template('index.html', username=current_user.username)
    print(session)
    return render_template('input_form.html', username=current_user.username)

@app.route('/test')
@login_required
def test():
    # if request.method == 'POST':
    print(session)
    sso=session.get('sso')
    return ['test',sso]

@app.route('/result', methods=['POST', 'GET'])
@login_required
def set_result():
    try:
        if request.method == 'POST':
            result = request.form
            print(result,type(result))
            for i in result['input_2'].split(','):
                print(i,'value'+i)
            print('input_2', result['input_2'])
            return render_template("result.html", result=result,username=current_user.username)
    except:

        return redirect('/')





from flask import redirect, url_for
from flask_login import logout_user
# ...
@app.route('/logout')  # 登出
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
