# for loop python mein kya karta hai # for loop ka use hum tab karte hain jab hume kisi sequence (jaise list, tuple, string) ke har element par kuch operation perform karna hota hai.

    # for i in range (1 , 11):
    #     print(i)
    
# while loop python mein kya karta hai # while loop ka use hum tab karte hain jab hume kisi condition ke true hone tak kuch operation perform karna hota hai.
# num = 1
# while num <= 10:
#     print(num)
#     num += 1




# password attempt example using while loop
# attempt = 1
# while attempt <= 3:
#     pin = int(input("Enter your pin: "))
#     if pin == 1234:
#         print("Access granted")
#         break
#     else:
#         print("Access denied")
#         attempt += 1



# break and continue statements in loops
# break statement loop ko turant rok deta hai, jabki continue statement loop ke current iteration ko skip kar deta hai aur next iteration par chala jata hai.

# for i in range(1, 6):
#     if i == 4:
#         continue  # jab i 4 hoga to us iteration ko skip kar dega
#     print(i)


# hum students ki id k through loop chala kar present aur absent students ko mark kar sakte hain.
# students = [101, 102, 103, 104, 105]
# present_students = [101, 103, 105]
# for student in students:
#     if student in present_students:
#         print(f"Student {student} is present.")
#     else:
#         print(f"Student {student} is absent.")
        
        
# digits mein pattern 1 se le k 15 tak right angle mein, to main for loop ka use kar sakta hoon.
# for i in range(1, 16):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()  # new line after each row
    
    
# # digits mein triangle pattern 1 se le k 5 tak, to main for loop ka use kar sakta hoon.
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()  # new line after each row


# string mein pattern banana, to main for loop ka use kar sakta hoon.
# word = "HELLO"
# for i in range(len(word)):
#     for j in range(i + 1):
#         print(word[j], end=' ')
#     print()  # new line after each row




# 2 ka table print karna, to main for loop ka use kar sakta hoon.
# for i in range(1, 11):
#     print(f"2 x {i} = {2 * i}")
    
# # while loop ka use karke 2 ka table print karna, to main while loop ka use kar sakta hoon.
# num = 1
# while num <= 10:
#     print(f"2 x {num} = {2 * num}")
#     num += 1
