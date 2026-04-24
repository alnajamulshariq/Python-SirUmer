#functions in python
# without parameters and without return type
# with parameters and with return type
# with parameters and without return type
# without parameters and with return type


# without parameters and without return type
def greet():
    print("Hello")
    
greet()

# with parameters and with return type
def add(a, b):
    return a + b
result = add(5, 3)
print(result)

# with parameters and without return type
def print_message(message):
    print(message)
print_message("This is a message.")

# without parameters and with return type
def get_greeting():
    return "Hello, World!"
greeting = get_greeting()
print(greeting)
    
    
# function example with grade calculation
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'FAILED'
    
res_grade = calculate_grade(85)
print(res_grade)



#check even and odd number with function
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
number = 10
result = check_even_odd(number)
print(f"{number} is {result}.")



# nested function example
def outer_function(x):
    def inner_function(y):
        return y * 2
    return inner_function(x) + 5
result = outer_function(3)
print(result)



# nested function example (simple version)

def outer_function(x):
    print("Yeh OUTER function hai")

    def inner_function(y):
        print("Yeh INNER function hai")
        return y * 2

    result_inner = inner_function(x)
    return result_inner + 5


# function call
result = outer_function(3)

print("Final Result:", result)
