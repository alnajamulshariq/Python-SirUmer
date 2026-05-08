import json 

def add_std (name, age):
    std = {
        "name": name,
        "age": age}
    file = open("Std.json", "a")
    json.dump(std, file)
    file.write("\n")
    file.close()
add_std("Ali", 20)
add_std("Sara", 22)
add_std("Sawati", 19)

