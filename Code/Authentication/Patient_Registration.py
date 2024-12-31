import time
from tkinter import messagebox
# import qrcode
import sqlite3
from tkinter import *
from tkinter import ttk
import os
from tkinter.filedialog import asksaveasfile

from EHR.DataSecurity.Existing_Elgamal import Existing_Elgamal
from EHR.DataSecurity.Existing_AES import Existing_AES
from EHR.DataSecurity.Existing_RSA import Existing_RSA
from EHR.DataSecurity.Existing_ECC import Existing_ECC
from EHR.DataSecurity.Proposed_ECGRCC import Proposed_ECGRCC

from EHR.Authentication.Substitute_Cipher import Substitute_Cipher

# import segno

class Patient_Registration():

    def __init__(self, root):
        self.hosp_id_name = StringVar()
        self.pid = StringVar()
        self.sex = StringVar()

        self.hid = "H1"
        self.hname = "MIOT Hospital"

        self.hosp_id_name = str(self.hid)+" : "+str(self.hname)

        self.large_font = ("Algerian", 16)
        self.text_font = ("Constantia", 15)
        self.text_font1 = ("Constantia", 11)

        self.root = root
        self.label_heading = Label(root, text="Patient Registration Form", fg="deep pink", bg="azure3", font=self.large_font)
        self.label_heading.place(x=110, y=10)

        self.label_hosp_id = Label(root, text="Hospital Id & Name", bg='azure3', font=13)
        self.label_hosp_id.place(x=20, y=50)
        self.entry_hosp_id_name = Entry(root, bg='azure3', font=13)
        self.entry_hosp_id_name.place(x=180, y=50, width=300, height=20)
        self.entry_hosp_id_name.insert(INSERT,"H1 : MIOT Hospital")
        self.entry_hosp_id_name.configure(state="disabled")

        self.create_pid()
        self.label_patient_id = Label(root, text="Patient ID", bg="azure3", font=13)
        self.label_patient_id.place(x=20, y=100)
        self.entry_patient_id = Entry(root, bg='azure3', font=13)
        self.entry_patient_id.place(x=180, y=100, width=300, height=20)
        self.entry_patient_id.insert(INSERT, self.pid)
        self.entry_patient_id.configure(state="disabled")

        csg=["Aadhar Cord No.", "Voter ID No.", "PAN Card No."]
        self.label_csg_no = Label(root, text="CSG No.", bg="azure3", font=13)
        self.label_csg_no.place(x=20, y=150)
        self.combbox_csg = ttk.Combobox(root, values=csg, width=15)
        self.combbox_csg.place(x=180, y=150)
        self.combbox_csg.set("--Select--")
        self.combbox_csg["state"] = "readonly"
        self.entry_csg_no = Entry(root)
        self.entry_csg_no.place(x=300, y=150, width=180, height=20)

        self.label_patient_name = Label(root, text="Patient Name", bg="azure3", font=13)
        self.label_patient_name.place(x=20, y=200)
        self.entry_patient_name = Entry(root)
        self.entry_patient_name.place(x=180, y=200, width=300, height=20)

        self.label_age = Label(root, text="Age", bg="azure3", font=13)
        self.label_age.place(x=20, y=250)
        self.entry_age = Entry(root)
        self.entry_age.place(x=180, y=250, width=300, height=20)

        self.label_sex = Label(root, text="Sex", bg="azure3", font=13)
        self.label_sex.place(x=20, y=300)
        self.rbt_male = Radiobutton(root, text="Male", value=1, command=self.s_male)
        self.rbt_male.place(x=180, y=300)
        self.rbt_female = Radiobutton(root, text="FeMale", value=0, command=self.s_female)
        self.rbt_female.place(x=400, y=300)

        self.label_cno = Label(root, text="Contact No.", bg="azure3", font=13)
        self.label_cno.place(x=20, y=350)
        self.entry_cno = Entry(root)
        self.entry_cno.place(x=180, y=350, width=300, height=20)

        self.label_place = Label(root, text="Place", bg="azure3", font=13)
        self.label_place.place(x=20, y=400)
        self.entry_place = Entry(root)
        self.entry_place.place(x=180, y=400, width=300, height=20)

        self.label_pid_mark = Label(root, text="Personal Identification\nMark", bg="azure3", font=13)
        self.label_pid_mark.place(x=20, y=440)
        self.entry_pid_mark = Entry(root)
        self.entry_pid_mark.place(x=180, y=450, width=300, height=20)

        self.label_user_name = Label(root, text="User Name", bg="azure3", font=13)
        self.label_user_name.place(x=20, y=500)
        self.entry_user_name = Entry(root)
        self.entry_user_name.place(x=180, y=500, width=300, height=20)

        self.label_pwd = Label(root, text="Password", bg='azure3', font=13)
        self.label_pwd.place(x=20, y=550)
        self.entry_pwd = Entry(root, show="*")
        self.entry_pwd.place(x=180, y=550, width=300, height=20)

        self.label_retype_pwd = Label(root, text="Retype Password", bg='azure3', font=13)
        self.label_retype_pwd.place(x=20, y=600)
        self.entry_rpwd = Entry(root, show="*")
        self.entry_rpwd.place(x=180, y=600, width=300, height=20)

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

        cursorObj.execute('CREATE TABLE IF NOT EXISTS patient_detail_form (hosp_id_name text, patient_id text, patient_csgno text, patient_name text, age text, sex text, cno text, place text, pidmark text, '
                          'user_name text, password text, eelpubkey text, eelprkey text, eaespubkey text, eaesprkey text, ersapubkey text, ersaprkey text, eeccpubkey text, eeccprkey text, peccpubkey text, peccprkey text)')
        sdata = cursorObj.execute("SELECT patient_id FROM patient_detail_form")
        sdata = cursorObj.fetchall()
        uid = ""
        uid1 = ""
        if len(sdata) == 0:
            self.pid = "P001"
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
                b = "P00"
                c = b + str(maximum_int_value)
                self.pid = c
            elif a == 2:
                b = "P0"
                c = b + str(maximum_int_value)
                self.pid = c
            else:
                b = "P"
                c = b + str(maximum_int_value)
                self.pid = c
        con.commit()
        con.close()

    def submit(self):
        strhidname = self.entry_hosp_id_name.get()
        strpid = self.entry_patient_id.get()
        strpcsgno = self.entry_csg_no.get()
        strpname = self.entry_patient_name.get()
        strpage = self.entry_age.get()
        strpsex = self.sex
        strpcno = self.entry_cno.get()
        strpplace = self.entry_place.get()
        strpuname = self.entry_user_name.get()
        strppwd = self.entry_pwd.get()
        strprpwd = self.entry_rpwd.get()
        strpim = self.entry_pid_mark.get()

        strcmb = self.combbox_csg.get()

        if strcmb == "--Select--" or strpcsgno == "" or strpname == "" or strpage == "" or strpcno=="" or strpplace == "" or strpuname == "" or strppwd == "" or strprpwd == "":
            messagebox.showerror("Warning", "Field should not be empty")
        else:
            csgnobool = False
            namebool = False
            agebool = False
            cnobool = False
            placebool = False
            unamebool = False
            pwdbool = False
            rpwdbool = False
            epwdbool = False

            errcsgno=''
            errname=''
            errage=''
            errcno=''
            errplace=''
            erruname=''
            errpwd=''
            errrpwd=''
            errepwd=''

            if len(strpcsgno) >3:
                if len(strpcsgno)<20:
                    csgnobool = True
                else:
                    csgnobool = False
                    errcsgno= self.entry_csg_no.get()+' should be less than 20 characters...'
            else:
                csgnobool = False
                errcsgno = self.entry_csg_no.get()+' should be less than 20 characters...'
