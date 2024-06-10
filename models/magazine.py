import sqlite3  # Import the SQLite3 module to interact with the SQLite database

# Class to represent a Magazine
class Magazine:
    # Initialize the Magazine instance with id, name, and category
    def __init__(self, id, name, category):
        self._id = id
        self._name = name
        self._category = category

    # Property to get the magazine's ID
    @property
    def id(self):
        return self._id

    # Setter to set the magazine's ID
    @id.setter
    def id(self, id):
        # Ensure the ID is an integer
        if isinstance(id, int):
            self._id = id
        else:
            raise ValueError("Magazine id must be of type int")

    # Property to get the magazine's name
    @property
    def name(self):
        return self._name

    # Setter to set the magazine's name with validation
    @name.setter
    def name(self, name):
        # Ensure the name is a string between 2 and 16 characters
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Name must be a string between 2 and 16 characters")

    # Property to get the magazine's category
    @property
    def category(self):
        return self._category

    # Setter to set the magazine's category with validation
    @category.setter
    def category(self, category):
        # Ensure the category is a non-empty string
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string")

    # Method to create the magazine in the database
    def create_magazine(self):
        conn = sqlite3.connect('./database/magazine.db')  # Connect to the database
        cursor = conn.cursor()  # Create a cursor object to interact with the database

        # Insert the magazine's details into the magazines table
        cursor.execute('INSERT INTO magazines (id, name, category) VALUES (?, ?, ?)', 
                       (self._id, self._name, self._category))
        self._id = cursor.lastrowid  # Get the ID of the newly inserted magazine
        conn.commit()  # Commit the transaction
        conn.close()  # Close the database connection

    # Method to test magazine creation
    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")  # Pass id, name, and category arguments
        assert magazine.name == "Tech Weekly"  # Check if the name is set correctly
        assert magazine.category == "Technology"  # Check if the category is set correctly

    # String representation of the Magazine instance
    def __repr__(self):
        return f'<Magazine {self._name}, Category: {self._category}>'
