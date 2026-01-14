# MiniRDBMS — Pesapal Junior Dev Challenge '26

This project is a mini relational database management system (RDBMS) built in Python as part of the Pesapal Junior Developer Challenge 2026.

It demonstrates core database concepts including table creation, constraints, CRUD operations, joins, persistence, and a simple web interface.

--------------------------------------------------

FEATURES

- Create tables with column types (INT, TEXT)
- Primary key and unique constraints
- Insert, select, update, and delete records
- Basic join between two tables
- Data persistence using JSON files
- Interactive command-line REPL
- Flask web app demonstrating CRUD

--------------------------------------------------

INSTALLATION

1. Clone the repository

git clone https://github.com/gilbert-rgb/pesapal-jdev26-rdbms
cd pesapal-jdev26-rdbms

2. Install dependencies and activate environment

pip install pipenv
pipenv install
pipenv shell

Requirements:
- Python 3.10 or higher
- Flask

--------------------------------------------------

RUNNING THE REPL

Start the database REPL:

python -m rdbms.repl 

Example commands:

CREATE TABLE users (id INT PRIMARY KEY, name TEXT, email TEXT UNIQUE);
INSERT INTO users VALUES (1, "Gilbert", "gilbert@gmail.com");
SELECT * FROM users;
UPDATE users SET name="Cheboi" WHERE id=1;
DELETE FROM users WHERE id=1;

Type:
exit
to quit the REPL.

--------------------------------------------------

RUNNING THE FLASK WEB APP

Start the web application:

python -m web.app


Available endpoints:

GET /users
Returns all users

POST /users
Adds a new user

Example JSON body:

{
  "id": 1,
  "name": "Gilbert",
  "email": "gilbert@gmail.com"
}

--------------------------------------------------

AUTHOR

Gilbert Cheboi
Email: icheboigilbert@gmail.com
Phone: +254743143013
GitHub: https://github.com/gilbert-rgb

--------------------------------------------------

LICENSE

This project is licensed under the MIT License.
See the LICENSE file for details.
