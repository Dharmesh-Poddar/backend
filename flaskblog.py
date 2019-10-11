from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>welcome to my world</h1>"

@app.route('/about')
def about():
    return "<h1>know about me</h1>"