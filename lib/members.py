import sqlite3

con = sqlite3.connect('LMS.db')
cur = con.cursor()

class CLIMemberStore:
    def __init__(self):
        pass  # You can perform any necessary initialization here

    def save_member(self, name, phone):
        """
        Adds a member to the library and updates the database
        """
        if name != '' and phone != '':
            try:
                query = "INSERT INTO member(name, phone) VALUES (?, ?)"
                cur.execute(query, (name, phone))
                con.commit()
                print('Member is created!')
            except:
                print('Transaction failed!')
        else:
            print('All fields are required!')

    def run(self):
        print("CLI Library Management System")
        while True:
            print("\n1. Add New Member")
            print("2. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter member name: ")
                phone = input("Enter phone: ")
                self.save_member(name, phone)
            elif choice == '2':
                print("Exiting the Library Management System.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    cli_member_store = CLIMemberStore()
    cli_member_store.run()
