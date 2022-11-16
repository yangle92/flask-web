from flask import Flask, render_template, request
from functools import  wraps

app = Flask(__name__)


def permission(func):
    @wraps(func)
    def inner():
        user_info = {'admin': 'admin', 'tom': 'tom'}
        user=request.form.get('input_1')
        password=request.form.get('input_2')
        # user = input('Username: ')
        # password = input('Password: ')
        if user_info[user] == password:
            print('%s log on  ...' % user)
            return func()
        else:
            print('login fail,please enter the password ')
            return permission(func)
    return inner

@app.route('/login')
def get_login_form():
    return render_template('login.html')



@app.route('/')
def get_form():
    return render_template('input_form.html')


@app.route('/result', methods=['POST', 'GET'])
def set_result():
    if request.method == 'POST':
        result = request.form
        print(result,type(result))
        for i in result['input_2'].split(','):
            print(i,'value'+i)
        print('input_2', result['input_2'])
        return render_template("result.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
