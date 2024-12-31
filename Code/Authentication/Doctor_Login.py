import os
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile

from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3
import socket
import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk,messagebox
from tkinter import filedialog as fd

from EHR import config as cfg

class Doctor_Login(object):

    def __init__(self, root):
        print("Doctor Login process...")

        self.user_name = StringVar()
        self.pwd = StringVar()
        self.hcode = StringVar()

        self.hashcode = ""

        self.Large_font = ("Algerian", 16)
        self.root = root

        self.label_heading = Label(root, text="Doctor Login Form", height=2, width=24,fg="deep pink", bg="white", font=self.Large_font)
        self.label_heading.place(x=40, y=30)

        self.user_name_label = Label(root, text="User Name ", bg="white", font=4)
        self.user_name_label.place(x=10, y=100)
        self.user_name_entry = Entry(root, highlightthickness=2, textvar=self.user_name)
        self.user_name_entry.config(highlightbackground="black")
        self.user_name_entry.place(x=120, y=100, width=140, height=30)

        self.password_label = Label(root, text="Password ",bg="white", font=4)
        self.password_label.place(x=10, y=170)
        self.password_entry = Entry(root, highlightthickness=2, textvar=self.pwd,show="*")
        self.password_entry.config(highlightbackground="black")
        self.password_entry.place(x=120, y=170, width=140, height=30)

        self.secretcode_label = Label(root, text="Secret Code ",bg="white", font=4)
        self.secretcode_label.place(x=10, y=240)
        self.secretcode_entry = Entry(root, highlightthickness=2)
        self.secretcode_entry.config(highlightbackground="black")
        self.secretcode_entry.place(x=120, y=240, width=140, height=30)
        self.secretcode_entry.configure(state='disabled')
        self.secretcode_button = Button(root, text="Browse Secret Code",width=9, height=1, bg="white",command=self.secretcode)
        self.secretcode_button.configure(background='#345', foreground='deep pink', font=('Arial', 14))
        self.secretcode_button.place(x=270, y=240, width=190, height=30)

        self.purpose_label = Label(root, text="Purpose ", bg="white", font=4)
        self.purpose_label.place(x=10, y=300)
        purpose = ["Consultation", "IoT Data Download"]
        self.cmb_purpose = ttk.Combobox(root, values=purpose, width=20)
        self.cmb_purpose.place(x=120, y=300)
        self.cmb_purpose.set("--Select--")
        self.cmb_purpose["state"] = "readonly"

        self.login_button = Button(root, text="Login",width=9, height=1, bg="white",command=self.login)
        self.login_button.configure(background='#345', foreground='deep pink', font=('Arial', 14))
        self.login_button.place(x=50, y=350, width=90, height=30)
        self.clear_button = Button(root, text="Clear", width=9, height=1, bg="white", command=self.clear)
        self.clear_button.configure(background='#345', foreground='deep pink', font=('Arial', 14))
        self.clear_button.place(x=150, y=350, width=90, height=30)
        self.back_button = Button(root, text="Back", width=9, height=1, bg="white", command=self.back)
        self.back_button.configure(background='#345', foreground='deep pink', font=('Arial', 14))
        self.back_button.place(x=250, y=350, width=90, height=30)
        self.close_button = Button(root, text="Close", width=9, height=1, bg="white", command=self.close)
        self.close_button.configure(background='#345', foreground='deep pink', font=('Arial', 14))
        self.close_button.place(x=350, y=350, width=90, height=30)

        load = Image.open("..\\Images\\s_doctor_icon.png")
        render = ImageTk.PhotoImage(load)
        self.img = Label(root, image=render, bg="white", fg = "white")
        self.img.image = render
        self.img.place(x=350, y=100)

    def secretcode(self):
        self.secretcode_path = askopenfile(mode='r', filetypes=[('All Files', '*')])
        self.secretcode_entry.configure(state="normal")
        self.secretcode_entry.insert(INSERT, self.secretcode_path.name)

    def login(self):
        try:
            if len(self.user_name.get()) > 0:
                if len(self.pwd.get()) > 0:
                   if self.cmb_purpose.get() != "--Select--":
                        user_name = self.user_name.get()
                        password = self.pwd.get()
                        strpurpose = self.cmb_purpose.get()
                        if not os.path.exists('..//db//'):
                            os.makedirs('..//db//')
                        con = sqlite3.connect("..\\db\\user_datas.db")
                        cursorObj = con.cursor()
                        cursorObj.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='doctor_detail_form' ''')
                        if cursorObj.fetchone()[0] == 1:
                            cursorObj.execute("SELECT * FROM doctor_detail_form WHERE user_name=? AND password= ?",(user_name, password))
                            result = cursorObj.fetchall()
                            if result:
                                for row in result:
                                    cfg.did = row[1]
                                    cfg.dname = row[2]

                                if strpurpose == "Consultation":
                                    con = sqlite3.connect("..\\db\\user_datas.db")
                                    cursorObj = con.cursor()
                                    cursorObj.execute(
                                        ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='book_appointment_form' ''')
                                    if cursorObj.fetchone()[0] == 1:
                                        print("Login Successfully!!!")
                                        messagebox.showinfo("Success", "Login Successfully...")
                                        print("\nDoctor ID : " + str(cfg.did))
                                        print("Username : " + str(user_name))
                                        print("Password : " + str(password))
                                        self.root.destroy()
                                        from EHR.Code.Consultation import Consultation
                                    else:
                                        messagebox.showerror("Error Message", "No consultation was done...")
                                        self.clear()
                                else:
                                    con = sqlite3.connect("..\\db\\user_datas.db")
                                    cursorObj = con.cursor()
                                    cursorObj.execute(
                                        ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='book_appointment_form' ''')
                                    if cursorObj.fetchone()[0] == 1:
                                        cursorObj.execute(
                                            "SELECT * FROM book_appointment_form WHERE doctor_id=? AND consultation=?",
                                            (str(row[1]), "1"))
                                        result = cursorObj.fetchall()
                                        if result:
                                            print("Login Successfully!!!")
                                            messagebox.showinfo("Success", "Login Successfully...")
                                            print("\nDoctor ID : " + str(cfg.did))
                                            print("Username : " + str(user_name))
                                            print("Password : " + str(password))
                                            self.root.destroy()
                                            from EHR.Code.Doctor_GUI import Doctor_GUI
                                        else:
                                            messagebox.showerror("Error Message", "No consultation was done...")
                                            self.clear()
                                    else:
                                        messagebox.showerror("Error Message", "No consultation was done...")
                                        self.clear()
                            else:
                                messagebox.showerror("Error Message", "Login failed please register your details...")
                        else:
                            messagebox.showerror("Error Message", "Please register the doctor first...")
                   else:
                       messagebox.showerror("Error", "Please select the purpose to login...")
                else:
                    messagebox.showerror("Error", "Please enter the password...")
            else:
                messagebox.showerror("Error", "Please enter user name...")
        except Exception as e:
            print("Exception", e)

    def clear(self):
        self.user_name.set("")
        self.pwd.set("")
        self.hcode.set("")

    def close(self):
        self.root.destroy()

    def back(self):
        self.root.destroy()
        from EHR.Code.First_GUI import First_GUI

root = Tk()
root.title("Doctor Login Window")
root.geometry('500x500+400+150')
root.resizable(0,0)
root.configure(bg='white')
log = Doctor_Login(root)
root.mainloop()