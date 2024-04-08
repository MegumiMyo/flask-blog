# Flask Blog
This is a simple blog web application built using Flask, a lightweight web framework in Python.

## Features
- User authentication (register, login, logout)
- Create, edit, and delete blog posts
- View blog posts by category or author
- Responsive design using Bootstrap

## Technologies Used
- Python
- Flask
- SQLAlchemy (for database ORM)
- HTML/CSS (Bootstrap for styling)
- SQLite (or other relational database)
- WTForms (for form validation)
- Flask-Bcrypt (for password hashing)
- Flask-Login (for user session management)

## Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/flask-blog.git
cd flask-blog
```
Create a virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Set up environment variables (create a .env file in the root directory):
```plaintext
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///site.db
```
Initialize the database and run the application:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
flask run
```
Visit http://localhost:5000 in your web browser to view the Flask blog application.

## Usage
- Register a new user account.
- Log in with your registered account.
- Create, edit, or delete blog posts.
- Browse blog posts by category or author.

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your changes.

1. Fork the repository (https://github.com/yourusername/flask-blog.git)
2. Create your feature branch (git checkout -b feature/your-feature)
3. Commit your changes (git commit -am 'Add your feature')
4. Push to the branch (git push origin feature/your-feature)
5. Open a new pull request

## License
This project is licensed under the Mozilla Public License Version 2.0 - see the LICENSE file for details.

