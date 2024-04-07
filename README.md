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

- `/api/books`

  - <font color="blue">**GET**</font>: Get a list of all books.
  - <font color="green">**POST**</font>: Add a new book (Admin only).

- `/api/books/<book_id>`

  - <font color="blue">**GET**</font>: Get details of a specific book.
  - <font color="orange">**PUT**</font>: Update details of a specific book (Admin only).
  - <font color="red">**DELETE**</font>: Delete a specific book (Admin only).

- `/api/users/register`

  - <font color="green">**POST**</font>: Register a new user.

- `/api/users/login`

  - <font color="green">**POST**</font>: Log in an existing user and receive a JWT token.

- `/api/users/logout`

  - <font color="green">**POST**</font>: Log out the current user.

- `/api/users/<username>`

  - <font color="blue">**GET**</font>: Get details of the current user.
  - <font color="orange">**PUT**</font>: Update details of the current user.
  - <font color="red">**DELETE**</font>: Delete the current user account.

- `/api/books/<book_id>/read`

  - <font color="blue">**GET**</font>: Read the specified book.

## Usage

1. Ensure the Flask server is running (flask run).
2. Use tools like Postman or curl to interact with the API endpoints.
3. Refer to Swagger UI (/apidocs) for detailed API documentation and testing.
