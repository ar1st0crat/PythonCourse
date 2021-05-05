from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/wow')
def wow():
    return 'Wow'

@app.route('/page')
def page():
    cars = [ { 'model': 'Toyota Lexus', 'no': 'A123AH' }, 
             { 'model': 'Ford Focus', 'no': 'A765OO' } ]
    return render_template('page.html', cars=cars)
