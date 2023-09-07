import sqlite3

con = sqlite3.connect('LMS.db')
cur = con.cursor()

class CLIIssueBook:
    def __init__(self):
        pass  # You can perform any necessary initialization here

    def issue_book(self, book_id, member_id):
        """
        Issues the book to the given member and updates the database
        """
        try:
            query = "INSERT INTO issuedbooks(book_id, member_id) VALUES (?, ?)"
            cur.execute(query, (book_id, member_id))
            con.commit()
            cur.execute("UPDATE books SET book_status=1 WHERE book_id=?", (book_id,))
            con.commit()
            print("Book has been issued successfully!")
        except:
            print("Transaction not committed")

    def run(self):
        print("CLI Library Management System")
        while True:
            print("\n1. Issue Book")
            print("2. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                book_id = input("Enter book ID: ")
                member_id = input("Enter member ID: ")
                self.issue_book(book_id, member_id)
            elif choice == '2':
                print("Exiting the Library Management System.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    cli_issue_book = CLIIssueBook()
    cli_issue_book.run()