# ============================================================================
            if len(strpname) >3:
                if len(strpname)<20:
                    namebool = True
                else:
                    namebool = False
                    errname='Name should be less than 20 characters...'
            else:
                namebool = False
                errname = 'Name should be greater than 3 characters...'
#============================================================================
            if len(strpage) < 3:
                if int(strpage) > 0 and int(strpage) <110:
                    agebool = True
                else:
                    agebool = False
                    errname = 'Enter correct age...'
            else:
                agebool = False
                errname = 'Age should be less than 3 characters...'
# ============================================================================
            if len(strpcno) >9:
                if len(strpcno)<13:
                    cnobool = True
                else:
                    cnobool = False
                    errcno ='Contact no. should be less than 13 characters...'
            else:
                cnobool = False
                errcno = 'Contact no. should be greater than 9 characters...'
#=============================================================================
            if len(strpplace) >3:
                if len(strpplace)<20:
                    placebool = True
                else:
                    placebool = False
                    errplace='Address should be less than 20 characters...'
            else:
                placebool = False
                errplace = 'Address should be greater than 3 characters...'
# ============================================================================
            if len(strpuname) >3:
                if len(strpuname)<20:
                    unamebool = True
                else:
                    unamebool = False
                    erruname='User Name should be less than 20 characters...'
            else:
                unamebool = False
                erruname = 'User Name should be greater than 3 characters...'
