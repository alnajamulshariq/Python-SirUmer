# tkinter module import kar rahe hain aur is ko short name tk de rahe hain
import tkinter as tk


# submit naam ka function bana rahe hain
# yeh function tab chalega jab user Submit button press karega
def submit():

    # txt_name Entry box se user ka name get kar rahe hain
    name = txt_name.get()

    # txt_age Entry box se user ki age get kar rahe hain
    age = txt_age.get()

    # txt_address Entry box se user ka address get kar rahe hain
    address = txt_address.get()

    # lbl_result label ka text update kar rahe hain
    # is mein name, age aur address show hoga
    lbl_result.config(
        text=f"Name: {name}\nAge: {age}\nAddress: {address}"
    )


# main window create kar rahe hain
window = tk.Tk()

# window ka size set kar rahe hain
# width 500 aur height 350 pixels hogi
window.geometry("500x350")


# name ke liye label bana rahe hain
# yeh user ko batayega ke name enter karna hai
lbl_name = tk.Label(window, text="Enter Name:")

# label ko window mein show kar rahe hain
lbl_name.pack()


# name enter karne ke liye text box bana rahe hain
txt_name = tk.Entry(window)

# name wala text box window mein show kar rahe hain
txt_name.pack()


# age ke liye label bana rahe hain
# yeh user ko batayega ke age enter karni hai
lbl_age = tk.Label(window, text="Enter Age:")

# age label ko window mein show kar rahe hain
lbl_age.pack()


# age enter karne ke liye text box bana rahe hain
txt_age = tk.Entry(window)

# age wala text box window mein show kar rahe hain
txt_age.pack()


# address ke liye label bana rahe hain
# yeh user ko batayega ke address enter karna hai
lbl_address = tk.Label(window, text="Enter Address:")

# address label ko window mein show kar rahe hain
lbl_address.pack()


# address enter karne ke liye text box bana rahe hain
txt_address = tk.Entry(window)

# address wala text box window mein show kar rahe hain
txt_address.pack()


# Submit button bana rahe hain
# text="Submit" button par likha hua text hai
# command=submit ka matlab button click hone par submit function chalega
btn_submit = tk.Button(window, text="Submit", command=submit)

# button ko window mein show kar rahe hain
# pady=10 ka matlab button ke upar aur neeche thora space hoga
btn_submit.pack(pady=10)


# result show karne ke liye empty label bana rahe hain
# shuru mein is label mein koi text nahi hoga
lbl_result = tk.Label(window, text="")

# result label ko window mein show kar rahe hain
lbl_result.pack()


# window ko continuously open rakhne ke liye mainloop chalate hain
# is ke baghair window foran close ho sakti hai
window.mainloop()