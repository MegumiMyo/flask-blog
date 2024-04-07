- `/api/books`

  - **GET**: Get a list of all books.
  - **POST**: Add a new book (Admin only).

- `/api/books/<book_id>`

  - **GET**: Get details of a specific book.
  - **PUT**: Update details of a specific book (Admin only).
  - **DELETE**: Delete a specific book (Admin only).

- `/api/users/register`

  - **POST**: Register a new user.

- `/api/users/login`

  - **POST**: Log in an existing user and receive a JWT token.

- `/api/users/logout`

  - **POST**: Log out the current user.

- `/api/users/<username>`

  - **GET**: Get details of the current user.
  - **PUT**: Update details of the current user.
  - **DELETE**: Delete the current user account.

- `/api/books/<book_id>/read`

  - **GET**: Read the specified book.
