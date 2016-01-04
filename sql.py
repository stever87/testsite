import sqlite3

#use to create empty shell for site.db

with sqlite3.connect("site.db") as connection:
	c = connection.cursor()
	#c.execute("""DROP TABLE posts""")
	c.execute("""CREATE TABLE `posts` (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`title`	TEXT NOT NULL,
	`content`	TEXT NOT NULL)""")

	c.execute('INSERT INTO posts (title, content) VALUES ("If you can read me", "sql.py has run correctly")')
