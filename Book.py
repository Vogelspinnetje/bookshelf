class Book:
    def __init__(self, isbn, title, authors, publish_date, number_of_pages, read):
        self.isbn = isbn
        self.title = title
        self.authors = authors
        self.publish_date = publish_date
        self.number_of_pages = number_of_pages
        self.read = read
        
    def save_book(self, conn):
        c = conn.cursor()
        c.execute("INSERT OR REPLACE INTO books VALUES (?,?,?,?,?,?)",(self.isbn, self.title, self.authors, self.publish_date, self.number_of_pages, int(self.read)))
        conn.commit()
        
    def __str__(self):
        return f"{self.title} - {self.authors}\nPublished: {self.publish_date}\nNumber of pages: {self.number_of_pages}\nRead: {'✓' if self.read else '✗'}"