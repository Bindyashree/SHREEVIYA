import time
from tkinter import messagebox

import sqlite3
from tkinter import *
import os
from tkinter.filedialog import asksaveasfile

from EHR.DataSecurity.Existing_Elgamal import Existing_Elgamal
from EHR.DataSecurity.Existing_AES import Existing_AES
from EHR.DataSecurity.Existing_RSA import Existing_RSA
from EHR.DataSecurity.Existing_ECC import Existing_ECC
from EHR.DataSecurity.Proposed_ECGRCC import Proposed_ECGRCC

from EHR.Authentication.Substitute_Cipher import Substitute_Cipher

class Doctor_Registration():
    def __init__(self, root):
        self.hosp_id_name = StringVar()
        self.pid = StringVar()
        self.specialization = StringVar()
        self.sex = StringVar()

        self.hosp_id_name = "H1 : MIOT Hospital"

        self.large_font = ("Algerian", 16)
        self.text_font = ("Constantia", 15)
        self.text_font1 = ("Constantia", 11)

        self.root = root
        self.label_heading = Label(root, text="Doctor Registration Form", fg="deep pink", bg="azure3", font=self.large_font)
        self.label_heading.place(x=110, y=30)

        self.label_hosp_id = Label(root, text="Hospital Id & Name", bg='azure3', font=13)
        self.label_hosp_id.place(x=20, y=70)
        self.entry_hosp_id_name = Entry(root, bg='azure3', font=13)
        self.entry_hosp_id_name.place(x=220, y=70, width=250, height=20)
        self.entry_hosp_id_name.insert(INSERT,"H1 : MIOT Hospital")
        self.entry_hosp_id_name.configure(state="disabled")

        self.create_pid()
        self.label_doctor_id = Label(root, text="Doctor ID", bg="azure3", font=13)
        self.label_doctor_id.place(x=20, y=120)
        self.entry_doctor_id = Entry(root, bg='azure3', font=13)
        self.entry_doctor_id.place(x=220, y=120, width=250, height=20)
        self.entry_doctor_id.insert(INSERT, self.pid)
        self.entry_doctor_id.configure(state="disabled")

        self.label_doctor_name = Label(root, text="Doctor Name", bg="azure3", font=13)
        self.label_doctor_name.place(x=20, y=170)
        self.entry_doctor_name = Entry(root)
        self.entry_doctor_name.place(x=220, y=170, width=250, height=20)

        self.label_age = Label(root, text="Age", bg="azure3", font=13)
        self.label_age.place(x=20, y=220)
        self.entry_age = Entry(root)
        self.entry_age.place(x=220, y=220, width=250, height=20)

        self.label_sex = Label(root, text="Sex", bg="azure3", font=13)
        self.label_sex.place(x=20, y=270)
        self.rbt_male = Radiobutton(root, text="Male", value=0, command=self.s_male)
        self.rbt_male.place(x=220, y=270)
        self.rbt_female = Radiobutton(root, text="FeMale", value=1, command=self.s_female)
        self.rbt_female.place(x=400, y=270)

        self.label_cno = Label(root, text="Contact No.", bg="azure3", font=13)
        self.label_cno.place(x=20, y=320)
        self.entry_cno = Entry(root)
        self.entry_cno.place(x=220, y=320, width=250, height=20)

        self.label_place = Label(root, text="Place", bg="azure3", font=13)
        self.label_place.place(x=20, y=370)
        self.entry_place = Entry(root)
        self.entry_place.place(x=220, y=370, width=250, height=20)

        self.label_pid_mark = Label(root, text="Personal Identification\nMark", bg="azure3", font=13)
        self.label_pid_mark.place(x=20, y=420)
        self.entry_pid_mark = Entry(root)
        self.entry_pid_mark.place(x=220, y=420, width=250, height=20)

        self.label_specialization = Label(root, text="Specialization", bg="azure3", font=13)
        self.label_specialization.place(x=20, y=470)
        specialization = ["Orthopedics", "Gynecology", "Dermatology", "Pediatrics", "General Surgery", "ENT", "Ophthalmology"]
        self.option_menu_specialization = OptionMenu(root, self.specialization, *specialization)
        self.specialization.set("---Select---")
        self.option_menu_specialization.place(x=220, y=470, width=250, height=25)

        self.label_user_name = Label(root, text="User Name", bg="azure3", font=13)
        self.label_user_name.place(x=20, y=520)
        self.entry_user_name = Entry(root)
        self.entry_user_name.place(x=220, y=520, width=250, height=20)

        self.label_pwd = Label(root, text="Password", bg='azure3', font=13)
        self.label_pwd.place(x=20, y=570)
        self.entry_pwd = Entry(root, show="*")
        self.entry_pwd.place(x=220, y=570, width=250, height=20)

        self.label_retype_pwd = Label(root, text="Retype Password", bg='azure3', font=13)
        self.label_retype_pwd.place(x=20, y=620)
        self.entry_rpwd = Entry(root, show="*")
        self.entry_rpwd.place(x=220, y=620, width=250, height=20)

        self.submit_button = Button(root, text="Submit", bg="deep sky blue", fg="#fff", command=self.submit, font=self.text_font1)
        self.submit_button.place(x=50, y=650, width=70, height=30)
        self.clear_button = Button(root, text="Clear", bg="deep sky blue", fg="#fff", command=self.clear, font=self.text_font1)
        self.clear_button.place(x=150, y=650, width=70, height=30)
        self.back_button = Button(root, text="Back", bg="deep sky blue", fg="#fff", command=self.back, font=self.text_font1)
        self.back_button.place(x=250, y=650, width=70, height=30)
        self.close_button = Button(root, text="Close", bg="deep sky blue", fg="#fff", command=self.close, font=self.text_font1)
        self.close_button.place(x=350, y=650, width=70, height=30)

    def back(self):
        self.root.destroy()

    def s_male(self):
        self.sex = "Male"

    def s_female(self):
        self.sex = "FeMale"

    def close(self):
        self.root.destroy()

    def create_pid(self):
        if not os.path.exists('..\\db'):
            os.makedirs('..\\db')
        con = sqlite3.connect("..\\db\\user_datas.db")
        cursorObj = con.cursor()
        cursorObj.execute('CREATE TABLE IF NOT EXISTS doctor_detail_form (hosp_id_name text, doctor_id text, doctor_name text, age text, sex text, cno text, place text, specialization text, pidmark text,'
                          'user_name text, password text, eelpubkey text, eelprkey text, eaespubkey text, eaesprkey text, ersapubkey text, ersaprkey text, eeccpubkey text, eeccprkey text, peccpubkey text, peccprkey text)')
        sdata = cursorObj.execute("SELECT doctor_id FROM doctor_detail_form")
        sdata = cursorObj.fetchall()
        uid = ""
        uid1 = ""
        if len(sdata) == 0:
            self.pid = "D001"
        else:
            uid1 = sdata[-1]
            struid = ""
            for item in uid1:
                struid = item
            struid.split(" ")
            list_id = struid[1:]
            list_id_int = int(list_id)
            list_id_add_no = list_id_int + 0
            maximum = max(list_id)
            maximum_int_value = int(maximum)
            maximum_int_value += 1
            string = str(maximum_int_value)
            a = len(string)
            if a == 1:
                b = "D00"
                c = b + str(maximum_int_value)
                self.pid = c
            elif a == 2:
                b = "D0"
                c = b + str(maximum_int_value)
                self.pid = c
            else:
                b = "D"
                c = b + str(maximum_int_value)
                self.pid = c
        con.commit()
        con.close()

    def submit(self):
        strhidname = self.entry_hosp_id_name.get()
        strdid = self.entry_doctor_id.get()
        strname = self.entry_doctor_name.get()
        strage = self.entry_age.get()
        strsex = self.sex
        strcno = self.entry_cno.get()
        strplace = self.entry_place.get()
        strspec = self.specialization.get()
        struname = self.entry_user_name.get()
        strpwd = self.entry_pwd.get()
        strrpwd = self.entry_rpwd.get()
        strpim = self.entry_pid_mark.get()

        if strname == "" or strage == "" or strcno=="" or strplace == "" or struname == "" or strpwd == "" or strrpwd == "":
            messagebox.showerror("Warning", "Field should not be empty")
        else:
            namebool = False
            agebool = False
            cnobool = False
            placebool = False
            specbool = False
            unamebool = False
            pwdbool = False
            rpwdbool = False
            epwdbool = False

            errname=''
            errage=''
            errcno=''
            errplace=''
            errspec=''
            erruname=''
            errpwd=''
            errrpwd=''
            errepwd=''

            if len(strname) >3:
                if len(strname)<20:
                    namebool = True
                else:
                    namebool = False
                    errname='Name should be less than 20 characters...'
            else:
                namebool = False
                errname = 'Name should be greater than 3 characters...'
