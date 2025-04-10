from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    pass

@app.route('/view')
def view():
    pass

@app.route('/register')
def register():
    pass

@app.route('/create')
def create():
    pass

@app.route('/delete')
def create():
    pass

@app.route('/edit')
def create():
    pass

if __name__ == '__main__':
    app.run(debug=True)