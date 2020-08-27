from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Home Page</h1>"

@app.route('/about')
def about():
    return "<h1>About Us</h1>" 