# ============================================================================
            if len(strppwd) > 3:
                if len(strppwd) < 20:
                    pwdbool = True
                else:
                    pwdbool = False
                    errpwd = 'Password should be less than 20 characters...'
            else:
                pwdbool = False
                errpwd = 'Password should be greater than 3 characters...'
# ============================================================================
            if len(strprpwd) > 3:
                if len(strprpwd) < 20:
                    rpwdbool = True
                else:
                    rpwdbool = False
                    errrpwd = 'Retype Password should be less than 20 characters...'
            else:
                pwdbool = False
                errpwd = 'Retype Password should be greater than 3 characters...'
# ============================================================================
            if strppwd == strprpwd:
                epwdbool = True
            else:
                epwdbool = False
                errepwd = 'Password should be equal...'
            if csgnobool:
                if namebool:
                    if agebool:
                        if cnobool:
                            if placebool:
                                if unamebool:
                                    if pwdbool:
                                        if rpwdbool:
                                            if epwdbool:
                                                # try:
                                                    if not os.path.exists('..//db//'):
                                                        os.makedirs('..//db//')

                                                    con = sqlite3.connect("..\\db\\user_datas.db")
                                                    cursorObj = con.cursor()
                                                    sqlite_select_query = """SELECT user_name from patient_detail_form"""
                                                    cursorObj.execute(sqlite_select_query)
                                                    records = cursorObj.fetchall()

                                                    un = []
                                                    for row in records:
                                                        un.append(row[0])
                                                    if strpuname not in un:
                                                        streelpubkey, streelprkey = Existing_Elgamal.keyGeneration(self)
                                                        streaespubkey, streaesprkey = Existing_AES.keyGeneration(self)
                                                        strersapubkey, strersaprkey = Existing_RSA.keyGeneration(self)
                                                        streeccpubkey, streeccprkey = Existing_ECC.keyGeneration(self)
                                                        strpeccpubkey, strpeccprkey = Proposed_ECGRCC.keyGeneration(self)

                                                        if not os.path.exists("..\\Keys\\" + str(strpid)):
                                                            os.makedirs("..\\Keys\\" + str(strpid))

                                                        eaeskey = Existing_AES.key_create(self)
                                                        Existing_AES.key_write(self, eaeskey, "..\\Keys\\" + str(strpid) + "\\ExistingAESKey.key")

                                                        eelkey = Existing_Elgamal.key_create(self)
                                                        Existing_Elgamal.key_write(self, eelkey, "..\\Keys\\" + str(strpid) + "\\ExistingELKey.key")

                                                        ersakey = Existing_RSA.key_create(self)
                                                        Existing_RSA.key_write(self, ersakey, "..\\Keys\\" + str(strpid) + "\\ExistingRSAKey.key")

                                                        eecckey = Existing_ECC.key_create(self)
                                                        Existing_ECC.key_write(self, eecckey, "..\\Keys\\" + str(strpid) + "\\ExistingECCKey.key")

                                                        stime = int(time.time() * 1000)

                                                        pecckey = Proposed_ECGRCC.key_create(self)
                                                        Proposed_ECGRCC.key_write(self, pecckey, "..\\Keys\\" + str(strpid) + "\\ProposedECGRCCKey.key")
                                                        etime = int(time.time() * 1000)
                                                        ktime = etime - stime


                                                        strpcsgno = (strpcsgno)
                                                        strpcno = (strpcno)
                                                        cursorObj.execute('INSERT INTO patient_detail_form(hosp_id_name, patient_id, patient_csgno, patient_name, age, sex, cno, place, pidmark, user_name, password, eelpubkey, eelprkey, '
                                                                          'eaespubkey, eaesprkey, ersapubkey, ersaprkey, eeccpubkey, eeccprkey, peccpubkey, peccprkey) '
                                                                                  'VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                                                                (strhidname, strpid, strpcsgno, strpname, strpage, strpsex, strpcno, strpplace, strpim, strpuname, strppwd, str(streelpubkey), str(streelprkey), str(streaespubkey),
                                                                 str(streaesprkey), str(strersapubkey), str(strersaprkey), str(streeccpubkey), str(streeccprkey), str(strpeccpubkey), str(strpeccprkey)))

                                                        if not os.path.exists('..//SecretCode//'):
                                                            os.makedirs('..//SecretCode//')

                                                        key = Substitute_Cipher.generate_key(self)
                                                        enc_text = Substitute_Cipher.encrypt(self, strpim, key)

                                                        file = open("..\\SecretCode\\" + str(strpid) + " SecretCode.txt", 'w')
                                                        file.write(str(enc_text))
                                                        file.close()

                                                        f = asksaveasfile(initialfile=str(strpid) + ' SecretCode.txt',
                                                                          defaultextension=".txt",
                                                                          filetypes=[("All Files", "*.*"),
                                                                                     ("Text Documents", "*.txt")])

                                                        file = open(f.name, 'w')
                                                        file.write(str(enc_text))
                                                        file.close()

                                                        print("\nPatient Registration")
                                                        print("======================")
                                                        print("Hospital ID & Name : " + str(strhidname))
                                                        print("Patient ID : "+str(strpid))
                                                        print("Patient Name : "+str(strpname))
                                                        print("Contact Number : " + str(strpcno))
                                                        print("Personal Identification Mark : "+str(strpim))
                                                        print("User Name : "+str(strpuname))
                                                        print("Password : "+str(strppwd))
                                                        print("Public Key : "+str(strpeccpubkey))
                                                        print("Private Key : " + str(strpeccprkey))
                                                        print(self.combbox_csg.get()+" : "+str(strpcsgno))
                                                        print("Key Generation Time : " + str(ktime)+" ms")
                                                        con.commit()
                                                        con.close()
                                                        self.create_pid()
                                                        self.entry_patient_id.configure(state="normal")
                                                        self.entry_patient_id.delete(0, 'end')
                                                        self.entry_patient_id.insert(INSERT, self.pid)
                                                        self.entry_patient_id.configure(state="disabled")
                                                        print("\nPatient Registration was done Successfully...")
                                                        messagebox.showinfo("Success", "Patient Registration was done Successfully...")

                                                        self.clear()
                                                    else:
                                                        messagebox.showinfo("Warning", "Patient is already available...")
                                                        self.entry_user_name.delete(0, 'end')
                                                        self.entry_pwd.delete(0, 'end')
                                                        self.entry_rpwd.delete(0, 'end')
                                                # except Exception as e:
                                                #     print(Exception)
                                        else:
                                            messagebox.showinfo("Warning", errrpwd)
                                    else:
                                        messagebox.showinfo("Warning", errpwd)
                                else:
                                    messagebox.showinfo("Warning", erruname)
                            else:
                                messagebox.showinfo("Warning", errplace)
                        else:
                            messagebox.showinfo("Warning", errcno)
                    else:
                        messagebox.showinfo("Warning", errage)
                else:
                    messagebox.showinfo("Warning", errname)
            else:
                messagebox.showinfo("Warning", errcsgno)

    def clear(self):
        self.entry_patient_name.delete(0, 'end')
        self.entry_age.delete(0, 'end')
        self.entry_cno.delete(0, 'end')
        self.entry_place.delete(0, 'end')
        self.entry_user_name.delete(0, 'end')
        self.entry_pwd.delete(0, 'end')
        self.entry_rpwd.delete(0, 'end')
        self.entry_csg_no.delete(0, 'end')
        self.entry_pid_mark.delete(0, 'end')
        self.combbox_csg.set("--Select--")

root = Tk ()
root.title("Patient Registration Window")
root.geometry('500x700+400+0')
root.resizable(0, 0)
root.configure(bg='azure3')
regis = Patient_Registration(root)
root.mainloop ()
