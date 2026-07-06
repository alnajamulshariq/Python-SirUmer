import tkinter as tk


# submit button press hone par yeh function chalega
def show_employee():
    empl_id = txt_id.get()
    name = txt_name.get()
    salary = txt_salary.get()

    # second window create kar rahe hain
    second_window = tk.Toplevel(window)
    second_window.title("Employee Details")
    second_window.geometry("500x300")

    heading = tk.Label(
        second_window,
        text="Employee Details",
        font=("Arial", 22, "bold")
    )
    heading.pack(pady=10)

    lbl_id = tk.Label(
        second_window,
        text=f"Employee ID: {empl_id}",
        font=("Arial", 18)
    )
    lbl_id.pack(pady=5)

    lbl_name = tk.Label(
        second_window,
        text=f"Employee Name: {name}",
        font=("Arial", 18)
    )
    lbl_name.pack(pady=5)

    lbl_salary = tk.Label(
        second_window,
        text=f"Employee Salary: {salary}",
        font=("Arial", 18)
    )
    lbl_salary.pack(pady=5)


# main window create kar rahe hain
window = tk.Tk()
window.title("Employee Form")
window.geometry("500x300")

heading = tk.Label(
    window,
    text="Employee Entry Form",
    font=("Arial", 20, "bold")
)
heading.pack(pady=10)

lbl_id = tk.Label(window, text="Enter Employee ID")
lbl_id.pack()

txt_id = tk.Entry(window)
txt_id.pack(pady=5)

lbl_name = tk.Label(window, text="Enter Employee Name")
lbl_name.pack()

txt_name = tk.Entry(window)
txt_name.pack(pady=5)

lbl_salary = tk.Label(window, text="Enter Employee Salary")
lbl_salary.pack()

txt_salary = tk.Entry(window)
txt_salary.pack(pady=5)

btn_Submit = tk.Button(
    window,
    text="Submit",
    command=show_employee
)
btn_Submit.pack(pady=10)

window.mainloop()