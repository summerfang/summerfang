import sqlite3

conn = sqlite3.connect('articles.db')

cur = conn.cursor()

articles_schema_file = open('articledb_schema.sql', 'r')
articles_schema_init_script = articles_schema_file.read()

cur.executescript(articles_schema_init_script)
