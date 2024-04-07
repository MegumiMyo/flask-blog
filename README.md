# Flask API for Online Book Reading

This project implements a Flask API for online book reading. Users can access books and read them via this API. It includes endpoints for retrieving book information, reading books, and managing user accounts.

## Features

User Authentication: Users can sign up, log in, and manage their accounts.
Book Retrieval: Retrieve information about available books.
Reading Interface: Access books and read them online.
User Settings: Customize reading preferences and manage account details.

## Technologies Used

- Flask: Python web framework for building the API.
- SQLite: Database to store book and user information.
- JWT (JSON Web Tokens): For secure authentication and authorization.
- SQLAlchemy: ORM (Object-Relational Mapping) for interacting with the database.
- Swagger UI: Documentation and testing interface for API endpoints.

## Installation

Clone the repository:

```bash
git clone https://github.com/MineNique/flask-book-api.git
```

Navigate to the project directory:

```bash
cd flask-book-api
```

Install dependencies using pip:

```bash
pip install -r requirements.txt
```

Set up the database:

```bash
flask db init
flask db migrate
flask db upgrade
```

Start the Flask development server:

```bash
flask run
```

## API Endpoints

- /api/books

  - GET: Get a list of all books.
  - POST: Add a new book (Admin only).

- /api/books/<book_id>

  -GET: Get details of a specific book.
  -PUT: Update details of a specific book (Admin only).
  -DELETE: Delete a specific book (Admin only).

- /api/users/register

  - POST: Register a new user.

- /api/users/login

  - POST: Log in an existing user and receive a JWT token.

- /api/users/logout

  - POST: Log out the current user.

- /api/users/<username>

  - GET: Get details of the current user.
  - PUT: Update details of the current user.
  - DELETE: Delete the current user account.

- /api/books/<book_id>/read

  - GET: Read the specified book.

## Usage

1. Ensure the Flask server is running (flask run).
2. Use tools like Postman or curl to interact with the API endpoints.
3. Refer to Swagger UI (/apidocs) for detailed API documentation and testing.
