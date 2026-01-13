CREATE TABLE users (id INT PRIMARY KEY, name TEXT, email TEXT UNIQUE);
INSERT INTO users VALUES (1, "Gilbert", "gilbert@gmail.com");
SELECT * FROM users;
UPDATE users SET name="Cheboi" WHERE id=1;
SELECT * FROM users;
DELETE FROM users WHERE id=1;
SELECT * FROM users;
