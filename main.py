# Import necessary classes from Flask, Flask-WTF, WTForms, and Bootstrap-Flask
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
# Added Email and Length validators for better form validation
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

# Define a login form class that inherits from FlaskForm
class LoginForm(FlaskForm):
    # Email field: Must be a valid email format and cannot be empty.
    email = StringField('Email', validators=[DataRequired(), Email()])
    # Password field: Must be at least 8 characters long and cannot be empty.
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    # Submit button for the form
    submit = SubmitField(label="Log In")


# --- Flask App Setup ---
# Create an instance of the Flask class
app = Flask(__name__)
# Set a secret key for the app, required for CSRF protection in forms
app.secret_key = "any-string-you-want-just-keep-it-secret"
# Initialize Bootstrap 5 for the Flask app to easily use Bootstrap styles
bootstrap = Bootstrap5(app)


# --- Route Definitions ---
# Define the route for the homepage
@app.route("/")
def home():
    # Render the index.html template when a user visits the root URL
    return render_template('index.html')


# Define the route for the login page, accepting both GET and POST requests
@app.route("/login", methods=["GET", "POST"])
def login():
    # Create an instance of the LoginForm
    login_form = LoginForm()
    # This block executes when the form is submitted and passes all validation checks
    if login_form.validate_on_submit():
        # Check if the submitted email and password match the hardcoded credentials
        # NOTE: In a real application, you would check against a database, not hardcoded values.
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            # If credentials are correct, show the success page
            return render_template("success.html")
        else:
            # If credentials are incorrect, show the access denied page
            return render_template("denied.html")
    # If the request is GET (i.e., just visiting the page) or the form fails validation,
    # render the login page and pass the form object to it.
    return render_template("login.html", form=login_form)


# This standard Python construct ensures the app only runs when the script is executed directly
if __name__ == '__main__':
    # Run the app in debug mode on port 5001
    app.run(debug=True, port=5001)