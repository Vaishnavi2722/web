from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    mobile = db.Column(db.String(10), unique=True, nullable=False)

# Route: Homepage (Login Page)
@app.route('/')
def index():
    return render_template('index.html')

# Route: Signup Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        mobile = request.form['mobile']

        # Save user to database
        user = User(first_name=first_name, last_name=last_name, email=email, mobile=mobile)
        db.session.add(user)
        db.session.commit()
        return redirect('/')
    return render_template('signup.html')

# Initialize database
if __name__ == '_main_':
    db.create_all()  # Create database tables
    app.run(debug=True)