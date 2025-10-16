# Flask Authentication Demo

A simple yet secure Flask web application demonstrating user authentication with form validation and responsive design.

## 🚀 Features

- **Homepage**: Clean welcome interface with navigation
- **Login System**: Secure email/password authentication
- **Form Validation**: 
  - Email format validation
  - Password minimum length (8 characters)
  - CSRF protection via Flask-WTF
- **Responsive Design**: Bootstrap 5 integration for mobile-friendly UI
- **Success/Error Pages**: Clear feedback for login attempts
- **Security**: Built-in form validation and CSRF protection

## 📁 Project Structure

```
.
├── templates/
│   ├── base.html       # Base template with Bootstrap integration
│   ├── index.html      # Homepage with welcome message
│   ├── login.html      # Login form with validation
│   ├── success.html    # Success page for valid credentials
│   └── denied.html     # Access denied page for invalid attempts
├── main.py             # Main Flask application with routes and forms
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```


## 🛠️ Setup and Installation

### Prerequisites
- Python 3.7+ installed on your system
- pip (Python package installer)

### Quick Start

1. **Clone or Download**
   ```bash
   # Clone the repository or download the files to your local directory
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python main.py
   ```

5. **Access the App**
   Open your browser and navigate to: `http://127.0.0.1:5001`

### Expected Output
```
 * Serving Flask app 'main'
 * Debug mode: on
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
```


## 🎯 How to Use

1. **Navigate to Homepage**
   - Open `http://127.0.0.1:5001` in your browser
   - Click the "Login" button to proceed

2. **Test Authentication**
   Use these demo credentials:
   ```
   Email: admin@email.com
   Password: 12345678
   ```

3. **Expected Behavior**
   - ✅ **Valid credentials**: Redirects to success page
   - ❌ **Invalid credentials**: Shows access denied page
   - ⚠️ **Invalid format**: Form validation prevents submission

## 🔒 Security Features

- **CSRF Protection**: All forms include CSRF tokens
- **Input Validation**: Email format and password length validation
- **Secure Forms**: Flask-WTF integration for enhanced security
- **Error Handling**: Graceful handling of invalid inputs

## 🛡️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python 3.7+, Flask 3.0+ |
| **Forms** | Flask-WTF, WTForms |
| **Templating** | Jinja2 |
| **Styling** | Bootstrap 5 (via Bootstrap-Flask) |
| **Validation** | WTForms validators, email-validator |

## 📦 Dependencies

```txt
Flask>=3.0.0          # Web framework
Werkzeug>=3.0.1       # WSGI utility library
Bootstrap-Flask>=2.3.0 # Bootstrap integration
Flask-WTF>=1.2.1      # Form handling and CSRF protection
WTForms>=3.1.0        # Form validation
email-validator>=2.1.1 # Email format validation
```

## 🚧 Development Notes

- **Debug Mode**: Enabled for development (disable in production)
- **Secret Key**: Hardcoded for demo purposes (use environment variables in production)
- **Credentials**: Hardcoded for testing (implement database authentication for production)
- **Port**: Runs on port 5001 to avoid conflicts

## 📝 License

This project is for educational purposes and demonstration of Flask authentication concepts.
