import os
from flask import Flask, render_template, request, redirect, url_for, jsonify

basedir = os.path.abspath(os.path.dirname(__file__))
from logging import DEBUG

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/form", methods=['GET', 'POST'])
def form():
    return render_template("form.html")


@app.route('/calculate_result')
def calculate_result():
    a = int(request.args.get('val1'))
    b = int(request.args.get('val2'))
    return jsonify({"result": gcd(a, b)})


def gcd(x, y):
    if x == 0:
        return y  # GCD of a number with zero is the number itself
    else:
        return gcd(y % x, x)  # GCD is remainder of y/x and x


if __name__ == '__main__':
    app.run(debug=True)
