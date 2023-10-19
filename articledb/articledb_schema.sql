DROP TABLE IF EXISTS articles;

CREATE TABLE articles (
    article_id INTEGER PRIMARY KEY,
    title VARCHAR(255),
    subtitle VARCHAR(255),
    content TEXT,
    date_create DATE,
    date_lastmodified DATE,
    author_name VARCHAR(255)
);

DROP TABLE IF EXISTS tags;

CREATE TABLE tags (
    tag_id INTEGER PRIMARY KEY,
    tag_name VARCHAR(255)
);

DROP TABLE IF EXISTS article_tags;

CREATE TABLE article_tags (
    article_id INTEGER,
    tag_id INTEGER,
    FOREIGN KEY (article_id) REFERENCES articles(article_id),
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id)
);

