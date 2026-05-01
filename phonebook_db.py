import sqlite3

def main():
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Entries (
            Name TEXT,
            Phone TEXT
        )
    """)
    cur.execute("DELETE FROM Entries")

    sample = [
        ("Caiden", "612-391-4820"),
        ("Josiah", "651-204-9183"),
        ("Nicholas", "763-550-1092"),
        ("Adrian", "952-781-6630"),
        ("Kaelen", "612-447-2908"),
        ("Grace", "651-903-7745"),
        ("Jamel", "763-118-5629"),
        ("Elliott", "952-330-1847"),
        ("Nolan", "612-889-2031"),
        ("Sam", "612-839-4721"),
        ("Luke", "651-204-9183"),
        ("Javan", "763-550-1092"),
        ("Wesley", "952-781-6630"),
        ("Abraham", "612-447-2908")
    ]


    cur.executemany("INSERT INTO Entries VALUES (?, ?)", sample)

    conn.commit()
    conn.close()

    print("Phonebook database is ready.")

if __name__ == "__main__":
    main()