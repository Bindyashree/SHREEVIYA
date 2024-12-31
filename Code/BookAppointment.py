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

class BookAppointment:

    def __init__(self, root):
        self.LARGE_FONT = ("Algerian", 16)
        self.text_font = ("Constantia", 15)
        self.text_font1 = ("Constantia", 11)

        self.frame_font = ("", 9)
        self.frame_process_res_font = ("", 12)
        self.root = root
        self.hosp_id_name = "H1 : MIOT Hospital"
        label_heading = tkinter.Label(root, text="Book Appointment with Doctor for Consultation", fg='deep pink', bg="white", font=self.LARGE_FONT)
        label_heading.place(x=150, y=10)

        def spec():
            specname = []
            con = sqlite3.connect("..\\db\\user_datas.db")
            cursorObj = con.cursor()
            cursorObj.execute("SELECT * FROM doctor_detail_form")
            result = cursorObj.fetchall()
            for row in result:
                specname.append(row[7])
            return specname

        def doctor_name(event):
            # spec = self.cmb_specialization.get()
            spec = event.widget.get()
            con = sqlite3.connect("..\\db\\user_datas.db")
            cursorObj = con.cursor()
            cursorObj.execute("SELECT * FROM doctor_detail_form where specialization='" + spec + "'")
            result = cursorObj.fetchall()
            for row in result:
                self.cmb_doctor_name.set(str(row[1]) + " << " + str(row[2]))

        self.label_doctor_spec = Label(root, text="Doctor Specialization", bg="white", font=13)
        self.label_doctor_spec.place(x=20, y=70)
        specialization = spec()
        self.cmb_specialization = ttk.Combobox(root, values=specialization, width=38)
        self.cmb_specialization.place(x=180, y=70)
        self.cmb_specialization.set("--Select--")
        self.cmb_specialization["state"] = "readonly"
        self.cmb_specialization.bind("<<ComboboxSelected>>", doctor_name)

        self.label_doctor_name = Label(root, text="Doctor Name", bg="white", font=13)
        self.label_doctor_name.place(x=20, y=120)
        specialization = []
        self.cmb_doctor_name = ttk.Combobox(root, values=specialization, width=38)
        self.cmb_doctor_name.place(x=180, y=120)
        self.cmb_doctor_name.set("--Select--")
        self.cmb_doctor_name["state"] = "readonly"

        self.label_adate = Label(root, text="Appointment Date", bg="white", font=13)
        self.label_adate.place(x=20, y=170)
        self.cal_adate = Calendar(root, selectmode="day", date_pattern="dd-mm-y")
        self.cal_adate.place(x=180, y=170)

        home_image = Image.open("..\\Images\\book_appointment.PNG")
        render = ImageTk.PhotoImage(home_image)
        self.img = Label(root, image=render, bg="white", fg="white")
        self.img.image = render
        self.img.place(x=470, y=100)

        self.btn_book_appointment = Button(root, text="Book Appointment", bg="deep sky blue", fg="#fff", command=self.book_appointment, font=self.text_font1)
        self.btn_book_appointment.place(x=50, y=400, width=150, height=30)
        self.close_button = Button(root, text="Close", bg="deep sky blue", fg="#fff", command=self.close, font=self.text_font1)
        self.close_button.place(x=350, y=400, width=70, height=30)

    def book_appointment(self):
        strspec = self.cmb_specialization.get()
        strdname = self.cmb_doctor_name.get()
        strdate = self.cal_adate.get_date()

        a = strdname.split(" << ")
        strdid = a[0]
        strpid = cfg.pid

        if strspec != "--Select--" and strdname != "--Select--" and len(strdate)>0:
            if not os.path.exists('..\\db'):
                os.makedirs('..\\db')
            con = sqlite3.connect("..\\db\\user_datas.db")
            cursorObj = con.cursor()

            cursorObj.execute('CREATE TABLE IF NOT EXISTS book_appointment_form (hosp_id_name text, doctor_id text, patient_id text, appointment_date text, consultation text)')

            idata = cursorObj.execute(
                'INSERT INTO book_appointment_form(hosp_id_name, doctor_id, patient_id, appointment_date, consultation) VALUES(?,?,?,?,?)',
                (self.hosp_id_name, strdid, strpid, strdate, "0"))

            con.commit()
            con.close()
            print("Consulting was done Successfully...")
            messagebox.showinfo("Success", "Appointment was booked Successfully...")
            self.root.destroy()
        else:
            messagebox.showinfo("Info Message", "Please fill all fields...")

    def close(self):
        self.root.destroy()

root = Tk()
root.title("Book Appointment GUI")
root.geometry('800x500')
root.resizable(0, 0)
root.configure(bg='white')
od = BookAppointment(root)
root.mainloop()
