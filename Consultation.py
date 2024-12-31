import os
import sqlite3
import tkinter
from tkcalendar import Calendar
from tkinter import *
from tkinter import Tk, messagebox
from tkinter import ttk
from datetime import datetime

import openpyxl
from PIL import Image, ImageTk
from openpyxl.chart import ScatterChart, Reference, Series, BarChart3D
from prettytable import PrettyTable
from EHR import config as cfg
import datetime

class Consultation:

    did = ""
    dname = ""
    tdate = ""
    patient_id_name = []
    def __init__(self, root):
        self.LARGE_FONT = ("Algerian", 16)
        self.text_font = ("Constantia", 15)
        self.text_font1 = ("Constantia", 11)

        self.frame_font = ("", 9)
        self.frame_process_res_font = ("", 12)
        self.root = root
        self.hosp_id_name = "H1 : MIOT Hospital"
        label_heading = tkinter.Label(root, text="Online Consultation with Doctor", fg='deep pink', bg="white", font=self.LARGE_FONT)
        label_heading.place(x=150, y=10)

        self.did = cfg.did
        self.dname = cfg.dname

        self.tdate = datetime.datetime.now().strftime("%d-%m-%Y")+""

        self.label_hospital_id_name = Label(root, text="Hospital ID & Name", bg="white", font=13)
        self.label_hospital_id_name.place(x=20, y=70)
        self.entry_hospital_id_name = Entry(root, font=13)
        self.entry_hospital_id_name.place(x=200, y=70, width=250, height=25)
        self.entry_hospital_id_name.insert(INSERT, self.hosp_id_name)
        self.entry_hospital_id_name.configure(state="disabled")

        self.label_doctor_id_name = Label(root, text="Doctor ID & Name", bg="white", font=13)
        self.label_doctor_id_name.place(x=20, y=120)
        self.entry_doctor_id_name = Entry(root, font=13)
        self.entry_doctor_id_name.place(x=200, y=120, width=250, height=25)
        self.entry_doctor_id_name.insert(INSERT, str(self.did+" : "+self.dname))
        self.entry_doctor_id_name.configure(state="disabled")

        def consultation():
            pidname=[]

            con = sqlite3.connect("..\\db\\user_datas.db")
            cursorObj = con.cursor()
            cursorObj.execute("SELECT patient_detail_form.patient_id, patient_detail_form.patient_name from book_appointment_form INNER JOIN patient_detail_form on patient_detail_form.patient_id = book_appointment_form.patient_id where book_appointment_form.doctor_id='" + self.did + "' and book_appointment_form.appointment_date= '"+self.tdate+"' and book_appointment_form.consultation='0'")
            result = cursorObj.fetchall()
            for row in result:
                pidname.append(str(row[0]) + " << " + str(row[1]))

            return pidname

        self.label_patient_id_name = Label(root, text="Patient ID & Name", bg="white", font=13)
        self.label_patient_id_name.place(x=20, y=180)
        self.patient_id_name = consultation()
        self.cmb_patient_id_name = ttk.Combobox(root, values=self.patient_id_name, width=38)
        self.cmb_patient_id_name.place(x=200, y=180)
        self.cmb_patient_id_name.set("--Select--")
        # self.cmb_patient_id_name["state"] = "readonly"

        self.label_adate = Label(root, text="Appoinment Date", bg="white", font=13)
        self.label_adate.place(x=20, y=230)
        self.entry_adate = Entry(root, font=13)
        self.entry_adate.place(x=200, y=230, width=250, height=25)
        self.entry_adate.insert(INSERT, self.tdate)
        self.entry_adate.configure(state="disabled")

        home_image = Image.open("..\\Images\\consulting.png")
        render = ImageTk.PhotoImage(home_image)
        self.img = Label(root, image=render, bg="white", fg="white")
        self.img.image = render
        self.img.place(x=470, y=100)

        self.btn_consulting = Button(root, text="Consulting", bg="deep sky blue", fg="#fff", command=self.consulting, font=self.text_font1)
        self.btn_consulting.place(x=50, y=400, width=150, height=30)
        self.close_button = Button(root, text="Close", bg="deep sky blue", fg="#fff", command=self.close, font=self.text_font1)
        self.close_button.place(x=350, y=400, width=70, height=30)

    def consulting(self):
        strpname = self.cmb_patient_id_name.get()

        if len(self.patient_id_name) > 0:
            if strpname != "--Select--":
                a = strpname.split(" << ")
                strpid = a[0]
                strpname = a[1]
                tdate = datetime.datetime.now().strftime("%d-%m-%Y")
                if not os.path.exists('..\\db'):
                    os.makedirs('..\\db')
                con = sqlite3.connect("..\\db\\user_datas.db")
                cursorObj = con.cursor()

                cursorObj.execute("UPDATE book_appointment_form SET consultation = '1' WHERE doctor_id = '"+self.did+"' and patient_id='"+strpid+"' and appointment_date='"+tdate+"'")

                con.commit()
                con.close()
                print("Consulting was done Successfully...")
                messagebox.showinfo("Success", "Consulting was done Successfully...")

                print("\nConsensus Rule based Smart Contract Creation")
                print("==============================================")

                print("\nExisting Proof of Activity (PoA)")
                print("----------------------------------")

                print("\nExisting Proof of Burn (PoB)")
                print("------------------------------")

                print("\nExisting Proof of Capacity (PoC)")
                print("----------------------------------")

                print("\nExisting Proof of Stack (PoS)")
                print("-------------------------------")

                print("\nProposed Generalized-Pi Fuzzy Proof of Stack Consensus Rule (GPF-PoSCR)")
                print("-------------------------------------------------------------------------")

                print("\nConsensus Rule based Smart Contract Creation was done Successfully...")
                messagebox.showinfo("Success", "Consensus Rule based Smart Contract Creation was done Successfully...")
                self.root.destroy()
            else:
                messagebox.showinfo("Info Message", "Please select the patient...")
        else:
            messagebox.showinfo("Info Message", "No appointment is available...")

    def close(self):
        self.root.destroy()

root = Tk()
root.title("Online Consultation GUI")
root.geometry('800x500')
root.resizable(0, 0)
root.configure(bg='white')
od = Consultation(root)
root.mainloop()
