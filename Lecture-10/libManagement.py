import json


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author
        }


class Library:
    file_name = "library.json"

    def load_data(self):
        try:
            with open(self.file_name, "r") as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            return []

    def save_data(self, data):
        with open(self.file_name, "w") as f:
            json.dump(data, f, indent=4)

    def create_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")

        book = Book(title, author)

        data = self.load_data()
        data.append(book.to_dict())
        self.save_data(data)

        print("Book added successfully.")

    def read_books(self):
        data = self.load_data()

        if not data:
            print("No books in library.")
            return

        print("\n===== Library Books =====")
        for index, b in enumerate(data, start=1):
            print(f"{index}. Title: {b['title']}, Author: {b['author']}")

    def update_book(self):
        title = input("Enter the title of book to update: ")

        data = self.load_data()
        found = False

        for b in data:
            if b["title"].lower() == title.lower():
                new_title = input("Enter new book title: ")
                new_author = input("Enter new book author: ")

                b["title"] = new_title
                b["author"] = new_author

                found = True
                break

        if found:
            self.save_data(data)
            print("Book updated successfully.")
        else:
            print("Book not found.")

    def delete_book(self):
        title = input("Enter the title of book to delete: ")

        data = self.load_data()
        found = False

        for b in data:
            if b["title"].lower() == title.lower():
                data.remove(b)
                found = True
                break

        if found:
            self.save_data(data)
            print("Book deleted successfully.")
        else:
            print("Book not found.")


library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.create_book()

    elif choice == "2":
        library.read_books()

    elif choice == "3":
        library.update_book()

    elif choice == "4":
        library.delete_book()

    elif choice == "5":
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")