from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # return render_template('index.html')
    return "<h1> Hello moi </h1>"

