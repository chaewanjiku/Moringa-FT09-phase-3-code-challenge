import sqlite3  # Import the SQLite3 module to interact with the SQLite database

# Function to establish a connection to the database
def get_db_connection():
    return sqlite3.connect('/home/charity/Development/Phase-3/Moringa-FT09-phase-3-code-challenge/database/magazine.db')

# Class to represent an Article
class Article:
    # Initialize the Article instance with id, title, content, author_id, and magazine_id
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    # Property to get the author's name for this article
    @property
    def author(self):
        conn = get_db_connection()  # Establish database connection
        cursor = conn.cursor()  # Create a cursor object to interact with the database
        cursor.execute('SELECT name FROM authors WHERE id = ?', (self.author_id,))  # Execute a query to get the author's name
        author_name = cursor.fetchone()[0] if cursor.fetchone() else None  # Fetch the first result if it exists
        conn.close()  # Close the database connection
        return author_name  # Return the author's name

    # Property to get the magazine's name for this article
    @property
    def magazine(self):
        conn = get_db_connection()  # Establish database connection
        cursor = conn.cursor()  # Create a cursor object to interact with the database
        cursor.execute('SELECT name FROM magazines WHERE id = ?', (self.magazine_id,))  # Execute a query to get the magazine's name
        magazine_name = cursor.fetchone()[0] if cursor.fetchone() else None  # Fetch the first result if it exists
        conn.close()  # Close the database connection
        return magazine_name  # Return the magazine's name
    
    # Class method to find an Article by its ID
    @classmethod
    def find_by_id(cls, article_id):
        conn = get_db_connection()  # Establish database connection
        cursor = conn.cursor()  # Create a cursor object to interact with the database
        cursor.execute('SELECT * FROM articles WHERE id = ?', (article_id,))  # Execute a query to find the article by ID
        row = cursor.fetchone()  # Fetch the first result if it exists
        conn.close()  # Close the database connection
        if row:
            return cls(*row)  # Return an instance of Article initialized with the row data
        return None  # Return None if no article is found
