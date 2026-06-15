# ============================================================
# JSON module import kiya — yeh Python ka built-in module hai
# iske zariye hum data ko .json file mein save aur load kar sakte hain
# ============================================================
import json


# ============================================================
# BOOK CLASS — ek akeli book ko represent karta hai
# ============================================================
class Book:

    # jab bhi Book() likhein, yeh method automatically chalta hai
    # title aur author bahar se pass kiye jate hain
    def __init__(self, title, author):
        self.title = title    # title is object mein save ho gaya
        self.author = author  # author bhi save ho gaya

    # yeh method book object ko dictionary mein badalta hai
    # kyunki JSON file mein object seedha save nahi hota — dict hona chahiye
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author
        }


# ============================================================
# LIBRARY CLASS — file operations aur CRUD sab yahan hoga
# ============================================================
class Library:

    # class-level variable — sabhi methods mein same file naam use hoga
    # alag se har jagah likhne ki zaroorat nahi
    file_name = "library.json"

    # ----------------------------------------------------------
    # load_data() — JSON file se books ka data uthata hai
    # ----------------------------------------------------------
    def load_data(self):
        try:
            # file "r" (read) mode mein khola
            # with open() use kiya taake file automatically band ho jaye
            with open(self.file_name, "r") as f:
                data = json.load(f)  # JSON file ko Python list mein convert kiya
                return data
        except FileNotFoundError:
            # agar file exist nahi karti (pehli baar run ho raha hai)
            # to crash hone ki bajaye empty list return karo
            return []

    # ----------------------------------------------------------
    # save_data() — data ko JSON file mein likh deta hai
    # ----------------------------------------------------------
    def save_data(self, data):
        # "w" (write) mode: file pehle se ho to overwrite, nahi ho to naya banao
        with open(self.file_name, "w") as f:
            # indent=4: file readable format mein hogi, sab ek line mein nahi
            json.dump(data, f, indent=4)

    # ----------------------------------------------------------
    # create_book() — nayi book add karna | C in CRUD
    # ----------------------------------------------------------
    def create_book(self):
        title = input("Enter book title: ")   # user se title lo
        author = input("Enter book author: ") # user se author lo

        # Book object banaya in values se
        book = Book(title, author)

        # pehle existing books load karo — taake purani books na kat jayein
        data = self.load_data()

        # nai book ko dict mein badal ke list ke andar add karo
        data.append(book.to_dict())

        # poori updated list wapas file mein save karo
        self.save_data(data)

        print("Book added successfully.")

    # ----------------------------------------------------------
    # read_books() — saari books dikhana | R in CRUD
    # ----------------------------------------------------------
    def read_books(self):
        data = self.load_data()  # file se books uthao

        # agar koi book nahi hai to message dikhao aur bahar nikal jao
        if not data:
            print("No books in library.")
            return  # yahan se function khatam — neche ka code nahi chalega

        print("\n===== Library Books =====")

        # enumerate(data, start=1): index 0 ki bajaye 1 se shuru hoga
        # taake user ko 1, 2, 3 dikhe — 0, 1, 2 nahi
        for index, b in enumerate(data, start=1):
            # f-string se formatted output print ho raha hai
            print(f"{index}. Title: {b['title']}, Author: {b['author']}")

    # ----------------------------------------------------------
    # update_book() — book edit karna | U in CRUD
    # ----------------------------------------------------------
    def update_book(self):
        # pehle user se purana title lo — isse dhundhenge
        title = input("Enter the title of book to update: ")

        data = self.load_data()  # file se books uthao
        found = False            # flag: book mili ya nahi — abhi tak nahi mili

        for b in data:
            # .lower() dono taraf: "Python" aur "python" same maana jayenge
            if b["title"].lower() == title.lower():

                # match mil gayi — ab naya data lo user se
                new_title = input("Enter new book title: ")
                new_author = input("Enter new book author: ")

                # dictionary ki values update kar do
                b["title"] = new_title
                b["author"] = new_author

                found = True  # flag set karo — book mil gayi
                break         # ab baaki loop chalane ki zaroorat nahi

        if found:
            self.save_data(data)  # updated list save karo
            print("Book updated successfully.")
        else:
            print("Book not found.")  # loop poora chala, koi match nahi mila

    # ----------------------------------------------------------
    # delete_book() — book hatana | D in CRUD
    # ----------------------------------------------------------
    def delete_book(self):
        # user se woh title lo jise delete karna hai
        title = input("Enter the title of book to delete: ")

        data = self.load_data()  # file se books uthao
        found = False            # flag: book mili ya nahi

        for b in data:
            # case-insensitive match
            if b["title"].lower() == title.lower():
                data.remove(b)  # us book ko list se hata do
                found = True    # flag set karo
                break           # ek match mila — loop band karo

        if found:
            # bachi hui list (bina deleted book ke) save karo
            self.save_data(data)
            print("Book deleted successfully.")
        else:
            print("Book not found.")


# ============================================================
# PROGRAM ENTRY POINT — yahan se execution shuru hoti hai
# ============================================================

# Library ka ek object banaya — ab iske through saare methods call honge
library = Library()

# while True: jab tak user "5" na daale, program chalta rahega
while True:

    # har iteration mein menu print hoga
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice: ")  # user se choice lo

    if choice == "1":
        library.create_book()   # nayi book add karo

    elif choice == "2":
        library.read_books()    # saari books dikha

    elif choice == "3":
        library.update_book()   # book edit karo

    elif choice == "4":
        library.delete_book()   # book delete karo

    elif choice == "5":
        print("Thank you for using Library Management System.")
        break  # while loop yahan khatam — program band ho jata hai

    else:
        # koi bhi aur input aaye to yeh message dikhao aur loop dobara chale
        print("Invalid choice. Please try again.")