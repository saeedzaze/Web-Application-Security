#https://github.com/saeedzaze/Web-Application-Security

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, username, password, role):
        self.id = username
        self.password = password
        self.role = role

users = {
    'admin': User('admin', 'admin_password', 'admin'),
    'user': User('user', 'user_password', 'user'),
}

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)
    
# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/admin')
@login_required
def admin():
    if current_user.role == 'admin':
        return render_template('admin.html')
    elif current_user.role == 'user':
        flag = "Success! You accessed the admin page with a user role. Your flag is FLAGBROKENACCESSLAB1"
        return render_template('user.html', show_admin_button=False, flag=flag)
    else:
        flash('Access Denied. You do not have admin privileges.', 'danger')
        return redirect(url_for('home'))
        
@app.route('/user')
@login_required
def user():
    return render_template('user.html', show_admin_button=current_user.role == 'admin')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = users.get(username)

        if user and user.password == password:
            login_user(user)
            flash('Login successful!', 'success')
            if user.role == 'admin':
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('user'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('home'))

# Run the Application
if __name__ == '__main__':
    app.run(debug=True)
