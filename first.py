from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for registered users (replace with a database in a real application)
registered_users = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    # Basic validation, you might want to add more checks
    if not username or not password:
        return render_template('index.html', error='Username and password are required.')

    # Check if the username is already registered
    if username in [user['username'] for user in registered_users]:
        return render_template('index.html', error='Username already exists. Choose a different one.')

    # Store the user in memory (replace with database storage in a real application)
    registered_users.append({'username': username, 'password': password})

    # Redirect to a success page or login page
    return redirect(url_for('success'))


@app.route('/success')
def success():
    return 'Registration successful!'


if __name__ == '__main__':
    app.run(debug=True)
