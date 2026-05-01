#Author: Sam Gaines
#Date:5/1/2026
#Title: Cites Data Base


import sqlite3

def main():
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()
#prints off the different options
    while True:
        print("\n--- Cities Database Menu ---")
        print("1. Cities by population ascending")
        print("2. Cities by population descending")
        print("3. Cities by name")
        print("4. Total population")
        print("5. Average population")
        print("6. City with highest population")
        print("7. City with lowest population")
        print("8. Quit")
        #Tells the user to pick a number
        choice = input(" Please enter the number for your choice: ")

        if choice == "1":
            cur.execute("SELECT * FROM Cities ORDER BY Population ASC")
            show(cur.fetchall())

        elif choice == "2":
            cur.execute("SELECT * FROM Cities ORDER BY Population DESC")
            show(cur.fetchall())

        elif choice == "3":
            cur.execute("SELECT * FROM Cities ORDER BY CityName ASC")
            show(cur.fetchall())

        elif choice == "4":
            cur.execute("SELECT SUM(Population) FROM Cities")
            print("Total population:", cur.fetchone()[0])

        elif choice == "5":
            cur.execute("SELECT AVG(Population) FROM Cities")
            print("Average population:", cur.fetchone()[0])

        elif choice == "6":
            cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population DESC LIMIT 1")
            print("The city with the highest population:", cur.fetchone())

        elif choice == "7":
            cur.execute("SELECT CityName, Population FROM Cities ORDER BY Population ASC LIMIT 1")
            print("Lowest:", cur.fetchone())

        elif choice == "8":
            break

        else:
            print("Invalid choice")

    conn.close()

def show(rows):
    print("\nCityID  CityName            Population")
    print("--------------------------------------")
    for r in rows:
        print(f"{r[0]:<7}{r[1]:20}{r[2]:,}")

if __name__ == "__main__":
    main()