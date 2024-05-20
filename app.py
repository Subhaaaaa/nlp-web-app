from flask import Flask, render_template, request
from db import DataBase 


app = Flask(__name__)
dbo = DataBase()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('registration.html') 

@app.route('/perform_registration', methods = ['post'])
def perform_registration():

    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = dbo.insert(name, email, password)
    
    if response:
        return "Registration successful"
    else:
        return "Email already exists"

app.run(debug=True)