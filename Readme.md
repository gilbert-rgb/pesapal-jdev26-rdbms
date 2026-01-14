# MiniRDBMS — Pesapal Junior Dev Challenge '26

This project is a **mini relational database management system (RDBMS)** built in Python as part of the Pesapal Junior Developer Challenge 2026.

## Features
It supports:

- Creating tables with column types (`INT`, `TEXT`)
- Primary keys (`PRIMARY KEY`) and unique constraints (`UNIQUE`)
- CRUD operations (`INSERT`, `SELECT`, `UPDATE`, `DELETE`)
- Basic JOIN between two tables
- Data persistence using JSON files
- Interactive REPL interface
- Flask web app demonstrating CRUD operations

---



### Installation

1. Clone the repository:


git clone <https://github.com/gilbert-rgb/pesapal-jdev26-rdbms>
cd pesapal-jdev26-rdbms

2. Activate the virtual environment and install dependencies:

pip install pipenv
pipenv install
pipenv shell

#### Technology used:

Requires Python 3.10+ and Flask.

##### Running the REPL

The REPL allows you to interact with the database using SQL-like commands.

python -m rdbms.repl or python rdbms/repl.py

Example commands:
CREATE TABLE users (id INT PRIMARY KEY, name TEXT, email TEXT UNIQUE);
INSERT INTO users VALUES (1, "Gilbert", "gilbert@gmail.com");
SELECT * FROM users;
UPDATE users SET name="Cheboi" WHERE id=1;
DELETE FROM users WHERE id=1;

 Type exit to quit the REPL.

 ###### Running the Flask Web App

 The Flask app demonstrates CRUD operations via HTTP requests:

 1.Run the app:
 python web/app.py

 2.API endpoints:

GET /users → Returns all users

POST /users → Add a new user (JSON body example: {"id": 1, "name": "Gilbert", "email": "gilbert@gmail.com"})

 ###### AUTHOR
Gilbert Cheboi
Email: icheboigilbert@gmail.com
Tell NO: +254743143013
GitHub: gilbert-rgb

---

###### License

This project is licensed under the **MIT License**.  

See the [LICENSE](LICENSE) file for details.





