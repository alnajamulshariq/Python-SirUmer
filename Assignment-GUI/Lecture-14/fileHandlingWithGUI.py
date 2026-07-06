import tkinter as tk
import json


def save_Employee():
    emp = {
        "id": txt_id.get(),
        "name": txt_name.get(),
        "salary": txt_salary.get(),
        "address": txt_address.get(),
        "phone": txt_phone.get(),
        "email": txt_email.get()
    }

    try:
        with open("employee.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(emp)

    with open("employee.json", "w") as f:
        json.dump(data, f, indent=4)

    showEmployee()


def showEmployee():
    secWindow = tk.Toplevel(window)
    secWindow.title("Employees Record")
    secWindow.geometry("900x400")

    try:
        with open("employee.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    if len(data) == 0:
        tk.Label(secWindow, text="No employee record found").pack(pady=10)
        return

    for emp in data:
        lbl_id = tk.Label(
            secWindow,
            text=f"ID: {emp['id']} | Name: {emp['name']} | Salary: {emp['salary']} | Address: {emp['address']} | Phone: {emp['phone']} | Email: {emp['email']}",
            wraplength=850,
            justify="left"
        )
        lbl_id.pack(pady=10, padx=10)


window = tk.Tk()
window.title("Employee Form")
window.geometry("500x400")

tk.Label(window, text="Employee Name").pack()
txt_name = tk.Entry(window)
txt_name.pack()

tk.Label(window, text="Employee ID").pack()
txt_id = tk.Entry(window)
txt_id.pack()

tk.Label(window, text="Salary").pack()
txt_salary = tk.Entry(window)
txt_salary.pack()

tk.Label(window, text="Address").pack()
txt_address = tk.Entry(window)
txt_address.pack()

tk.Label(window, text="Phone").pack()
txt_phone = tk.Entry(window)
txt_phone.pack()

tk.Label(window, text="Email").pack()
txt_email = tk.Entry(window)
txt_email.pack()

btn = tk.Button(window, text="Save Employee", command=save_Employee)
btn.pack(pady=20)

window.mainloop()