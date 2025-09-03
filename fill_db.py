import scanner
from Book import Book
import sqlite3


def manually_enter_details():
    title = input("Enter the title: ")
    authors = input("Enter the author: ")
    publish_date = input("Enter the publish_date: ")
    number_of_pages = input("Enter the number of pages: ")
    read = input("Have you already read this book? (Y/n): ")
    read = True if read == "Y" else False
    
    info = {
            "title": title,
            "authors": authors,
            "publish_date": publish_date,
            "number_of_pages": number_of_pages,
            "read": read
        }
    
    return info

def check_info(info):
    for keys in info:
        if info[keys] == "":
            new_val = input(f"Program couldn't find {keys}. Enter it yourself: ")
            info[keys] = new_val
                
    read = input("Have you read the book? (Y/n)")
    info["read"] = True if read == "Y" else False
            
    return info

def main():
    conn = sqlite3.connect("books.db")
    
    while True:
        isbn = scanner.get_barcode()
        info = scanner.lookup_isbn(isbn)
        
        if info == None:
            correct = input(f"Book not found!\nISBN: {isbn}\nIs the ISBN correct? (Y/n): ")
            
            if correct == "Y":
                info = manually_enter_details()
            else:
                print("Scanning again:")
                continue
        else:
            info_new = check_info(info)  
        
        book = Book(isbn, info["title"], info["authors"], info["publish_date"], info["number_of_pages"], info["read"])
        print(book)
        book.save_book(conn)
        
        if input("Scan another book? Typ Y: ") != "Y":
            break

if __name__ == "__main__":
    main()