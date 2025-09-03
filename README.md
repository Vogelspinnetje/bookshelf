# Bookshelf
## Introduction
Bookshelf is a small project for scanning book barcodes and automatically storing them in a **SQLite** database. It uses a webcam, Open Library API, and some custom scripts to keep track of your personal library. It is still in concept. For now, you will have to run the scripts separately.

## create_db.py
Creates a **SQLite** database, essentially the bookshelf.

## scanner.py
This code uses the **cv2** library to scan barcodes via a webcam. Then these barcodes are parsed through the **Open Library API**, which, hopefully, returns information about the scanned book.

## fill_db.py
Uses **scanner.py** to scan the barcodes and look them up through the **API**. If there is some information about the book missing, the program allows the user to fill in this information. Then the information will be stored in the **SQLite** database.

## Book.py
This is the book **class**. Maybe not really necessary, but I am just trying to get used to using classes.

## insight.py
A bunch of pre-written **SQL** queries to get details/statistics of your bookshelf