#============================================================================
            if len(strage) < 3:
                agebool = True
            else:
                agebool = False
                errname = 'Age should be less than 3 characters...'
# ============================================================================
            if len(strcno) >9:
                if len(strplace)<13:
                    cnobool = True
                else:
                    cnobool = False
                    errcno ='Contact no. should be less than 13 characters...'
            else:
                cnobool = False
                errcno = 'Contact no. should be greater than 9 characters...'
#=============================================================================
            if len(strplace) >3:
                if len(strplace)<20:
                    placebool = True
                else:
                    placebool = False
                    errplace='Address should be less than 20 characters...'
            else:
                placebool = False
                errplace = 'Address should be greater than 3 characters...'
# ============================================================================
            if len(strspec) >0:
                specbool = True
            else:
                specbool = False
                errspec = "Select anyone of the Specialization..."
# ============================================================================
            if len(struname) >3:
                if len(struname)<20:
                    unamebool = True
                else:
                    unamebool = False
                    erruname='User Name should be less than 20 characters...'
            else:
                unamebool = False
                erruname = 'User Name should be greater than 3 characters...'
# ============================================================================
            if len(strpwd) > 3:
                if len(strpwd) < 20:
                    pwdbool = True
                else:
                    pwdbool = False
                    errpwd = 'Password should be less than 20 characters...'
            else:
                pwdbool = False
                errpwd = 'Password should be greater than 3 characters...'
