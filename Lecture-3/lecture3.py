name = "Shariq"
age = 25
weight = 70.5
isActive = True

print(name)
print(type(name))
print(len(name))
print(name, age, weight, isActive)
print(f" my name is {name}. \nmy age is {age}. \n my weight is {weight}. \nmy active status is {isActive}.")

# data types
# string
# integer
# float
# boolean
# type conversion
age_str = str(age)
weight_int = int(weight)
isActive_str = str(isActive)
print(age_str, type(age_str))
print(weight_int, type(weight_int))
print(isActive_str, type(isActive_str))

# operators
a = 10
b = 5
print(a + b)  # addition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division
print(a % b)  # modulus
print(a ** b)  # exponentiation
print(a // b)  # floor division

# comparison operators
print(a == b)  # equal to
print(a != b)  # not equal to
print(a > b)   # greater than
print(a < b)   # less than
print(a >= b)  # greater than or equal to
print(a <= b)  # less than or equal to

# logical operators
x = True
y = False
print(x and y)  # logical AND
print(x or y)   # logical OR
print(not x)    # logical NOT

# conditional statements
if age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")
    
# conditional statements with elif
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")
    
    
# loops
# for loop
for i in range(5):
    print(i)    

# while loop
count = 0
while count < 5:
    print(count)
    count = count + 1 # or count += 1
    