from flask import Flask,render_template

app = Flask(__name__)



@app.route('/')
def hello_world():
    result={'1':['hello','world12111111111'],
            '2': ['hello', 'world'],
            '3': ['hello', 'world']
            }

    return render_template("test1.html", result=result)


if __name__ == '__main__':
    app.run()
