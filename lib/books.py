import sqlite3

con = sqlite3.connect('LMS.db')
cur = con.cursor()

class CLIStoreBook:
    def __init__(self):
        pass  # You can perform any necessary initialization here

    def save_book(self, book_name, author, book_pages):
        """
        Saves the book and updates the database
        """
        if book_name != '' and author != '' and book_pages != '':
            try:
                query = "INSERT INTO books(book_name, author, book_pages) VALUES (?, ?, ?)"
                cur.execute(query, (book_name, author, book_pages))
                con.commit()
                print('Book has been saved successfully')
            except:
                print('Transaction failed!')
        else:
            print('All fields are required!')

    def run(self):
        print("CLI Library Management System")
        while True:
            print("\n1. Add New Book")
            print("2. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                book_name = input("Enter book name: ")
                author = input("Enter author name: ")
                book_pages = input("Enter book pages: ")
                self.save_book(book_name, author, book_pages)
            elif choice == '2':
                print("Exiting the Library Management System.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    cli_store_book = CLIStoreBook()
    cli_store_book.run()
