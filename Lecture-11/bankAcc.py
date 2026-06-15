
# abc module se ABC aur abstractmethod import kar rahe hain
# ABC ka use abstract class banane ke liye hota hai
# abstractmethod ka use abstract method banane ke liye hota hai
from abc import ABC, abstractmethod


# BankAcc ek abstract class hai
# Abstract class ka direct object nahi ban sakta
# Is class ko parent/base class ki tarah use karenge
class BankAcc(ABC):

    # Constructor method
    # Jab bhi BankAcc ki child class ka object banega, yeh method automatically chalega
    def __init__(self, accountNo, name, balance):

        # Account number ko object ke andar save kar rahe hain
        self.accountNo = accountNo

        # Account holder ka name save kar rahe hain
        self.name = name

        # Account ka initial balance save kar rahe hain
        self.balance = balance

    # Deposit method
    # Is method ka kaam account mein paisay jama karna hai
    def deposit(self, amount):

        # Check kar rahe hain ke deposit amount 0 se bara hai ya nahi
        if amount > 0:

            # Balance mein amount add kar rahe hain
            self.balance += amount

            # User ko message show kar rahe hain ke amount deposit ho gaya
            print("Deposited", amount, "in account", self.accountNo)

            # Deposit ke baad updated balance show kar rahe hain
            print("Balance is", self.balance)

        # Agar amount 0 ya negative ho to invalid message show hoga
        else:
            print("Invalid deposit amount")

    # Withdraw method
    # Is method ka kaam account se paisay nikalna hai
    def withdraw(self, amount):

        # Check kar rahe hain ke withdraw amount 0 se bara hai ya nahi
        if amount <= 0:

            # Agar amount 0 ya negative hai to invalid message show hoga
            print("Invalid withdraw amount")

        # Check kar rahe hain ke account mein itna balance available hai ya nahi
        elif amount <= self.balance:

            # Balance se amount minus kar rahe hain
            self.balance -= amount

            # User ko message show kar rahe hain ke amount withdraw ho gaya
            print("Withdrawn", amount, "from account", self.accountNo)

            # Withdraw ke baad updated balance show kar rahe hain
            print("Balance is", self.balance)

        # Agar balance kam hai to insufficient funds show hoga
        else:
            print("Insufficient funds")

    # Show balance method
    # Is method ka kaam account ka balance display karna hai
    def show_balance(self):

        # Account holder ka name show kar rahe hain
        print("Account Holder:", self.name)

        # Account number show kar rahe hain
        print("Account No:", self.accountNo)

        # Current balance show kar rahe hain
        print("Balance is", self.balance)

    # Abstract method
    # Is method ki body parent class mein nahi hogi
    # Har child class ko apna calculate_profit method banana zaroori hoga
    @abstractmethod
    def calculate_profit(self):
        pass


# SavingsAcc child class hai
# Yeh BankAcc class se inherit kar rahi hai
class SavingsAcc(BankAcc):

    # Savings account ka profit calculate karne ka method
    def calculate_profit(self):

        # Savings account ke liye 10% profit calculate kar rahe hain
        profit = self.balance * 0.10

        # Profit show kar rahe hain
        print("Savings Account Profit is", profit)


# CurrentAcc child class hai
# Yeh bhi BankAcc class se inherit kar rahi hai
class CurrentAcc(BankAcc):

    # Current account ka profit calculate karne ka method
    def calculate_profit(self):

        # Current account ke liye 5% profit calculate kar rahe hain
        profit = self.balance * 0.05

        # Profit show kar rahe hain
        print("Current Account Profit is", profit)


# SavingsAcc ka object create kar rahe hain
# accountNo = pk-01
# name = Shariq
# balance = 10000
s1 = SavingsAcc("pk-01", "Shariq", 10000)

# CurrentAcc ka object create kar rahe hain
# accountNo = pk-02
# name = Najam
# balance = 10000
c1 = CurrentAcc("pk-02", "Najam", 10000)


# Savings Account ka section start kar rahe hain
print("\n========== Savings Account ==========")

# Savings account ka current balance show kar rahe hain
s1.show_balance()

# Savings account mein 5000 deposit kar rahe hain
s1.deposit(5000)

# Savings account se 2000 withdraw kar rahe hain
s1.withdraw(2000)

# Savings account ka final balance show kar rahe hain
s1.show_balance()

# Savings account ka profit calculate kar rahe hain
s1.calculate_profit()


# Current Account ka section start kar rahe hain
print("\n========== Current Account ==========")

# Current account ka current balance show kar rahe hain
c1.show_balance()

# Current account mein 3000 deposit kar rahe hain
c1.deposit(3000)

# Current account se 1000 withdraw kar rahe hain
c1.withdraw(1000)

# Current account ka final balance show kar rahe hain
c1.show_balance()

# Current account ka profit calculate kar rahe hain
c1.calculate_profit()