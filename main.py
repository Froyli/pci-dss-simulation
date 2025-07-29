# PCI DSS Simulation for a Small Retail Web App

from flask import Flask, request, redirect, session
import logging
import os
from cryptography.fernet import Fernet

app = Flask(__name__)
app.secret_key = "supersecret"  # Needed to manage user sessions securely

# Setup logging folder
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(filename='logs/payment.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Setup encryption key
if not os.path.exists("secret.key"):
    with open("secret.key", "wb") as key_file:
        key_file.write(Fernet.generate_key())

with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Dummy user database (Admin only)
users = {
    "admin": "password123"
}

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Secure Payment Portal</title>
        <style>
            body { font-family: Arial; background-color: #f5f5f5; text-align: center; padding-top: 50px; }
            form { background: white; display: inline-block; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
            input[type=text], input[type=password] { padding: 10px; margin: 10px; width: 250px; border: 1px solid #ccc; border-radius: 5px; }
            input[type=submit] { padding: 10px 20px; background-color: #2d89ef; color: white; border: none; border-radius: 5px; cursor: pointer; }
            a { display: block; margin-top: 20px; color: #2d89ef; text-decoration: none; }
        </style>
    </head>
    <body>
        <h2>Mock Payment Form</h2>
        <form method="POST" action="/process_payment">
            <input type="text" name="name" placeholder="Name on Card" required><br>
            <input type="text" name="card_number" placeholder="Card Number" required><br>
            <input type="text" name="cvv" placeholder="CVV" required><br>
            <input type="submit" value="Pay Securely">
        </form>
        <a href="/login">Admin Login</a>
    </body>
    </html>
    '''

@app.route('/process_payment', methods=['POST'])
def process_payment():
    name = request.form['name']
    card_number = request.form['card_number']
    cvv = request.form['cvv']

    encrypted_card = fernet.encrypt(card_number.encode()).decode()
    logging.info(f"Processed payment for {name}. Encrypted card: {encrypted_card[:10]}...")

    return "<h2>Payment processed securely (simulation).</h2><br><a href='/'>Back</a>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            return redirect('/view_logs')
        else:
            return "<h3>Invalid login. <a href='/login'>Try again</a></h3>"

    return '''
    <html>
    <head>
        <title>Admin Login</title>
        <style>
            body { font-family: Arial; background-color: #f5f5f5; text-align: center; padding-top: 50px; }
            form { background: white; display: inline-block; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
            input[type=text], input[type=password] { padding: 10px; margin: 10px; width: 250px; border: 1px solid #ccc; border-radius: 5px; }
            input[type=submit] { padding: 10px 20px; background-color: #2d89ef; color: white; border: none; border-radius: 5px; cursor: pointer; }
        </style>
    </head>
    <body>
        <h2>Admin Login</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <input type="submit" value="Login">
        </form>
    </body>
    </html>
    '''

@app.route('/view_logs')
def view_logs():
    if 'user' not in session:
        return redirect('/login')

    with open('logs/payment.log', 'r') as f:
        log_data = f.read()

    return f"<h2>Transaction Logs</h2><pre style='text-align:left; margin: 30px auto; background:#eee; padding:20px; width:80%; border-radius:10px'>{log_data}</pre><br><a href='/logout'>Logout</a>"

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
