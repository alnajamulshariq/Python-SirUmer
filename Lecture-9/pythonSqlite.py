import sqlite3

conn = sqlite3.connect('students.db')

# cursor object banate hain jisse hum SQL commands execute kar sakte hain
cursor = conn.cursor()

# table creation
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age Integer,
    grade TEXT
)
    ''')


# conn.commit() ka matlab hai ke aapne jo bhi changes kiye hain database mein, unko save karna. Jab aap koi table create karte hain ya data insert karte hain, toh wo changes temporary hote hain. conn.commit() use karke aap un changes ko permanent bana dete hain, taake wo database mein store ho jayein aur aap unko future mein access kar sakein. 
# conn.commit()

# print("Table created successfully")



# student ko add karne ke liye function
# def add_student(name, age, grade):
#     cursor.execute(
#         '''
#         INSERT INTO students (name, age, grade)
#         VALUES (?, ?, ?)
#         ''', (name, age, grade)
#     )
# conn.commit()
# print("Students added successfully")

# add_student("Shariq", 26, "A")
# add_student("Ali", 24, "B")
# add_student("Sara", 22, "A")
    
    
    
# students ko retrieve karne ke liye function
def fetch_all_students():
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
fetch_all_students()



# students ko update karne ke liye function
def update_student(student_id, new_name, new_age, new_grade):
    cursor.execute(
        '''
        UPDATE students
        SET name = ?, age = ?, grade = ?
        WHERE id = ?
        ''', (new_name, new_age, new_grade, student_id)
    )
    

update_student(1, "Shariq Ahmed", 27, "A+")
conn.commit()

# students ko fetch karne ke liye function
def fetch_all_students():
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
fetch_all_students()     
        
# delete karne ke liye function id k through
def delete_student(student_id):
    cursor.execute(
        '''
        DELETE FROM students
        WHERE id = ?
        ''', (student_id,)
    )
    conn.commit()
    print(f"Student with ID {student_id} deleted successfully")
    
# delete_student(4)


# students ko fetch karne ke liye function
def fetch_all_students():
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

fetch_all_students()


# connection close karna zaroori hai jab aapka kaam ho jaye database ke saath, taake resources free ho jayein aur data loss na ho. conn.close() use karke aap apne database connection ko properly close kar sakte hain, taake aapke application mein koi issues na aayein aur database secure rahe.
conn.close()
print("Database connection closed")