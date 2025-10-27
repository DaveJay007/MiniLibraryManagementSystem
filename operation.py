class Book:
    def __init__(self, isbn, title, author, genre, total):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre = genre
        self.total = total
        self.available = total


class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed = []


class Library:
    GENRES = ("Fiction", "Non-Fiction", "Sci-Fi", "Programming")

    def __init__(self):
        self.books = {}
        self.members = []

    def add_book(self, isbn, title, author, genre, total):
        if isbn in self.books:
            print("Book already exists")
            return
        if genre not in self.GENRES:
            print("Invalid genre choose from", self.GENRES)
            return
        self.books[isbn] = Book(isbn, title, author, genre, total)
        print("Book added:", title)

    def add_member(self, member_id, name, email):
        for m in self.members:
            if m.member_id == member_id:
                print("Member already exists")
                return
        self.members.append(Member(member_id, name, email))
        print("Member added:", name)

    def search_books(self, word):
        found = 0
        for b in self.books.values():
            if word.lower() in b.title.lower() or word.lower() in b.author.lower():
                print(b.isbn, "-", b.title, "by", b.author, "| Available:", b.available)
                found += 1
        if found == 0:
            print("No books found.")

    def borrow_book(self, member_id, isbn):
        member = None
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break
        if not member:
            print("Member not found!")
            return
        if isbn not in self.books:
            print("Book not found!")
            return
        book = self.books[isbn]
        if book.available == 0:
            print("No copies left!")
            return
        if len(member.borrowed) >= 3:
            print("Borrow limit reached!")
            return
        book.available -= 1
        member.borrowed.append(isbn)
        print(member.name, "borrowed", book.title)

    def return_book(self, member_id, isbn):
        for m in self.members:
            if m.member_id == member_id:
                if isbn in m.borrowed:
                    m.borrowed.remove(isbn)
                    self.books[isbn].available += 1
                    print(m.name, "returned", self.books[isbn].title)
                    return
        print("Book not borrowed or member not found!")

    def delete_book(self, isbn):
        if isbn in self.books:
            b = self.books[isbn]
            if b.available != b.total:
                print("Can't delete, some copies are borrowed.")
                return
            del self.books[isbn]
            print("Book deleted!")
        else:
            print("Book not found!")

    def delete_member(self, member_id):
        for m in self.members:
            if m.member_id == member_id:
                if m.borrowed:
                    print("Can't delete, member has borrowed books.")
                    return
                self.members.remove(m)
                print("Member deleted!")
                return
        print("Member not found!")

    def view_books(self):
        if not self.books:
            print("No books yet.")
            return
        print("\nBooks in library:")
        for b in self.books.values():
            print(b.isbn, "-", b.title, "|", b.author, "|", b.available, "of", b.total, "available")

    def view_members(self):
        if not self.members:
            print("No members yet.")
            return
        print("\nLibrary Members:")
        for m in self.members:
            print(m.member_id, "-", m.name, "| Borrowed:", m.borrowed)


def menu():
    print("\n==== MINI LIBRARY MENU ====")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. View All Books")
    print("7. View All Members")
    print("8. Delete Book")
    print("9. Delete Member")
    print("0. Exit")


if __name__ == "__main__":
    lib = Library()
    while True:
        menu()
        c = input("Choose: ")
        if c == "1":
            i = input("ISBN: ")
            t = input("Title: ")
            a = input("Author: ")
            g = input(f"Genre {lib.GENRES}: ")
            n = int(input("Total copies: "))
            lib.add_book(i, t, a, g, n)
        elif c == "2":
            i = input("Member ID: ")
            n = input("Name: ")
            e = input("Email: ")
            lib.add_member(i, n, e)
        elif c == "3":
            word = input("Enter title or author: ")
            lib.search_books(word)
        elif c == "4":
            i = input("Member ID: ")
            b = input("Book ISBN: ")
            lib.borrow_book(i, b)
        elif c == "5":
            i = input("Member ID: ")
            b = input("Book ISBN: ")
            lib.return_book(i, b)
        elif c == "6":
            lib.view_books()
        elif c == "7":
            lib.view_members()
        elif c == "8":
            i = input("ISBN to delete: ")
            lib.delete_book(i)
        elif c == "9":
            i = input("Member ID to delete: ")
            lib.delete_member(i)
        elif c == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")