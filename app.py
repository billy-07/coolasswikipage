from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/view')
def view():
    return render_template('view.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/delete')
def create():
    return render_template('delete.html')

@app.route('/edit')
def create():
    return render_template('edit.html')

if __name__ == '__main__':
    app.run(debug=True)