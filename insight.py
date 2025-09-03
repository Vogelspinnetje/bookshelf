import sqlite3


def sort_by_pages(conn, direction):
    c = conn.cursor()
    c.execute(f"SELECT * FROM books ORDER BY number_of_pages {direction}")
    result = c.fetchall()
    return result


def books_older_then(conn, year):
    c = conn.cursor()
    c.execute(f"SELECT * FROM books WHERE publish_date < {year}")
    result = c.fetchall()
    return result


def books_younger_then(conn, year):
    c = conn.cursor()
    c.execute(f"SELECT * FROM books WHERE publish_date > {year}")
    result = c.fetchall()
    return result


def count_authors(conn):
    c = conn.cursor()
    c.execute("SELECT authors, COUNT(*) FROM books GROUP BY authors")
    result = c.fetchall()
    return result


def mean_length(conn):
    c = conn.cursor()
    c.execute("SELECT AVG(number_of_pages) FROM books")
    result = c.fetchall()
    return result


def read_books(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM books WHERE read = 1")
    result = c.fetchall()
    return result


def sum_pages(conn):
    c = conn.cursor()
    c.execute("SELECT SUM(number_of_pages) FROM books WHERE read = 1")
    result = c.fetchall()
    return result[0][0]
    

def get_books(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    result = c.fetchall()
    return result    

if __name__ == "__main__":
    conn = sqlite3.connect("books.db")
    print(sort_by_pages(conn, "DESC"))