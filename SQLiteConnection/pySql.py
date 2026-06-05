# sqlite3 module import kar rahe hain
# Ye Python ka built-in module hai jo SQLite database ke sath kaam karta hai
import sqlite3


# School.db naam ki database file se connection bana rahe hain
# Agar School.db file pehle se nahi hogi to Python automatically create kar dega
conn = sqlite3.connect("School.db")


# Cursor database mein SQL queries run karne ke liye use hota hai
# Matlab CREATE, INSERT, SELECT, UPDATE, DELETE jaise commands cursor ke through chalte hain
cursor = conn.cursor()


# Students naam ka table create kar rahe hain
# IF NOT EXISTS ka matlab: agar table pehle se mojood hai to dobara create nahi karega
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

# id: har student ka unique number hoga
# INTEGER PRIMARY KEY: id ko primary key bana raha hai
# AUTOINCREMENT: id automatically 1, 2, 3... ke form mein increase hogi
# name TEXT: student ka naam text form mein save hoga
# age INTEGER: student ki age number form mein save hogi


# Table create karne ke baad changes database mein save kar rahe hain
conn.commit()


# while True infinite loop hai
# Is se menu bar bar show hota rahega jab tak user Exit select na kare
while True:
    # Student Management System ka menu print ho raha hai
    print("====Student Management System====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    # User se choice le rahe hain ke woh kya karna chahta hai
    choice = input("Enter your choice: ")

    # Agar user 1 enter kare to new student add hoga
    if choice == "1":
        # Student ka naam input le rahe hain
        name = input("Enter student name: ")

        # Student ki age input le rahe hain
        # int() is liye lagaya hai kyunki age number hoti hai
        age = int(input("Enter student age: "))

        # INSERT query se Students table mein name aur age add kar rahe hain
        # ? placeholders use kiye gaye hain taake data safely insert ho
        cursor.execute(
            "INSERT INTO Students (name, age) VALUES (?, ?)",
            (name, age)
        )

        # Insert ke baad changes database mein save kar rahe hain
        conn.commit()

        # User ko confirmation message show kar rahe hain
        print("Student added successfully!")

    # Agar user 2 enter kare to students ka data show hoga
    elif choice == "2":
        # SELECT query se Students table ka sara data get kar rahe hain
        cursor.execute("SELECT * FROM Students")

        # fetchall() table ke sare records list ki form mein le aata hai
        students = cursor.fetchall()

        # Agar students list empty hai to iska matlab koi student record nahi mila
        if len(students) == 0:
            print("No students found.")
        else:
            # Agar records mojood hain to loop se ek ek record print kar rahe hain
            for row in students:
                print(row)

    # Agar user 3 enter kare to existing student update hoga
    elif choice == "3":
        # Jis student ko update karna hai uski id input le rahe hain
        id = int(input("Enter student id to update: "))

        # New name input le rahe hain
        name = input("Enter new student name: ")

        # New age input le rahe hain
        age = int(input("Enter new student age: "))

        # UPDATE query se selected id wale student ka name aur age update kar rahe hain
        cursor.execute(
            "UPDATE Students SET name = ?, age = ? WHERE id = ?",
            (name, age, id)
        )

        # Update ke baad changes database mein save kar rahe hain
        conn.commit()

        # User ko confirmation message show kar rahe hain
        print("Student updated successfully!")

    # Agar user 4 enter kare to student delete hoga
    elif choice == "4":
        # Jis student ko delete karna hai uski id input le rahe hain
        id = int(input("Enter student id to delete: "))

        # DELETE query se selected id wala student delete kar rahe hain
        cursor.execute("DELETE FROM Students WHERE id = ?", (id,))

        # Delete ke baad changes database mein save kar rahe hain
        conn.commit()

        # User ko confirmation message show kar rahe hain
        print("Student deleted successfully!")

    # Agar user 5 enter kare to program band ho jayega
    elif choice == "5":
        print("Exiting the program. Goodbye!")

        # break loop ko stop kar deta hai
        # Yani program menu se bahar aa jata hai
        break

    # Agar user 1 se 5 ke ilawa kuch aur enter kare
    else:
        print("Invalid choice. Please try again.")


# Program end hone ke baad database connection close kar rahe hain
# Ye good practice hai taake database safely close ho jaye
conn.close()