# use sql lite database
import sqlite3
from sqlite3 import Error # import Error if no import - throws error

# Function to create connection to the database
def create_connection():
    # create a database connection
    conn = None
    try:# connect to database
        conn = sqlite3.connect('hipster_cookbooks.db');
        print(f"Successfully connected to sqlite {sqlite3.version} ")
        return conn
    except Error as e: # if no connection print message
        print(f"Error establishing connection within void: {e}")
        return None
    
# function to create a table for storing the cookbooks
def create_table(conn):
    # create a table structure
    try:
        sql_create_cookbooks_table = '''
        CREATE TABLE IF NOT EXISTS cookbooks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year_published INTEGER,
            aesthetic_rating INTEGER,
            instagram_worthy BOOLEAN,
            cover_color TEXT
        );
        '''
        # need cursor for working with database
        # calling constructor for cursor object to create new cursor
        cursor = conn.cursor()
        cursor.execute(sql_create_cookbooks_table)
        print("Successfully created a database structure")
    except Error as e:
        print(f"Error creating table: {e} ")

# new function needs conn to connect to database and the cookbook
def insert_cookbook(conn, cookbook):
    # add new cookbook to your shelf
    # hold sql query to execute against sqlite database
    sql = '''INSERT INTO cookbooks(title, author, year_published, aesthetic_rating,
            instagram_worthy, cover_color)
            VALUES(?,?,?,?,?,?)'''
    

    # USE the connection to the DB to insert the new record
    try:
        # create cursor this is like a pointer that lets us traverse database
        cursor = conn.cursor()
        cursor.execute(sql, cookbook)
        # commit the changes
        conn.commit()
        print(f"Successfully curated the cookbook with the id: {cursor.lastrowid}")
    except Error as e:
        print(f"Error adding to collection: {e}")
        return None
    
# function to retrieve cookbooks from the database
def get_all_cookbooks(conn):
    # browse your entire collection of cookbooks
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cookbooks")
        # put the result set of cookbooks into a list called books
        books = cursor.fetchall()

        # Iterate through the list of books & display info for each cookbook
        for book in books:
            print(f"ID: {book[0]}") # output value at index 0
            print(f"Title: {book[1]}") # index 1 and so on
            print(f"Author: {book[2]}")
            print(f"Published: {book[3]}(oooold book)")
            print(f"Aesthetic Rating: {book[4]}")
            print(f"Instagram Worthy: {'Yes' if book[5] else 'Not Aesthetic Enough'}")
            print(f"Cover Color: {book[6]}")
            print(f"---") # separate by line of hyphens
        return books # return book list
    except Error as e:
        print(f"Error retrieving collection: {e}")
        return[] # return empty list if cannot return list of books
    
# Main function is called when the program executes
# Main function directs the program and calls functions in program
def main():
    # Establish a connection to our database
    conn = create_connection()

    # test if the connection is viable
    if conn is not None:
        # create our table
        create_table(conn) # pass database connection to create_table function

        # insert some cookbooks with corresponding values
        cookbooks = [
            ("Foraged & Found: A Guide to Pretending You Know About Mushrooms",
             "Oak Wavelength", 2023, 5, True, "Forest Green"),
             ('Small Batch: 50 Recipes You Will Never Actually Make', 'Sage Moonbeam', 2022, 4, True, 'Raw Linen'),
             ('How To Find Wild Turkeys: A Guide to Turkey Woods Woodsmanship', 'Gooble Spurs', 2007, 5, True, 'Hickory'),
             ('The Artistic Oak: Advanced Avocado Techniques', 'River Wildflower', 2023, 5, True, 'Recycled Brown'),
             ('Fermented Everything', 'Jim Kombucha', 2021, 3, True, 'Denim'),
             ('The Deconstructed Sandwich: Making Simple Things Complicated', 'Juniper Vinegar Smith', 2023, 5, True, 'Beige')
        ]

        # Display list of cookbooks
        print("\nCurating your cookbook collection. . . .")
        # loop thru list of cookbooks
        for cookbook in cookbooks:
            insert_cookbook(conn, cookbook) # pass connection & current cookbook

        # get cookbooks from database
        print("\nYour carefully curated collection:")
        get_all_cookbooks(conn) # pass connection so it does its job

        # close the database connection
        conn.close()

        print("\nThe database connection is closed!")
    # if cannot connect to db need and else case
    else:
        print("Error! No database connections - get better wifi!")

# Code to call the main function
if __name__== '__main__':
    main()
