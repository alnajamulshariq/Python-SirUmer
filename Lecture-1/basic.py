# data types in python
# int, float, str, bool, list, tuple, set, dict
# int
a = 10
print(a)
# float
b = 3.14
print(b)
# str
c = "Hello, World!"
print(c)
# bool
d = True
print(d)
# list
e = [1, 2, 3, 4, 5]
print(e)
# tuple
f = (1, 2, 3, 4, 5)
print(f)
# set
g = {1, 2, 3, 4, 5}
print(g)
# dict
h = {"name": "Alice", "age": 30, "city": "New York"}
print(h)


#type conversion
age = "30"
print(type(age))
updated_age = int(age) + 1
print("Updated age:", updated_age)

#string concatenation
first_name = "Shariq"
last_name = "Najam"
full_name = first_name + " " + last_name
print("Full Name:", full_name)


#list example
name = "Shariq"
age = 28
height = 5.9
is_student = True
sem = 6

st1 = [name, age, height, is_student, sem]
print("student information:", st1)

#methods ti manipulate the list
#append method to add an element to the end of the list
st1.append("Computer Science")
print("Updated student information:", st1)
#remove method to remove an element from the list
st1.remove(28)
print("Updated student information after removing age:", st1)
#insert method to add an element at a specific index
st1.insert(1, 29)
print("Updated student information after inserting age:", st1)
#sort method to sort the list (only works if all elements are of the same type)
numbers = [5, 2, 9, 1, 3]
numbers.sort()
print("Sorted numbers:", numbers)
#reverse method to reverse the order of the list
numbers.reverse()
print("Reversed numbers:", numbers)


