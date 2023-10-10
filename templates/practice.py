from flask import Flask, render_template, session
from login_decorator import login_required  # Assumi

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for securing session data

# Example route protected by login_required decorator
@app.route('/protected')
@login_required
def protected():
    username = session['username']
    return f'Welcome, {username}! This is a protected route.'

# Your login and other routes go here...

if __name__ == '__main__':
    app.run(debug=True)
