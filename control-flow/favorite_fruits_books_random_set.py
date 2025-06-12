# Creating a list of favorite fruits
favorite_fruits = ["Mango", "Strawberry", "Banana", "Pineapple"]

# Accessing the second element (index 1) and printing it
print("Second favorite fruit:", favorite_fruits[1])

# Creating a dictionary with book information
favorite_book = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "genre": "Fiction",
}

# Retrieving the genre using the get method
book_genre = favorite_book.get("genre")
print("Genre of favorite book:", book_genre)

import random

# Generate a list of 10 random numbers between 1 and 10
random_numbers = [random.randint(1, 10) for _ in range(10)]

# Use a set to remove duplicates
unique_numbers = set(random_numbers)

# Display the results 
print("Original random numbers:", random_numbers)
print("Unique numbers:", unique_numbers)