# ============================================================================
            if len(strrpwd) > 3:
                if len(strrpwd) < 20:
                    rpwdbool = True
                else:
                    rpwdbool = False
                    errrpwd = 'Retype Password should be less than 20 characters...'
            else:
                pwdbool = False
                errpwd = 'Retype Password should be greater than 3 characters...'
# ============================================================================
            if strpwd == strrpwd:
                epwdbool = True
            else:
                epwdbool = False
                errepwd = 'Password should be equal...'
            if namebool:
                if agebool:
                    if cnobool:
                        if placebool:
                            if specbool:
                                if unamebool:
                                    if pwdbool:
                                        if rpwdbool:
                                            if epwdbool:
                                                try:
                                                    if not os.path.exists('..//db//'):
                                                        os.makedirs('..//db//')

                                                    con = sqlite3.connect("..\\db\\user_datas.db")
                                                    cursorObj = con.cursor()
                                                    sqlite_select_query = """SELECT user_name from doctor_detail_form"""
                                                    cursorObj.execute(sqlite_select_query)
                                                    records = cursorObj.fetchall()

                                                    streelpubkey, streelprkey = Existing_Elgamal.keyGeneration(self)
                                                    streaespubkey, streaesprkey = Existing_AES.keyGeneration(self)
                                                    strersapubkey, strersaprkey = Existing_RSA.keyGeneration(self)
                                                    streeccpubkey, streeccprkey = Existing_ECC.keyGeneration(self)
                                                    strpeccpubkey, strpeccprkey = Proposed_ECGRCC.keyGeneration(self)

                                                    if not os.path.exists("..\\Keys\\" + str(strdid)):
                                                        os.makedirs("..\\Keys\\" + str(strdid))

                                                    eaeskey = Existing_AES.key_create(self)
                                                    Existing_AES.key_write(self, eaeskey, "..\\Keys\\" + str(strdid) + "\\ExistingAESKey.key")

                                                    eelkey = Existing_Elgamal.key_create(self)
                                                    Existing_Elgamal.key_write(self, eelkey, "..\\Keys\\" + str(strdid) + "\\ExistingELKey.key")

                                                    ersakey = Existing_RSA.key_create(self)
                                                    Existing_RSA.key_write(self, ersakey, "..\\Keys\\" + str(strdid) + "\\ExistingRSAKey.key")

                                                    eecckey = Existing_ECC.key_create(self)
                                                    Existing_ECC.key_write(self, eecckey, "..\\Keys\\" + str(strdid) + "\\ExistingECCKey.key")

                                                    stime = int(time.time() * 1000)
                                                    pecckey = Proposed_ECGRCC.key_create(self)
                                                    Proposed_ECGRCC.key_write(self, pecckey, "..\\Keys\\" + str(strdid) + "\\ProposedECGRCCKey.key")
                                                    etime = int(time.time() * 1000)
                                                    ktime = etime - stime

                                                    un = []
                                                    for row in records:
                                                        un.append(row[0])
                                                    if struname not in un:
                                                        idata = cursorObj.execute(
                                                                'INSERT INTO doctor_detail_form(hosp_id_name, doctor_id, doctor_name, age, sex, cno, place, specialization, pidmark, user_name, password, eelpubkey, eelprkey, eaespubkey, eaesprkey, ersapubkey, ersaprkey, eeccpubkey, eeccprkey, peccpubkey, peccprkey) '
                                                                'VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                                                                (strhidname, strdid, strname, strage, strsex, strcno, strplace, strspec, strpim, struname, strpwd, str(streelpubkey), str(streelprkey), str(streaespubkey), str(streaesprkey),
                                                                 str(strersapubkey), str(strersaprkey), str(streeccpubkey), str(streeccprkey), str(strpeccpubkey), str(strpeccprkey)))

                                                        if not os.path.exists('..//SecretCode//'):
                                                            os.makedirs('..//SecretCode//')

                                                        key = Substitute_Cipher.generate_key(self)
                                                        enc_text = Substitute_Cipher.encrypt(self, strpim, key)

                                                        file = open("..\\SecretCode\\" + str(strdid) + " SecretCode.txt", 'w')
                                                        file.write(str(enc_text))
                                                        file.close()

                                                        f = asksaveasfile(initialfile=str(strdid) + ' SecretCode.txt',
                                                                          defaultextension=".txt",
                                                                          filetypes=[("All Files", "*.*"),
                                                                                     ("Text Documents", "*.txt")])

                                                        file = open(f.name, 'w')
                                                        file.write(str(enc_text))
                                                        file.close()

                                                        print("Doctor Registration was done Successfully...")
                                                        messagebox.showinfo("Success", "Doctor Registration was done Successfully...")

                                                        print("\nDoctor Registration")
                                                        print("======================")
                                                        print("Hospital ID & Name : " + str(strhidname))
                                                        print("Doctor ID : "+str(strdid))
                                                        print("Doctor Name : "+str(strname))
                                                        print("Contact Number : " + str(strcno))
                                                        print("Place : "+str(strplace))
                                                        print("Specialization : " + str(strspec))
                                                        print("Personal Identification Mark : " + str(strpim))
                                                        print("User Name : "+str(struname))
                                                        print("Password : "+str(strpwd))
                                                        print("Public Key : "+str(strpeccpubkey))
                                                        print("Private Key : " + str(strpeccprkey))
                                                        print("Key Generation Time : " + str(ktime) + " ms")
                                                        con.commit()
                                                        con.close()
                                                        self.create_pid()
                                                        self.entry_doctor_id.configure(state="normal")
                                                        self.entry_doctor_id.delete(0, 'end')
                                                        self.entry_doctor_id.insert(INSERT, self.pid)
                                                        self.entry_doctor_id.configure(state="disabled")
                                                        self.clear()

                                                    else:
                                                        messagebox.showinfo("Warning", "Doctor is already available...")
                                                        self.entry_user_name.delete(0, 'end')
                                                        self.entry_pwd.delete(0, 'end')
                                                        self.entry_rpwd.delete(0, 'end')
                                                except Exception as e:
                                                    print(e.args)
                                        else:
                                            messagebox.showinfo("Warning", errrpwd)
                                    else:
                                        messagebox.showinfo("Warning", errpwd)
                                else:
                                    messagebox.showinfo("Warning", erruname)
                            else:
                                messagebox.showinfo("Warning", errspec)
                        else:
                            messagebox.showinfo("Warning", errplace)
                    else:
                        messagebox.showinfo("Warning", errcno)
                else:
                    messagebox.showinfo("Warning", errage)
            else:
                messagebox.showinfo("Warning", errname)

    def clear(self):
        self.entry_doctor_name.delete(0, 'end')
        self.entry_age.delete(0, 'end')
        self.entry_cno.delete(0, 'end')
        self.entry_place.delete(0, 'end')
        self.entry_user_name.delete(0, 'end')
        self.entry_pwd.delete(0, 'end')
        self.entry_rpwd.delete(0, 'end')
        self.entry_pid_mark.delete(0, 'end')
        self.specialization.set("---Select---")

root = Tk ()
root.title("Doctor Registration Window")
root.geometry('500x700+400+0')
root.resizable(0, 0)
root.configure(bg='azure3')
regis = Doctor_Registration(root)
root.mainloop ()
