# -*- coding: utf-8 -*-
"""book_tracker

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1o5BBYZCOdci_4UWne5fjD8mr9i2lBHOa
"""

## Create a program that will store book and display all books using dictionaries
## create two separate functions
#empty dictionary
library = {}

#first function: adds a new book to the library and sets its status to available
def add_book():
  title = input("Enter the title of the book: ").title()
  library[title] = "Available"
  print(f"The book '{title}' has been added to the library.")
  print("\n")
  main_menu()

#second function: display all books in the library
def display_books():
  print("\nLibarary Books:")
  for title, status in library.items():
    print(f'{title}: {status}')
  print("\n")
  main_menu()

def main_menu():
  print("Libarary Book Tracker")
  print("1. Add a Book")
  print("2. Display All Books")
  print("3. Exit")
  choice = input("Enter your choice (1-3): ")
  if choice == "1":
    add_book()
  elif choice == "2":
    display_books()
  elif choice == "3":
    print("Goodbye!")
  else:
    print("Invalid choice. Please enter a number between 1 and 3.")
    main_menu()

main_menu()