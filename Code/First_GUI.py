import os
import sqlite3
import tkinter
from tkinter import *
from tkinter import Tk, messagebox

import openpyxl
from PIL import Image, ImageTk
from openpyxl.chart import ScatterChart, Reference, Series, BarChart3D
from prettytable import PrettyTable

class First_GUI:

    def __init__(self, root):
        self.LARGE_FONT = ("Algerian", 16)
        self.text_font = ("Constantia", 15)
        self.text_font1 = ("Constantia", 11)

        self.frame_font = ("", 9)
        self.frame_process_res_font = ("", 12)
        self.root = root

        label_heading = tkinter.Label(root, text="ETHEREUM HYPERLEDGER BLOCKCHAIN BASED SECURE EHR TRANSMISSION USING GPFPoSCR & ECGRCC", fg='deep pink', bg="azure3", font=self.LARGE_FONT)
        label_heading.place(x=0, y=10)

        home_image = Image.open("..\\Images\\HP.PNG")
        render = ImageTk.PhotoImage(home_image)
        self.img = Label(root, image=render, bg="white", fg="white")
        self.img.image = render
        self.img.place(x=10, y=50)

        patient_image = Image.open("..\\Images\\s_patient_icon.PNG")
        render = ImageTk.PhotoImage(patient_image)
        self.img = Label(root, image=render, bg="white", fg="white")
        self.img.image = render
        self.img.place(x=70, y=55)

        doctor_image = Image.open("..\\Images\\s_doctor_icon.PNG")
        render = ImageTk.PhotoImage(doctor_image)
        self.img = Label(root, image=render, bg="white", fg="white")
        self.img.image = render
        self.img.place(x=830, y=55)

        self.btn_p_login = Button(root, text="Login", width=13, bg="deep sky blue", fg="#fff", font=self.text_font1, command=self.p_login)
        self.btn_p_login.place(x=50, y=200)

        self.btn_p_registration = Button(root, text="Registration", width=13, bg="deep sky blue", fg="#fff", font=self.text_font1, command=self.p_registration)
        self.btn_p_registration.place(x=50, y=250)

        self.btn_d_login = Button(root, text="Login", width=13, bg="deep sky blue", fg="#fff", font=self.text_font1, command=self.d_login)
        self.btn_d_login.place(x=820, y=200)

        self.btn_d_registration = Button(root, text="Registration", width=13, bg="deep sky blue", fg="#fff", font=self.text_font1, command=self.d_registration)
        self.btn_d_registration.place(x=820, y=250)

        self.btn_system_failure_prediction = Button(root, text="SFP Training", width=13, bg="deep sky blue", fg="#fff", font=self.text_font1, command=self.system_failure_prediction)
        self.btn_system_failure_prediction.place(x=50, y=350)

        self.btn_exit = Button(root, text="Exit", width=13, bg="deep sky blue", fg="#fff", font=self.text_font1, command=self.exit)
        self.btn_exit.place(x=820, y=350)

    def exit(self):
        self.root.destroy()

    def p_login(self):
        try:
            con = sqlite3.connect("..\\db\\user_datas.db")
            cursorObj = con.cursor()

            cursorObj.execute("SELECT * FROM doctor_detail_form")
            result = cursorObj.fetchall()
            if result:
                self.root.destroy()
                from EHR.Authentication.Patient_Login import PatientLogin
            else:
                messagebox.showinfo("Show Info", "Please create the doctor first...")
        except Exception as e:
            print(e)
            messagebox.showinfo("Show Info", "Please create the doctor first...")

    def d_login(self):
        self.root.destroy()
        from EHR.Authentication.Doctor_Login import Doctor_Login

    def p_registration(self):
        self.root.destroy()
        from EHR.Authentication.Patient_Registration import Patient_Registration

    def d_registration(self):
        self.root.destroy()
        from EHR.Authentication.Doctor_Registration import Doctor_Registration

    def system_failure_prediction(self):
        self.root.destroy()
        from EHR.Code.SFP_Training import SFP_Training

    def graph_tables(self):
        if not os.path.exists("..\\Result\\"):
            os.makedirs("..\\Result\\")

        def graphsresult():

            messagebox.showinfo("Result", "Graphs and tables are generated successfully!!!")

        graphsresult()


root = Tk()
root.title("First GUI")
root.geometry('1000x500')
root.resizable(0, 0)
root.configure(bg='azure3')
od = First_GUI(root)
root.mainloop()
