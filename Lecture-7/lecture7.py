# Sets kya hote hain python mein?# Sets ek unordered collection hota hai jisme unique elements hote hain. 
# Iska use tab hota hai jab hume duplicate values ko remove karna hota hai ya phir set operations jaise union, intersection, difference perform karna hota hai.
# Set banane ke liye hum curly braces {} ka use karte hain ya phir set() function ka use kar sakte hain.
# Example of creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
# Example of creating a set using set() function
my_set2 = set([1, 2, 3, 4, 5])
print(my_set2)  # Output: {1, 2, 3, 4, 5}
# Sets mein duplicate values nahi hoti hain, agar aap duplicate values add karne ki koshish karenge to wo ignore kar di jayengi.
my_set.add(3)  # This will not add 3 again since it's already in the set
print(my_set)  # Output: {1, 2, 3, 4, 5}
# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
# Union
union_set = set_a.union(set_b)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}
# Intersection
intersection_set = set_a.intersection(set_b)
print(intersection_set)  # Output: {3, 4}   
# Difference
difference_set = set_a.difference(set_b)
print(difference_set)  # Output: {1, 2}
# Symmetric Difference
sym_diff_set = set_a.symmetric_difference(set_b)
print(sym_diff_set)  # Output: {1, 2, 5, 6}



# tuple kya hote hain python mein?# Tuple ek ordered collection hota hai jisme elements immutable hote hain, yani ki unhe change nahi kiya ja sakta.
# Tuple banane ke liye hum parentheses () ka use karte hain.
# Example of creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)
# Tuple ke elements ko change nahi kiya ja sakta, agar aap try karenge to aapko error milega.
# my_tuple[0] = 10  # This will raise a TypeError
# Tuple ke elements ko access karne ke liye hum indexing ka use karte hain.
print(my_tuple[0])  # Output: 1
print(my_tuple[1:4])  # Output: (2, 3, 4)
# Tuple ke andar hum different types ke elements rakh sakte hain.
mixed_tuple = (1, "Hello", 3.14, [1, 2, 3])
print(mixed_tuple)  # Output: (1, 'Hello', 3.14, [1, 2, 3])

city = ("khi", "hyd", "lhr")
country = "pak", "india", "china"
print(city[0])  # Output: "khi"
print(country[1])  # Output: "india"

numbers = (1,2,3,4,5,6,7,8,9,21,34,56,)
print(numbers[3])  # Output: 4
print(numbers[-5 : -1]) # Output: (5, 6, 7, 8)   # start, stop, end






# dictionary kya hote hain python mein?# Dictionary ek unordered collection hota hai jisme key-value pairs hote hain.
# Dictionary banane ke liye hum curly braces {} ka use karte hain aur key-value pairs ko colon : se separate karte hain.
# Example of creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Dictionary ke elements ko access karne ke liye hum keys ka use karte hain.
print(my_dict["name"])  # Output: "Alice"
print(my_dict["age"])   # Output: 30
# Dictionary ke elements ko change karne ke liye hum keys ka use karte hain.
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}
# Dictionary ke andar hum different types ke keys aur values rakh sakte hain.
mixed_dict = {
    "name": "Bob",
    "age": 25,
    "is_student": True,
    "hobbies": ["reading", "gaming", "coding"]
}
print(mixed_dict)  # Output: {'name': 'Bob', 'age': 25, 'is_student': True, 'hobbies': ['reading', 'gaming', 'coding']}
# Dictionary ke andar hum nested dictionaries bhi rakh sakte hain.
nested_dict = {
    "person1": {
        "name": "Alice",
        "age": 30
    },
    "person2": {
        "name": "Bob",
        "age": 25
    }
}
print(nested_dict)  # Output: {'person1': {'name': 'Alice', 'age': 30}, 'person2': {'name': 'Bob', 'age': 25}}

