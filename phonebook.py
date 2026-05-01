import sqlite3

def main():
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()

    while True:
        print("\n--- SAM'S CONTACT LIST MENU ---")
        print("1. View all the contacts")
        print("2. Change a phone number")
        print("3. Delete a contact")
        print("4. Quit")

        choice = input(" Please enter your choice of action: ")


        if choice == "1":
            cur.execute("SELECT * FROM Entries")
            rows = cur.fetchall()

            print("\nName        Phone")
            print("------------------------")
            for r in rows:
                print(f"{r[0]:<12}{r[1]}")

        # UPDATE
        elif choice == "2":
            name = input("Enter name you would like to update: ")
            new_phone = input("Enter the new phone number: ")

            cur.execute(
                "UPDATE Entries SET Phone = ? WHERE Name = ?",
                (new_phone, name)
            )
            conn.commit()
            print("Updated.")

        # DELETE
        elif choice == "3":
            name = input("Enter name you would like to delete: ")

            cur.execute(
                "DELETE FROM Entries WHERE Name = ?",
                (name,)
            )
            conn.commit()
            print("Deleted.")

        # QUIT
        elif choice == "4":
            break

        else:
            print("Invalid choice, please try again.")

    conn.close()

if __name__ == "__main__":
    main()