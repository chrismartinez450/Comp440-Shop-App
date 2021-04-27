from tkinter import *
from functools import partial

import login

UserName = ''
BuyerID = -1
Cart = {}
root = Tk()


def register_page(root):
    page = Frame(root)
    page.grid()
    title_lbl = Label(root, text="Registration page").grid(row=0, column=0, columnspan=2, pady=5)
    f_name_lbl = Label(root, text="First name: ").grid(row=1, column=0, padx=30)
    f_name_entry = Entry(root).grid(row=1, column=1)

    last_name_lbl = Label(root, text="Last name: ").grid(row=2, column=0)
    last_name_entry = Entry(root).grid(row=2, column=1, pady=10)

    login_id_lbl = Label(root, text="Login ID: ").grid(row=3, column=0)
    login_id_entry = Entry(root).grid(row=3, column=1, pady=10)

    password_lbl = Label(root, text="Password: ").grid(row=4, column=0)
    password_entry = Entry(root).grid(row=4, column=1, pady=10)

    next_button = Button(root, text="Next", width=10 ,command=change_to_add_bank).grid(row=5, column=1)
    back_button = Button(root, text="Back", width=10, command=change_to_login_page).grid(row=5, column=0)


def change_to_reg_page():
    for widget in root.winfo_children():
        widget.destroy()
    register_page(root)


def login_page(root):
    welcome_lbl = Label(root, text="Welcome, please login").pack(pady=10)

    """ Login """
    username = StringVar()
    usr_name_box = Entry(root, textvariable=username).pack(pady=5)

    password = StringVar()
    password_box = Entry(root, textvariable=password, show='*').pack(pady=5)

    validateLogin = partial(login.validateLogin, username, password)
    #login_button = Button(root, text="Login", command=validateLogin).pack(pady=5) This is the original
    login_button = Button(root, text="Login", command=change_to_home_page).pack(pady=5)#Above line is correct ,this line is just temporary access permission ONLY GUI for demonstration

    reg_button = Button(root, text="Register", command=change_to_reg_page).pack(pady=5)

    root.geometry("300x300")

def change_to_login_page():
    for widget in root.winfo_children():
        widget.destroy()
    login_page(root)
############################################1
def add_bank(root):
    page = Frame(root)
    page.grid()

    title_lbl = Label(root, text="                 Add Bank Information").grid(row = 0, columnspan=2 , pady=10 )

    bank_name_lbl = Label(root, text="Bank Name : ").grid(row=1, column=0, sticky=E)
    bank_name_entry = Entry(root).grid(row=1, column=1,pady=10,sticky=W)

    account_number_lbl = Label(root, text="Account # : ").grid(row=2, column=0 ,sticky=E)
    account_number_entry = Entry(root).grid(row=2, column=1, pady=10,sticky=W)

    zip_code_lbl = Label(root, text="Zip Code : ").grid(row=3, column=0 ,sticky=E)
    zip_code_entry = Entry(root).grid(row=3, column=1, pady=10,sticky=W)

    submit_button = Button(root, text="Submit", width=10).grid(row=5, column=1,pady=10)
    canel_button = Button(root, text="Cancel", width=10,command=change_to_reg_page).grid(row=5, column=0,padx=25)


def change_to_add_bank():
    for widget in root.winfo_children():
        widget.destroy()
    add_bank(root)


############################################2
def home_page(root):
    page = Frame(root)
    page.grid()

    shop_button = Button(root, text="Shop", width=15 , height =5,bg='#bce5ec').grid(row=1, column=0 ,pady=30,padx=25)
    checkout_button = Button(root, text="Checkout", width=15 , height =5,bg='#bcecd5').grid(row=1, column=1)
    acc_Setting_button = Button(root, text="Account Setting", width=15 , height =5,bg='#ebecbc',command=change_to_account_setting).grid(row=2, column=0)
    logout_button = Button(root, text="Logout", width=15 , height =5, bg='#ecbcbc',command=change_to_login_page).grid(row=2, column=1)

def change_to_home_page():
    for widget in root.winfo_children():
        widget.destroy()
    home_page(root)
###############################################3
def account_setting(root):
    page = Frame(root)
    page.grid()

    back_home_page_button = Button(root, text="<<Back ", width=10,bg='#ebecbc',command=change_to_home_page).grid(row=0, column=0,pady=10)
    change_bank_button = Button(root, text="Change Bank", width=15 , height =5,bg='#bce5ec',command=change_to_change_bank).grid(row=1, column=0 ,pady=30,padx=25)
    change_password_button = Button(root, text="Change Password", width=15 , height =5,bg='#bcecd5',command=change_to_change_password).grid(row=1, column=1)

def change_to_account_setting():
    for widget in root.winfo_children():
        widget.destroy()
    account_setting(root)

##########################################4
def change_password(root):
    page = Frame(root)
    page.grid()

    back_home_page_button = Button(root, text="<<Back ", width=10,bg='#ebecbc',command=change_to_home_page).grid(row=0, column=0,pady=10)

    current_password_lbl = Label(root, text="Current Password : ").grid(row=1, column=0, sticky=E)
    current_password_entry = Entry(root).grid(row=1, column=1,pady=10,sticky=W)

    new_password_lbl = Label(root, text="New Password : ").grid(row=2, column=0 ,sticky=E)
    new_password_entry = Entry(root).grid(row=2, column=1, pady=10,sticky=W)

    confirm_new_password_lbl = Label(root, text="Confirm New Password : ").grid(row=3, column=0 ,sticky=E)
    confirm_new_password_entry = Entry(root).grid(row=3, column=1, pady=10,sticky=W)
    save_new_password_button = Button(root, text="Save ", width=30,bg='#ebecbc').grid(row=4, column=0,columnspan=4,padx=10,pady=10)


def change_to_change_password():
    for widget in root.winfo_children():
        widget.destroy()
    change_password(root)
###############################################5
def change_bank(root):
    page = Frame(root)
    page.grid()

    title_lbl = Label(root, text="                 Change Bank Information").grid(row=0, columnspan=2, pady=10)

    change_bank_name_lbl = Label(root, text="Bank Name : ").grid(row=1, column=0, sticky=E)
    change_bank_name_entry = Entry(root,state='disabled').grid(row=1, column=1, pady=10, sticky=W)

    change_account_number_lbl = Label(root, text="Account # : ").grid(row=2, column=0, sticky=E)

    change_account_number_entry = Entry(root, state='disabled').grid(row=2, column=1, pady=10, sticky=W)

    change_zip_code_lbl = Label(root, text="Zip Code : ").grid(row=3, column=0, sticky=E)
    change_zip_code_entry = Entry(root ,state='disabled').grid(row=3, column=1, pady=10, sticky=W)

    change_submit_button = Button(root, text="Change", width=10).grid(row=5, column=1, pady=10)
    change_canel_button = Button(root, text="Cancel", width=10, command=change_to_account_setting).grid(row=5, column=0, padx=25)

def change_to_change_bank():
    for widget in root.winfo_children():
        widget.destroy()
    change_bank(root)
###############################



def main():
    login_page(root)
    print('Global Cart:', Cart)
    root.title("Online Retail")
    root.mainloop()


if __name__ == "__main__":
    main()