# Encapsulation

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
        
#     def deposit(self, amount):
#         self.__balance += amount
        
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds")
            
#     def show_balance(self):
#         print("Balance is", self.__balance)
        
# acc1 = BankAccount(2000)
# acc1.deposit(500)
# acc1.withdraw(300)
# acc1.show_balance()



# Polymorphism

class CreditCard:
    def pay (self, amount):
        print(f"Paid Rs. {amount} using Credit Card")
        
class JazzCash:
    def pay (self, amount):
        print(f"Paid Rs. {amount} using Jazz Cash")
        
class EasyPaisa:
    def pay (self, amount):
        print(f"Paid Rs. {amount} using Easy Paisa")
        
payments = [CreditCard(), JazzCash(), EasyPaisa()]

payment = CreditCard()
payment.pay(1000)

payment = JazzCash()
payment.pay(20000)

payment = EasyPaisa()
payment.pay(10000)
        