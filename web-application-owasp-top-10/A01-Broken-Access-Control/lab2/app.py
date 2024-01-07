#https://github.com/saeedzaze/Web-Application-Security

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a more secure value in a production environment

# Sample data - user accounts with unique identifiers
user_accounts = {
    '1': {'username': 'user1', 'email': 'user1@example.com', 'password': 'password1'},
    '2': {'username': 'user2', 'email': 'user2@example.com', 'password': 'password2'},
    '3': {'username': 'user3', 'email': 'user3@example.com', 'password': 'password3'},
}

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for user_id, user_info in user_accounts.items():
            if user_info['username'] == username and user_info['password'] == password:
                session['user_id'] = user_id
                return redirect(url_for('view_account', user_id=user_id))

        return "Invalid login credentials."

    return render_template('login.html')

# Route to display user account details
@app.route('/account/<user_id>')
def view_account(user_id):
    if 'user_id' in session :#and user_id == session['user_id']:
        account = user_accounts[user_id]
        return render_template('account.html', account=account)
    else:
        
        return "Access denied. Please log in."

# Route to edit user account details
@app.route('/edit_account/<user_id>', methods=['GET', 'POST'])
def edit_account(user_id):
    if 'user_id' in session :#and user_id == session['user_id']:
        account = user_accounts[user_id]

        if request.method == 'POST':
            # Update user account details
            account['username'] = request.form['username']
            account['email'] = request.form['email']
            return redirect(url_for('view_account', user_id=user_id))

        return render_template('edit_account.html', account=account)
    else:
        return "Access denied. Please log in."

# Route to logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
