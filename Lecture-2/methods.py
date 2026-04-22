# ============================================================
# Python OOP - Classes aur Methods
# Topic: Setter aur Getter Methods ka use
# ============================================================

# CLASS kya hai?
# Class ek blueprint hota hai jis se hum objects banate hain.
# Jaise ghar ka naksha hota hai aur us se kai ghar bante hain.

class Students:

    # setName() - Setter Method
    # Yeh method student ka naam store karta hai.
    # 'self' matlab: jo bhi object ne yeh method call kiya, usi ka naam store karo.
    def setName(self, name):
        self.name = name

    # showName() - Getter/Display Method
    # Yeh method stored naam ko screen par print karta hai.
    def showName(self):
        print("Name: ", self.name)

    # setAge() - Setter Method
    # Student ki umar store karta hai self.age mein.
    def setAge(self, age):
        self.age = age

    # showAge() - Getter/Display Method
    # Stored umar ko print karta hai.
    def showAge(self):
        print("Age: ", self.age)

    # setGrade() - Setter Method
    # Student ka grade store karta hai self.grade mein.
    def setGrade(self, grade):
        self.grade = grade

    # showGrade() - Getter/Display Method
    # Stored grade ko print karta hai.
    def showGrade(self):
        print("Grade: ", self.grade)


# ============================================================
# OBJECT BANANA
# Students() likh kar class ka ek object banate hain.
# s1 ab ek real student hai jis mein data store ho sakta hai.
# ============================================================

s1 = Students()

# Step 1: naam set karo aur dikhao
s1.setName("Shariq")   # self.name = "Shariq"
s1.showName()          # Output: Name:  Shariq

# Step 2: umar set karo aur dikhao
s1.setAge(20)          # self.age = 20
s1.showAge()           # Output: Age:  20

# Step 3: grade set karo aur dikhao
s1.setGrade("A")       # self.grade = "A"
s1.showGrade()         # Output: Grade:  A

# ============================================================
# IMPORTANT NOTES:
# 1. 'self' hamesha pehla parameter hota hai har method mein.
#    Python automatically pass karta hai - hum nahi dete.
# 2. set___() = data store karna  (Setter)
#    show___() = data dikhana     (Display/Getter)
# 3. Ek aur object bana sakte hain - s2 = Students()
#    s2 ka apna alag data hoga, s1 se koi link nahi.
# ============================================================
