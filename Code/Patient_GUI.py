import random
import sqlite3
import time
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile
# import pandas as pd
import os
from tkinter import Tk, filedialog
from tkinter import messagebox
import datetime

from hashlib import sha512
from hashlib import blake2b

from EHR import config as cfg

from EHR.DataSecurity.Existing_AES import Existing_AES
from EHR.DataSecurity.Existing_Elgamal import Existing_Elgamal
from EHR.DataSecurity.Existing_RSA import Existing_RSA
from EHR.DataSecurity.Existing_ECC import Existing_ECC
from EHR.DataSecurity.Proposed_ECGRCC import Proposed_ECGRCC

import tracemalloc

class Patient_GUI:
    boolsfile = False
    strpid=""
    strdid=""

    def __init__(self, root):
        self.LARGE_FONT = ("Algerian", 16)
        self.text_font = ("Constantia", 15)
        self.text_font1 = ("Constantia", 10)

        self.frame_font = ("", 9)
        self.frame_process_res_font = ("", 12)
        self.root = root
        self.specialization = StringVar()
        self.dname = StringVar()
        self.ufiles = StringVar()
        self.sufiles = []

        label_heading = tkinter.Label(root, text="ETHEREUM HYPERLEDGER BLOCKCHAIN BASED SECURE EHR USING GPF-PoSCR and E-CGR-CC", fg='deep pink', bg="azure3", font=self.LARGE_FONT)
        label_heading.place(x=50, y=10)

        self.label_select_bigdata = LabelFrame(root, text='Select EHR File for Secure upload', bg="azure3", fg="#00a800", font=self.frame_font)
        self.label_select_bigdata.place(x=10, y=50, width=490, height=50)
        self.label_file_browse = Label(root, text="Browse File", bg='azure3', fg='#CD7F32', font=13)
        self.label_file_browse.place(x=15, y=70)
        self.entry_file_browse = Entry(root, font=13)
        self.entry_file_browse.place(x=110, y=70, width=250, height=25)
        self.entry_file_browse.configure(state="disabled")
        self.btn_bd_browse = Button(root, text="Click", bg="deep sky blue", fg="#fff", font=self.text_font1, width=15, command = self.browse_ehr)
        self.btn_bd_browse.place(x=365, y=70)

        self.label_doctor_name = LabelFrame(root, text='Doctor ID and Name', bg="azure3",  fg="#FF00FF",font=self.frame_font)
        self.label_doctor_name.place(x=510, y=50, width=200, height=50)

        tdate = datetime.datetime.now().strftime("%d-%m-%Y") + ""

        def dnamespec(choice):
            strspec=""
            choice = self.dname.get()
            a = str(choice).split(" << ")
            con = sqlite3.connect("..\\db\\user_datas.db")
            cursorObj = con.cursor()
            cursorObj.execute("SELECT specialization from doctor_detail_form where doctor_id='"+str(a[0])+"'")

            xresult = cursorObj.fetchall()
            if xresult:
                for xrow in xresult:
                    strspec = xrow[0]

            self.entry_specname.configure(state="normal")
            self.entry_specname.insert(INSERT, str(strspec))
            self.entry_specname.configure(state="disabled")

        def doctorname():
            dn = []
            con = sqlite3.connect("..\\db\\user_datas.db")
            cursorObj = con.cursor()
            cursorObj.execute("SELECT doctor_detail_form.doctor_id, doctor_detail_form.doctor_name FROM book_appointment_form INNER JOIN doctor_detail_form on doctor_detail_form.doctor_id = book_appointment_form.doctor_id WHERE patient_id=? AND consultation=?",
                              (str(cfg.pid), "1"))

            xresult = cursorObj.fetchall()
            if xresult:
                for xrow in xresult:
                    strval = xrow[0] + " << " + xrow[1]
                    if not dn.__contains__(strval):
                        dn.append(strval)
            return dn

        listdname=doctorname()

        self.option_menu_dname = OptionMenu(root, self.dname, *listdname, command = dnamespec)
        self.dname.set("---Select---")
        self.option_menu_dname.place(x=520, y=70, width=180, height=25)

        self.label_specialization = LabelFrame(root, text='Specialization', bg="azure3",  fg="#FF00FF",font=self.frame_font)
        self.label_specialization.place(x=730, y=50, width=200, height=50)
        self.entry_specname = Entry(root, font=13)
        self.entry_specname.place(x=740, y=70, width=180, height=25)
        self.entry_specname.configure(state="disabled")

        self.label_secure_upload = LabelFrame(root, text='Secure Upload', bg="azure3",fg="#000080", font=self.frame_font)
        self.label_secure_upload.place(x=350, y=110, width=300, height=50)
        self.btn_secure_upload = Button(root, text="Upload", bg="deep sky blue", fg="#fff", font=self.text_font1, width=30, command = self.secure_upload)
        self.btn_secure_upload.place(x=380, y=130)

        # self.btn_load = Button(root, text="Load", bg="deep sky blue", fg="#fff", font=self.text_font1, width=15, command=self.load)
        # self.btn_load.place(x=50, y=190)
        # self.label_upload = LabelFrame(root, text='Uploaded Files', bg="azure3", fg = "#8B008B", font=self.frame_font)
        # self.label_upload.place(x=200, y=170, width=370, height=50)
        #
        # self.sufiles = [""]
        # if os.path.exists("..\\CloudServer\\"+cfg.pid+"\\"):
        #     temp = getListOfFiles("..\\CloudServer\\"+cfg.pid+"\\")
        #     for x in range(len(temp)):
        #         if str(temp[x]).__contains__("ProposedECGRCC"):
        #             self.sufiles.append(str(temp[x]).replace("..\CloudServer\\\\",""))
        #
        # self.option_menu_ufiles = OptionMenu(root, self.ufiles, *self.sufiles)
        # self.ufiles.set("---Select---")
        # self.option_menu_ufiles.place(x=210, y=190, width=350, height=25)
        # self.btn_download = Button(root, text="Download", bg="deep sky blue", fg="#fff", font=self.text_font1, width=15, command=self.download)
        # self.btn_download.place(x=600, y=185)

        self.btn_exit = Button(root, text="Exit",bg="deep sky blue", fg="#fff", font=self.text_font1, width=15, command=self.close)
        self.btn_exit.place(x=750, y=130)

        # Horizontal (x) Scroll bar
        self.xscrollbar = Scrollbar(root, orient=HORIZONTAL)
        self.xscrollbar.pack(side=BOTTOM, fill=X)
        # Vertical (y) Scroll Bar
        self.yscrollbar = Scrollbar(root)
        self.yscrollbar.pack(side=RIGHT, fill=Y)

        self.label_output_frame = LabelFrame(root, text='Result Window', bg="azure3", fg="#0000FF", font=self.frame_process_res_font)
        self.label_output_frame.place(x=10, y=180, width=900, height=450)
        # Text Widget
        self.data_textarea_result = Text(root, wrap=WORD, xscrollcommand=self.xscrollbar.set, yscrollcommand=self.yscrollbar.set)
        self.data_textarea_result.pack()
        # Configure the scrollbars
        self.xscrollbar.config(command=self.data_textarea_result.xview)
        self.yscrollbar.config(command=self.data_textarea_result.yview)
        self.data_textarea_result.place(x=20, y=200, width=880, height=420)
        self.data_textarea_result.configure(state="disabled")

    def browse_ehr(self):
        self.boolsfile = True
        self.entry_file_browse.configure(state="normal")
        self.data_textarea_result.configure(state="normal")
        self.ehr_file = askopenfile(filetypes=[("Image Files", ".jpg .png")])
        path = self.ehr_file.name
        basename = os.path.basename(path)
        self.entry_file_browse.insert(INSERT, "" + str(basename))
        self.data_textarea_result.insert(INSERT, "Selected File Name : " + str(self.ehr_file.name))
        print("Selected File Name : " + str(self.ehr_file.name))
        self.entry_file_browse.configure(state="disabled")
        self.data_textarea_result.configure(state="disabled")
        self.btn_bd_browse.configure(state="disabled")

    def close(self):
        self.root.destroy()

    def secure_upload(self):
        if self.boolsfile:
            strspec = self.specialization.get()
            strdname = self.dname.get()

            if not strspec=="---Select---":
                if not strdname=="---Select---":
                    self.data_textarea_result.configure(state="normal")
                    path = self.ehr_file.name

                    strpdval = strdname.split(" << ")
                    basename = os.path.basename(path)

                    dpubkey=getDoctorPublicKey(strpdval[0])
                    ppubkey=getPatientPublicKey(cfg.pid)

                    did = strdname.split(" << ")

                    if not os.path.exists("..\\CloudServer\\"+str(cfg.pid)+"\\"+str(did[0])+"\\ExistingAES\\"):
                        os.makedirs("..\\CloudServer\\"+str(cfg.pid)+"\\"+str(did[0])+"\\ExistingAES\\")
                    if not os.path.exists("..\\CloudServer\\"+str(cfg.pid)+"\\"+str(did[0])+"\\ExistingEL\\"):
                        os.makedirs("..\\CloudServer\\"+str(cfg.pid)+"\\"+str(did[0])+"\\ExistingEL\\")
                    if not os.path.exists("..\\CloudServer\\"+str(cfg.pid)+"\\"+str(did[0])+"\\ExistingRSA\\"):
                        os.makedirs("..\\CloudServer\\"+str(cfg.pid)+"\\"+str(did[0])+"\\ExistingRSA\\")
                    if not os.path.exists("..\\CloudServer\\"+str(cfg.pid)+"\\"+str(did[0])+"\\ExistingECC\\"):
                        os.makedirs("..\\CloudServer\\"+str(cfg.pid)+"\\"+str(did[0])+"\\ExistingECC\\")
                    if not os.path.exists("..\\CloudServer\\"+str(cfg.pid)+"\\"+str(did[0])+"\\ProposedECGRCC\\"):
                        os.makedirs("..\\CloudServer\\"+str(cfg.pid)+"\\"+str(did[0])+"\\ProposedECGRCC\\")

                    print("\nEHR Security")
                    print("==============")
                    self.data_textarea_result.insert(INSERT, "\nEHR Security")
                    self.data_textarea_result.insert(INSERT, "\n==============")
                    print("Existing Advanced Encryption Standard (AES) Algorithm")
                    print("-----------------------------------------------------")
                    self.data_textarea_result.insert(INSERT, "\nExisting Advanced Encryption Standard (AES) Algorithm")
                    self.data_textarea_result.insert(INSERT, "\n-----------------------------------------------------")
                    tracemalloc.start()
                    stime = int(time.time() * 1000)
                    eaeskey = Existing_AES.key_load(self, "..\\Keys\\" + str(cfg.pid) + "\\ExistingAESKey.key")
                    eaesslevel, eaesalevel = Existing_AES.file_encrypt(self, eaeskey, self.ehr_file.name,
                                                              "..\\CloudServer\\" + str(cfg.pid) + "\\" + str(did[0]) + "\\ExistingAES\\" + basename)
                    etime = int(time.time() * 1000)
                    eaestime = etime - stime
                    eaesmu = tracemalloc.get_traced_memory()
                    print("Encryption Time : " + str(eaestime) + " ms")
                    print("Memory Usage : " + str(eaesmu[1]) + " kb")
                    print("Security Level : " + str(eaesslevel) + " %")
                    print("Attack Level : " + str(eaesalevel) + " %")
                    self.data_textarea_result.insert(INSERT, "\nEncryption Time : " + str(eaestime) + " ms")
                    self.data_textarea_result.insert(INSERT, "\nMemory Usage : " + str(eaesmu[1]) + " kb")
                    self.data_textarea_result.insert(INSERT, "\nSecurity Level : " + str(eaesslevel) + " %")
                    self.data_textarea_result.insert(INSERT, "\nAttack Level : " + str(eaesalevel) + " %")

                    print("\nExisting ElGamal Algorithm")
                    print("----------------------------")
                    self.data_textarea_result.insert(INSERT, "\n\nExisting ElGamal Algorithm")
                    self.data_textarea_result.insert(INSERT, "\n----------------------------")
                    tracemalloc.start()
                    stime = int(time.time() * 1000)
                    eelkey = Existing_Elgamal.key_load(self, "..\\Keys\\" + str(cfg.pid) + "\\ExistingELKey.key")
                    eelslevel, eelalevel = Existing_Elgamal.file_encrypt(self, eelkey, self.ehr_file.name,"..\\CloudServer\\" + str(cfg.pid) + "\\" + str(did[0]) + "\\ExistingEL\\" + basename)
                    etime = int(time.time() * 1000)
                    eeltime = etime-stime
                    eelmu = tracemalloc.get_traced_memory()
                    print("Encryption Time : "+str(eeltime)+" ms")
                    print("Memory Usage : " + str(eelmu[1]) + " kb")
                    print("Security Level : " + str(eelslevel) + " %")
                    print("Attack Level : " + str(eelalevel) + " %")
                    self.data_textarea_result.insert(INSERT, "\nEncryption Time : "+str(eeltime)+" ms")
                    self.data_textarea_result.insert(INSERT, "\nMemory Usage : " + str(eelmu[1]) + " kb")
                    self.data_textarea_result.insert(INSERT, "\nSecurity Level : " + str(eelslevel) + " %")
                    self.data_textarea_result.insert(INSERT, "\nAttack Level : " + str(eelalevel) + " %")

                    print("\nExisting Rivest-Shamir-Adleman (RSA) Algorithm")
                    print("------------------------------------------------")
                    self.data_textarea_result.insert(INSERT, "\n\nExisting Rivest-Shamir-Adleman (RSA) Algorithm")
                    self.data_textarea_result.insert(INSERT, "\n------------------------------------------------")
                    tracemalloc.start()
                    stime = int(time.time() * 1000)
                    ersakey = Existing_RSA.key_load(self, "..\\Keys\\" + str(cfg.pid) + "\\ExistingRSAKey.key")
                    ersaslevel, ersaalevel = Existing_RSA.file_encrypt(self, ersakey, self.ehr_file.name,"..\\CloudServer\\" + str(cfg.pid) + "\\" + str(did[0]) + "\\ExistingRSA\\" + basename)
                    etime = int(time.time() * 1000)
                    ersatime = etime - stime
                    ersamu = tracemalloc.get_traced_memory()
                    print("Encryption Time : "+str(ersatime)+" ms")
                    print("Memory Usage : " + str(ersamu[1]) + " kb")
                    print("Security Level : " + str(ersaslevel) + " %")
                    print("Attack Level : " + str(ersaalevel) + " %")
                    self.data_textarea_result.insert(INSERT, "\nEncryption Time : "+str(ersatime)+" ms")
                    self.data_textarea_result.insert(INSERT, "\nMemory Usage : " + str(ersamu[1]) + " kb")
                    self.data_textarea_result.insert(INSERT, "\nSecurity Level : " + str(ersaslevel) + " %")
                    self.data_textarea_result.insert(INSERT, "\nAttack Level : " + str(ersaalevel) + " %")

                    print("\nExisting Elliptic Curve Cryptography (ECC) Algorithm")
                    print("------------------------------------------------------")
                    self.data_textarea_result.insert(INSERT, "\n\nExisting Elliptic Curve Cryptography (ECC) Algorithm")
                    self.data_textarea_result.insert(INSERT, "\n------------------------------------------------------")
                    tracemalloc.start()
                    stime = int(time.time() * 1000)
                    eecckey = Existing_ECC.key_load(self, "..\\Keys\\"+str(cfg.pid)+"\\ExistingECCKey.key")
                    eeccslevel, eeccalevel = Existing_ECC.file_encrypt(self, eecckey, self.ehr_file.name, "..\\CloudServer\\"+str(cfg.pid)+"\\"+str(did[0])+"\\ExistingECC\\"+basename)
                    etime = int(time.time() * 1000)
                    eecctime = etime - stime
                    eeccmu = tracemalloc.get_traced_memory()
                    print("Encryption Time : "+str(eecctime)+" ms")
                    print("Memory Usage : " + str(eeccmu[1]) + " kb")
                    print("Security Level : " + str(eeccslevel) + " %")
                    print("Attack Level : " + str(eeccslevel) + " %")
                    self.data_textarea_result.insert(INSERT, "\nEncryption Time : "+str(eecctime)+" ms")
                    self.data_textarea_result.insert(INSERT, "\nMemory Usage : " + str(eeccmu[1]) + " kb")
                    self.data_textarea_result.insert(INSERT, "\nSecurity Level : " + str(eeccslevel) + " %")
                    self.data_textarea_result.insert(INSERT, "\nAttack Level : " + str(eeccalevel) + " %")

                    print("\nProposed Elliptic CryptGenRandom Curve Cryptography (E-CGR-CC) Algorithm")
                    print("--------------------------------------------------------------------------")
                    self.data_textarea_result.insert(INSERT, "\n\nProposed Elliptic CryptGenRandom Curve Cryptography (E-CGR-CC) Algorithm")
                    self.data_textarea_result.insert(INSERT, "\n--------------------------------------------------------------------------")
                    tracemalloc.start()
                    stime = int(time.time() * 1000)
                    pecckey = Proposed_ECGRCC.key_load(self, "..\\Keys\\"+str(cfg.pid)+"\\ProposedECGRCCKey.key")
                    peccslevel, peccalevel = Proposed_ECGRCC.file_encrypt(self, pecckey, self.ehr_file.name, "..\\CloudServer\\"+str(cfg.pid)+"\\"+str(did[0])+"\\ProposedECGRCC\\"+basename)
                    etime = int(time.time() * 1000)
                    pecctime = etime - stime
                    peccmu = tracemalloc.get_traced_memory()
                    print("Encryption Time : "+str(pecctime)+" ms")
                    print("Memory Usage : " + str(peccmu[1]) + " kb")
                    print("Security Level : " + str(peccslevel) + " %")
                    print("Attack Level : " + str(peccalevel) + " %")
                    self.data_textarea_result.insert(INSERT, "\nEncryption Time : "+str(pecctime)+" ms")
                    self.data_textarea_result.insert(INSERT, "\nMemory Usage : " + str(peccmu[1]) + " kb")
                    self.data_textarea_result.insert(INSERT, "\nSecurity Level : " + str(peccslevel) + " %")
                    self.data_textarea_result.insert(INSERT, "\nAttack Level : " + str(peccalevel) + " %")

                    con = sqlite3.connect("..\\db\\user_datas.db")
                    cursorObj = con.cursor()
                    cursorObj.execute('CREATE TABLE IF NOT EXISTS blockchain (hashcode text, timestamp text, phashcode text, nounce text)')
                    tdate = datetime.datetime.now().strftime("%d-%m-%Y")
                    dockey = Proposed_ECGRCC.key_load(self, "..\\Keys\\" + str(did[0]) + "\\ProposedECGRCCKey.key")
                    strctext = str(cfg.pid) + str(pecckey) + str(did[0])+ str(dockey)

                    stime = int(time.time() * 1000)
                    strhcode= blake2b(strctext.encode('utf-8')).hexdigest()
                    strphcode = blake2b(strctext.encode('utf-8')).hexdigest()
                    time.sleep(0.3)
                    nounce = random.random()
                    idata = cursorObj.execute('INSERT INTO blockchain(hashcode, timestamp, phashcode, nounce) VALUES(?,?,?,?)', (strhcode, str(tdate), strphcode, nounce))
                    con.commit()
                    con.close()
                    etime = int(time.time() * 1000)

                    print("\nSelected EHR file was encrypted successfully...")
                    self.data_textarea_result.insert(INSERT, "\n\nSelected EHR file was encrypted successfully...")
                    messagebox.showinfo("Info Message", "Selected EHR file was encrypted successfully...")

                    self.data_textarea_result.configure(state="disabled")
                    self.btn_secure_upload.configure(state="disabled")
                    self.option_menu_dname.configure(state="disabled")
                else:
                    messagebox.showinfo("Info Message", "Please select the doctor name...")
            else:
                messagebox.showinfo("Info Message", "Please select the specialization...")
        else:
            messagebox.showinfo("Info Message", "Please select the EHR file to securely upload...")

def getDoctorPublicKey(did):
    dpk = ""
    con = sqlite3.connect("..\\db\\user_datas.db")
    cursorObj = con.cursor()
    cursorObj.execute("select * from doctor_detail_form where doctor_id='" + str(did) +"'")
    result = cursorObj.fetchall()
    for row in result:
        dpk = row[18]
    return dpk

def getPatientPublicKey(pid):
    ppk=""
    con = sqlite3.connect("..\\db\\user_datas.db")
    cursorObj = con.cursor()
    cursorObj.execute("select * from patient_detail_form where patient_id='" + str(pid) + "'")
    result = cursorObj.fetchall()
    for row in result:
        ppk = row[17]
    return ppk

def getListOfFiles(dirName):
    # create a list of file and sub directories names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

root = Tk()
root.title("Patient GUI")
root.geometry('1000x700')
root.resizable(0, 0)
root.configure(bg='azure3')
od = Patient_GUI(root)
root.mainloop()
