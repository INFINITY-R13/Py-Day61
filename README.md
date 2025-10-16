# Py-Day61
Simple Flask Login Application

This is a basic web application built with Python and the Flask framework that demonstrates a simple user login system. It uses Flask-WTF for secure form handling and Bootstrap 5 for modern, responsive styling.

Features

A homepage with a welcome message.

A login page with email and password fields.

Form validation to ensure the email is in a valid format and the password meets a minimum length.

A "success" page for correct login credentials.

An "access denied" page for incorrect credentials.

Styled using Bootstrap 5 via the Bootstrap-Flask extension.

Project Structure

.
├── templates/
│   ├── base.html       # The base template all other pages extend
│   ├── index.html      # The homepage
│   ├── login.html      # The login page with the form
│   ├── success.html    # Page shown on successful login
│   └── denied.html     # Page shown on failed login
├── main.py             # The main Flask application logic
└── requirements.txt    # A list of Python packages required for the project


Setup and Installation

Follow these steps to get the application running on your local machine.

1. Prerequisites

Python 3 installed on your system.

pip (Python package installer).

2. Clone the Repository

First, clone this repository or download the files to a local directory.

3. Create a Virtual Environment (Recommended)

It's a best practice to create a virtual environment to keep the project's dependencies isolated.

On macOS/Linux:

python3 -m venv venv
source venv/bin/activate


On Windows:

python -m venv venv
.\venv\Scripts\activate


4. Install Dependencies

Install all the required Python packages using the requirements.txt file.

pip install -r requirements.txt


5. Run the Application

Execute the main.py script to start the Flask development server.

python main.py


You should see output similar to this in your terminal:

 * Serving Flask app 'main'
 * Debug mode: on
 * Running on [http://127.0.0.1:5001](http://127.0.0.1:5001)
Press CTRL+C to quit


How to Use

Open your web browser and navigate to http://127.0.0.1:5001.

You will see the welcome page. Click the "Login" button.

On the login page, use the following hardcoded credentials to test the application:

Email: admin@email.com

Password: 12345678

If you enter the correct credentials, you will be redirected to the "Top Secret" success page.

If you enter incorrect credentials or invalid data (e.g., a password less than 8 characters), you will be shown the "Access Denied" page.

Technology Stack

Backend: Python, Flask

Forms: Flask-WTF, WTForms

Frontend: HTML, Jinja

Styling: Bootstrap 5 (via Bootstrap-Flask)
