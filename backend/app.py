from flask import Flask, render_template, redirect, url_for, request, session, flash, send_from_directory
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')

app.secret_key = 'your_secret_key_here'

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['user_db']
users_collection = db['users']

# Ensure unique index on username
users_collection.create_index('username', unique=True)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users_collection.find_one({'username': username})
        if user and check_password_hash(user['password'], password):
            session['logged_in'] = True
            return redirect('http://localhost:8501')  # Redirect to Streamlit app
        else:
            flash('Invalid username or password')
    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')
        try:
            users_collection.insert_one({'username': username, 'password': hashed_password})
            return redirect(url_for('signin'))
        except:
            flash('Username already exists')
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('signin'))

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
