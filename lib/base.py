import sqlite3

class LibraryManager:
    def __init__(self):
        self.con = sqlite3.connect('LMS.db')
        self.cur = self.con.cursor()

    def show_summary(self):
        """
        Get queryset from the DB and show the details of
        books not issued, members count, and books issued
        on the summary panel
        """
        book_instock_counter = self.cur.execute("SELECT COUNT(book_id) FROM books WHERE book_status").fetchall()
        member_counter = self.cur.execute("SELECT COUNT(member_id) FROM member").fetchall()
        issued_counter = self.cur.execute("SELECT COUNT(book_id) FROM books WHERE book_status=1").fetchall()
        print("IN STOCK:", book_instock_counter[0][0])
        print("MEMBERS:", member_counter[0][0])
        print("ISSUED:", issued_counter[0][0])

    def show_books(self):
        """
        Display all books of the library to the user
        """
        books = self.cur.execute("SELECT * FROM books").fetchall()
        for book in books:
            print(f"{book[0]}-{book[1]}")

    def search_sort_books(self, choice):
        """
        Sorting all the books based on the user's choice
        """
        query = ''
        if choice == 1:
            query = "SELECT * FROM books ORDER BY book_name"
        elif choice == 2:
            query = "SELECT * FROM books WHERE book_status = 0"
        else:
            query = "SELECT * FROM books WHERE book_status = 1"

        books = self.cur.execute(query).fetchall()
        for book in books:
            print(f"{book[0]}-{book[1]}")

    def issue_book(self):
        """
        Issues a book to a member
        """
        pass  # Implement this functionality

    def add_new_book(self):
        """
        Add a new book to the library
        """
        pass  # Implement this functionality

    def add_new_member(self):
        """
        Add a new member to the library
        """
        pass  # Implement this functionality

    def search_books(self, keyword):
        """
        Search for books in the library
        """
        books = self.cur.execute("SELECT * FROM books WHERE book_name LIKE ?", ('%' + keyword + '%',)).fetchall()
        for book in books:
            print(f"{book[0]}-{book[1]}")


def main():
    library_manager = LibraryManager()
    while True:
        print("\nLibrary Management System")
        print("1. Show Summary")
        print("2. Show All Books")
        print("3. Sort Books")
        print("4. Issue Book")
        print("5. Add New Book")
        print("6. Add New Member")
        print("7. Search Books")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            library_manager.show_summary()
        elif choice == '2':
            library_manager.show_books()
        elif choice == '3':
            sort_choice = int(input("Sort by:\n1. All Books\n2. Books Available\n3. Books Issued\nEnter choice: "))
            library_manager.search_sort_books(sort_choice)
        elif choice == '4':
            library_manager.issue_book()
        elif choice == '5':
            library_manager.add_new_book()
        elif choice == '6':
            library_manager.add_new_member()
        elif choice == '7':
            keyword = input("Enter a keyword to search: ")
            library_manager.search_books(keyword)
        elif choice == '8':
            print("Exiting the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
