from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def get_form():
    return render_template('input_form.html')


@app.route('/result', methods=['POST', 'GET'])
def set_result():
    if request.method == 'POST':
        result = request.form
        print(result,type(result))
        print("input_1", result['input_1'])
        for i in result['input_2'].split(','):
            print(i,'value'+i)
        print('input_2', result['input_2'])



        return render_template("result.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
