cart = []
for i in range(5):
    item = input("Enter an item to add to the cart: ")
    cart.append(item)
    
    print("Your cart:", cart)
    
    
    
# remove an item from the cart
item_to_remove = input("Enter an item to remove from the cart: ")
if item_to_remove in cart:
    cart.remove(item_to_remove)
    print("Item removed. Your cart:", cart)
else:
    print("Item not found in the cart.")