# uppercase kya karta hai apke string ke har character ko capital letter me convert kar deta hai
name = "shariq najam"
print(name.upper())

# lowercase kya karta hai apke string ke har character ko small letter me convert kar deta hai
print(name.lower())

# title case kya karta hai apke string ke har word ke first character ko capital letter me convert kar deta hai
print(name.title())

# replace kya karta hai apke string ke specified substring ko dusre substring se replace kar deta hai
print(name.replace("shariq", "shariq najam"))

#split kya karta hai apke string ko specified delimiter ke basis par split kar deta hai aur ek list return karta hai
print(name.split())
splitName = name.split()
print(splitName[-1])

# find kya karta hai apke string me specified substring ke first occurrence ka index return kar deta hai, agar substring nahi milta to -1 return karta hai
print(name.find("najam"))

# count kya karta hai apke string me specified substring ke occurrences ki count return kar deta hai
print(name.count("a"))


# List kya hai? List ek ordered collection hota hai jisme multiple items store kiye ja sakte hain. List me items ko index ke through access kiya ja sakta hai, aur list mutable hoti hai, matlab aap list ke items ko change kar sakte hain.
std = ["shariq", "najam", "ali", "hamza"]
print(std[1])

# append kya karta hai apke list ke end me ek naya item add kar deta hai
std.append("hassan")
print(std)

# insert kya karta hai apke list ke specified index par ek naya item add kar deta hai, aur existing items ko shift kar deta hai
std.insert(2, "hussain")
print(std)

# remove kya karta hai apke list se specified item ko remove kar deta hai, agar item multiple times exist karta hai to pehla occurrence remove hota hai
std.remove("hussain")
print(std)


# pop kya karta hai apke list se specified index par item ko remove kar deta hai aur us item ko return kar deta hai, agar index specify nahi kiya jata to last item remove hota hai
std.pop(2)
print(std)


# sort kya karta hai apke list ke items ko ascending order me sort kar deta hai, agar items comparable nahi hote to error aata hai
std_id = [3, 1, 4, 2]
std_id.sort()
print(std_id)


# clear kya karta hai apke list ke saare items ko remove kar deta hai, lekin list khud exist karti hai
std_id.clear()
print(std_id)


# extend kya karta hai apke list me dusre iterable ke items ko add kar deta hai, aur original list ko modify karta hai
std.extend(["hassan", "hussain"])
print(std)


# reverse kya karta hai apke list ke items ko reverse order me arrange kar deta hai
std.reverse()
print(std)


# index kya karta hai apke list me specified item ke first occurrence ka index return kar deta hai, agar item nahi milta to error aata hai
employees = ["shariq", "najam", "ali", "hamza"]
print(employees.index("ali"))



# copy kya karta hai apke list ka ek shallow copy create kar deta hai, jisme original list ke items ke references hote hain, lekin new list me changes karne se original list affect nahi hoti
new_employees = employees.copy()
print(new_employees)

new_employees.extend(["abdul", "malik"])
print(new_employees)

