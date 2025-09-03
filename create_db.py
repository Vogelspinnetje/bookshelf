import sqlite3

conn = sqlite3.connect("books.db")
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS books (
    isbn TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    authors TEXT,
    publish_date INTEGER,
    number_of_pages INTEGER,
    read INTEGER DEFAULT 0
)
""")
conn.commit()
