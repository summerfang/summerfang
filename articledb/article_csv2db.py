import sqlite3
import pandas as pd

sql = '''INSERT INTO articles 
    (title, subtitle, content, date_create, date_lastmodified, author_name)  VALUES 
    (?, ?, ?, ?, ?, ?)'''

conn = sqlite3.connect('articles.db')
cur = conn.cursor()

articles_df = pd.read_csv('articles.csv')

for row in articles_df.itertuples(index=True, name='Pandas'):
    an_article = list()
    an_article.append(getattr(row, 'title'))
    an_article.append(getattr(row, 'subtitle'))
    an_article.append(getattr(row, 'content'))
    an_article.append(getattr(row, 'date_create'))
    an_article.append(getattr(row, 'date_lastmodified'))
    an_article.append(getattr(row, 'author_name'))


    print(an_article)
    cur.execute(sql, an_article)

conn.commit()