from tkinter import *

tk = Tk()


def login_page(root):
    welcome_lbl = Label(root, text="Welcome, please login").grid(row=0, column=0, columnspan=2, pady=5)
    usr_name_lbl = Label(tk, text="User ID: ").grid(row=1, column=0, padx=30)
    usr_name_box = Entry(root).grid(row=1,column=1, pady=10)
    password_lbl = Label(tk, text="Password: ").grid(row=2, column=0, padx=30)
    password_box = Entry(root).grid(row=2,column=1, pady=10)
    reg_button = Button(root, text="Register", command=change_to_reg_page).grid(row=3, column=0, columnspan=2, pady=5)
    login_button = Button(root, text="Login").grid(row=4, column=0, columnspan=2, pady=5)
    root.geometry("300x300")


def change_to_login_page():
    for widget in tk.winfo_children():
        widget.destroy()
    login_page(tk)


def register_page():
    title_lbl = Label(tk, text="Registration page").grid(row=0, column=0, columnspan=2, pady=5)
    f_name_lbl = Label(tk, text="First name: ").grid(row=1, column=0, padx=30)
    f_name_entry = Entry(tk).grid(row=1, column=1)

    last_name_lbl = Label(tk, text="Last name: ").grid(row=2, column=0)
    last_name_entry = Entry(tk).grid(row=2, column=1, pady=10)

    login_id_lbl = Label(tk, text="Login ID: ").grid(row=3, column=0)
    login_id_entry = Entry(tk).grid(row=3, column=1, pady=10)

    password_lbl = Label(tk, text="Password: ").grid(row=4, column=0)
    password_entry = Entry(tk).grid(row=4, column=1, pady=10)

    next_button = Button(tk, text="Next", width=10, command=change_to_add_bank_page).grid(row=5, column=1)
    back_button = Button(tk, text="Back", width=10, command=change_to_login_page).grid(row=5, column=0)


def change_to_reg_page():
    for widget in tk.winfo_children():
        widget.destroy()
    register_page()


def add_bank_page():
    bank_title_lbl = Label(tk, text="Please add bank info").grid(row=0, column=0, columnspan=2, pady=5)
    bank_name_lbl = Label(tk, text="Bank Name: ").grid(row=1, column=0, padx=30)
    bank_name_entry = Entry(tk).grid(row=1, column=1, pady=10)

    account_num_lbl = Label(tk, text="Account number: ").grid(row=2, column=0)
    account_num_entry = Entry(tk).grid(row=2, column=1, pady=10)

    zipcode_lbl = Label(tk, text="Zipcode: ").grid(row=3, column=0)
    zipcode_entry = Entry(tk).grid(row=3, column=1, pady=10)

    next_button2 = Button(tk, text="Next", width=10).grid(row=4, column=1)
    back_button2 = Button(tk, text="Back", width=10, command=change_to_reg_page).grid(row=4, column=0)


def change_to_add_bank_page():
    for widget in tk.winfo_children():
        widget.destroy()
    add_bank_page()


login_page(tk)
tk.mainloop()
