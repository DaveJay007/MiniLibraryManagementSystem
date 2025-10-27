Mini Library Management System

Overview

The Mini Library Management System is a simple Python application that allows users to manage a library’s books and members. It supports adding, searching, borrowing, returning, viewing, and deleting books and members. The system is designed to be beginner-friendly and easy to understand.

⸻

Features
	•	Add new books with ISBN, title, author, genre, and total copies.
	•	Add new members with unique ID, name, and email.
	•	Search for books by title or author.
	•	Borrow books (limit 3 books per member).
	•	Return borrowed books.
	•	View all books and their availability.
	•	View all library members and their borrowed books.
	•	Delete books (if no copies are borrowed).
	•	Delete members (if they have no borrowed books).

⸻

Technologies Used
	•	Python 3
	•	Object-Oriented Programming (OOP) concepts

⸻

Installation
	1.	Make sure Python 3 is installed on your computer.
	2.	Clone or download the repository.
	3.	Open the terminal/command prompt and navigate to the project folder.
	4.	Run the program:
  python filename.py

  (Replace filename.py with the name of your main Python file, e.g., library.py)

⸻

How to Use
	1.	Run the program.
	2.	Choose an option from the menu:
	•	1 to add a book
	•	2 to add a member
	•	3 to search for books
	•	4 to borrow a book
	•	5 to return a book
	•	6 to view all books
	•	7 to view all members
	•	8 to delete a book
	•	9 to delete a member
	•	0 to exit the program
	3.	Follow the prompts for input (e.g., ISBN, title, member ID).

⸻

Sample Usage
Choose: 1
ISBN: 978-123456
Title: Python Basics
Author: Samuel Bangura
Genre: Programming
Total copies: 3
Book added: Python Basics

Choose: 4
Member ID: M001
Book ISBN: 978-123456
Samuel borrowed Python Basics

Notes
	•	A member can borrow a maximum of 3 books at a time.
	•	A book cannot be deleted if copies are currently borrowed.
	•	A member cannot be deleted if they have borrowed books.
	•	Valid genres are: "Fiction", "Non-Fiction", "Sci-Fi", "Programming"

⸻

License

This project is open-source and free to use for learning purposes.
