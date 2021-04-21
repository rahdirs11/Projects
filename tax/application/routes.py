from flask import render_template
from application import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', home=True)


@app.route('/login')
def login():
    return render_template('login.html', login=False)


@app.route('/logout')
def logout():
    return "<h1>Logout</h1>"
