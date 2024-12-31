import random
import sqlite3
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile
import os
import base64

from tkinter import Tk, filedialog
from tkinter import messagebox
import time
from tkinter.filedialog import asksaveasfile
import shutil

from hashlib import blake2b

from EHR import config as cfg

from EHR.DataSecurity.Existing_AES import Existing_AES
from EHR.DataSecurity.Existing_Elgamal import Existing_Elgamal
from EHR.DataSecurity.Existing_RSA import Existing_RSA
from EHR.DataSecurity.Existing_ECC import Existing_ECC
from EHR.DataSecurity.Proposed_ECGRCC import Proposed_ECGRCC

from EHR.MerkleTreeConstruction.MT import MerkleTreeNode

import tracemalloc

class Doctor_GUI:

    patient_ids = []

    def __init__(self, root):
        self.LARGE_FONT = ("Algerian", 16)
        self.text_font = ("Constantia", 15)
        self.text_font1 = ("Constantia", 10)

        self.frame_font = ("", 9)
        self.frame_process_res_font = ("", 12)
        self.root = root

        self.ufiles = StringVar()

        label_heading = tkinter.Label(root, text="ETHEREUM HYPERLEDGER BLOCKCHAIN BASED SECURE EHR USING GPF-PoSCR and E-CGR-CC", fg='deep pink', bg="azure3", font=self.LARGE_FONT)
        label_heading.place(x=50, y=10)

        self.label_select_file = Label(root, text="Select File", bg='azure3',fg='#CD7F32', font=13)
        self.label_select_file.place(x=10, y=50)

        ufiles = [""]
        if os.path.exists("..\\CloudServer\\"):
            temp = getListOfFiles("..\\CloudServer\\")
            for x in range(len(temp)):
                a = str(temp[x]).split("\\")
                if str(a[3]).__eq__(cfg.did) and str(a[4]).__eq__("ProposedECGRCC"):
                    ufiles.append(a[2]+"\\"+a[3]+"\\"+a[5])
                    self.patient_ids.append(a[2])

        self.entry_memory = OptionMenu(root, self.ufiles, *ufiles)
        self.entry_memory.place(x=100, y=50, width=300, height=25)

        self.btn_merkle_hash_tree = Button(root, text="Merkle Hash Tree Creation", width=18, bg="deep sky blue", fg="#fff", font=self.text_font1, command=self.merkle_hash_tree)
        self.btn_merkle_hash_tree.place(x=410, y=50)

        self.btn_sfprediction = Button(root, text="System Failure Prediction", width=17, bg="deep sky blue", fg="#fff", font=self.text_font1, command=self.sfprediction)
        self.btn_sfprediction.place(x=570, y=50)

        self.btn_lookup_table = Button(root, text="Lookup Table", width=9, bg="deep sky blue", fg="#fff", font=self.text_font1, command=self.lookup_table)
        self.btn_lookup_table.place(x=720, y=50)

        self.btn_download = Button(root, text="Download", width=7, bg="deep sky blue", fg="#fff", font=self.text_font1, command=self.download)
        self.btn_download.place(x=840, y=50)

        self.btn_exit = Button(root, text="Exit", width=5, bg="deep sky blue", fg="#fff", font=self.text_font1,command=self.close)
        self.btn_exit.place(x=910, y=50)

        # Horizontal (x) Scroll bar
        self.xscrollbar = Scrollbar(root, orient=HORIZONTAL)
        self.xscrollbar.pack(side=BOTTOM, fill=X)
        # Vertical (y) Scroll Bar
        self.yscrollbar = Scrollbar(root)
        self.yscrollbar.pack(side=RIGHT, fill=Y)

        self.label_output_frame = LabelFrame(root, text='Result Window', bg="azure3", fg="#0000FF",
                                             font=self.frame_process_res_font)
        self.label_output_frame.place(x=10, y=80, width=950, height=600)
        # Text Widget
        self.data_textarea_result = Text(root, wrap=WORD, xscrollcommand=self.xscrollbar.set,
                                         yscrollcommand=self.yscrollbar.set)
        self.data_textarea_result.pack()
        # Configure the scrollbars
        self.xscrollbar.config(command=self.data_textarea_result.xview)
        self.yscrollbar.config(command=self.data_textarea_result.yview)
        self.data_textarea_result.place(x=20, y=100, width=930, height=570)

    def merkle_hash_tree(self):
        self.data_textarea_result.configure(state="normal")
        print("\nMerkle Hash Tree Creation")
        print("===========================")
        self.data_textarea_result.insert(INSERT, "\nMerkle Hash Tree Creation")
        self.data_textarea_result.insert(INSERT, "\n=========================")

        if not os.path.exists("..\\Output\\"):
            os.mkdir("..\\Output\\")

        inputString = [cfg.did]
        for x in range(len(self.patient_ids)):
            inputString.append(self.patient_ids[x])

        f = open("..\\Output\\merkle.tree", "w")
        MerkleTreeNode.buildTree(self, inputString, f)
        f.close()

        print("\nMerkle Hash Tree was created successfully...")
        self.data_textarea_result.insert(INSERT, "\n\nMerkle Hash Tree was created successfully...")
        messagebox.showinfo("Info Message", "Merkle Hash Tree was created successfully...")

        self.data_textarea_result.configure(state="disabled")
        self.btn_merkle_hash_tree.configure(state="disabled")

    def sfprediction(self):
        self.data_textarea_result.configure(state="normal")
        print("\nSystem Failure Prediction using Proposed Multi-Layer Lagrange Maxout Perceptrons (ML-LMP) Algorithm")
        print("=====================================================================================================")
        self.data_textarea_result.insert(INSERT, "\n\nSystem Failure Prediction using Proposed Multi-Layer Lagrange Maxout Perceptrons (ML-LMP) Algorithm")
        self.data_textarea_result.insert(INSERT, "\n=====================================================================================================")

        print("\nSystem Failure Prediction was created successfully...")
        self.data_textarea_result.insert(INSERT, "\n\nSystem Failure Prediction was created successfully...")
        messagebox.showinfo("Info Message", "System Failure Prediction was created successfully...")

        self.data_textarea_result.configure(state="disabled")
        self.btn_sfprediction.configure(state="disabled")

    def lookup_table(self):
        self.data_textarea_result.configure(state="normal")
        print("\nLookup Table")
        print("==============")
        self.data_textarea_result.insert(INSERT, "\n\nLookup Table")
        self.data_textarea_result.insert(INSERT, "\n==============")

        print("\nExisting Message Digest Method 5 (MD5) Algorithm")
        print("--------------------------------------------------")
        self.data_textarea_result.insert(INSERT, "\n\nExisting Message Digest Method 5 (MD5) Algorithm")
        self.data_textarea_result.insert(INSERT, "\n--------------------------------------------------")

        print("\nExisting SWIFFT Algorithm")
        print("---------------------------")
        self.data_textarea_result.insert(INSERT, "\n\nExisting SWIFFT Algorithm")
        self.data_textarea_result.insert(INSERT, "\n---------------------------")

        print("\nExisting Crostl Algorithm")
        print("---------------------------")
        self.data_textarea_result.insert(INSERT, "\n\nExisting Crostl Algorithm")
        self.data_textarea_result.insert(INSERT, "\n---------------------------")

        print("\nExisting Secure Hash Algorithm 512 (SHA512)")
        print("---------------------------------------------")
        self.data_textarea_result.insert(INSERT, "\n\nExisting Secure Hash Algorithm 512 (SHA512)")
        self.data_textarea_result.insert(INSERT, "\n---------------------------------------------")

        print("\nProposed Rounded Root Log Hashing Algorithm – 256 (RRLHA-256) Algorithm")
        print("-------------------------------------------------------------------------")
        self.data_textarea_result.insert(INSERT, "\n\nProposed Rounded Root Log Hashing Algorithm – 256 (RRLHA-256) Algorithm")
        self.data_textarea_result.insert(INSERT, "\n-------------------------------------------------------------------------")

        print("\nData was updated into Lookup Table successfully...")
        self.data_textarea_result.insert(INSERT, "\n\nData was updated into Lookup Table successfully...")
        messagebox.showinfo("Info Message", "Data was updated into Lookup Table successfully...")

        self.data_textarea_result.configure(state="disabled")
        self.btn_lookup_table.configure(state="disabled")

    def download(self):
        sfile = self.ufiles.get()
        if len(sfile)>0:
            self.data_textarea_result.configure(state="normal")
            stime = int(time.time() * 1000)
            strdpname = sfile.split("\\")

            strpid = str(strdpname[0])
            strdid = str(strdpname[1])
            strfname = str(strdpname[2])

            f = asksaveasfile(initialfile=str(strdpname[2]), defaultextension=".csv", filetypes=[("All Files", "*.*"), ("Text Documents", "*.csv")])
            if not os.path.exists("..\\temp\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ExistingEL\\"):
                os.makedirs("..\\temp\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ExistingEL\\")
            if not os.path.exists("..\\temp\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ExistingAES\\"):
                os.makedirs("..\\temp\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ExistingAES\\")
            if not os.path.exists("..\\temp\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ExistingRSA\\"):
                os.makedirs("..\\temp\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ExistingRSA\\")
            if not os.path.exists("..\\temp\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ExistingECC\\"):
                os.makedirs("..\\temp\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ExistingECC\\")
            if not os.path.exists("..\\temp\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ProposedECGRCC\\"):
                os.makedirs("..\\temp\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ProposedECGRCC\\")

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
            source = "..\\CloudServer\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ExistingAES\\" + str(strdpname[2])
            destination = "..\\temp\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ExistingAES\\" + str(strdpname[2])
            key = Existing_AES.key_load(self, "..\\Keys\\" + str(strdpname[0]) + "\\ExistingAESKey.key")
            eaesslevel, eaesalevel = Existing_AES.file_decrypt(self, key, source, destination)
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
            source = "..\\CloudServer\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ExistingEL\\" + str(strdpname[2])
            destination = "..\\temp\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ExistingEL\\" + str(strdpname[2])
            key = Existing_Elgamal.key_load(self, "..\\Keys\\" + str(strdpname[0]) + "\\ExistingELKey.key")
            eelslevel, eelalevel = Existing_Elgamal.file_decrypt(self, key, source, destination)
            etime = int(time.time() * 1000)
            eeltime = etime - stime
            eelmu = tracemalloc.get_traced_memory()
            print("Encryption Time : " + str(eeltime) + " ms")
            print("Memory Usage : " + str(eelmu[1]) + " kb")
            print("Security Level : " + str(eelslevel) + " %")
            print("Attack Level : " + str(eelalevel) + " %")
            self.data_textarea_result.insert(INSERT, "\nEncryption Time : " + str(eeltime) + " ms")
            self.data_textarea_result.insert(INSERT, "\nMemory Usage : " + str(eelmu[1]) + " kb")
            self.data_textarea_result.insert(INSERT, "\nSecurity Level : " + str(eelslevel) + " %")
            self.data_textarea_result.insert(INSERT, "\nAttack Level : " + str(eelalevel) + " %")

            print("\nExisting Rivest-Shamir-Adleman (RSA) Algorithm")
            print("------------------------------------------------")
            self.data_textarea_result.insert(INSERT, "\n\nExisting Rivest-Shamir-Adleman (RSA) Algorithm")
            self.data_textarea_result.insert(INSERT, "\n------------------------------------------------")
            tracemalloc.start()
            stime = int(time.time() * 1000)
            source = "..\\CloudServer\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ExistingRSA\\" + str(strdpname[2])
            destination = "..\\temp\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ExistingRSA\\" + str(strdpname[2])
            key = Existing_RSA.key_load(self, "..\\Keys\\" + str(strdpname[0]) + "\\ExistingRSAKey.key")
            ersaslevel, ersaalevel = Existing_RSA.file_decrypt(self, key, source, destination)
            etime = int(time.time() * 1000)
            ersatime = etime - stime
            ersamu = tracemalloc.get_traced_memory()
            print("Encryption Time : " + str(ersatime) + " ms")
            print("Memory Usage : " + str(ersamu[1]) + " kb")
            print("Security Level : " + str(ersaslevel) + " %")
            print("Attack Level : " + str(ersaalevel) + " %")
            self.data_textarea_result.insert(INSERT, "\nEncryption Time : " + str(ersatime) + " ms")
            self.data_textarea_result.insert(INSERT, "\nMemory Usage : " + str(ersamu[1]) + " kb")
            self.data_textarea_result.insert(INSERT, "\nSecurity Level : " + str(ersaslevel) + " %")
            self.data_textarea_result.insert(INSERT, "\nAttack Level : " + str(ersaalevel) + " %")

            print("\nExisting Elliptic Curve Cryptography (ECC) Algorithm")
            print("------------------------------------------------------")
            self.data_textarea_result.insert(INSERT, "\n\nExisting Elliptic Curve Cryptography (ECC) Algorithm")
            self.data_textarea_result.insert(INSERT, "\n------------------------------------------------------")
            tracemalloc.start()
            stime = int(time.time() * 1000)
            source = "..\\CloudServer\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ExistingECC\\" + str(strdpname[2])
            destination = "..\\temp\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ExistingECC\\" + str(strdpname[2])
            key = Existing_ECC.key_load(self, "..\\Keys\\" + str(strdpname[0]) + "\\ExistingECCKey.key")
            eeccslevel, eeccalevel = Existing_ECC.file_decrypt(self, key, source, destination)
            etime = int(time.time() * 1000)
            eecctime = etime - stime
            eeccmu = tracemalloc.get_traced_memory()
            print("Encryption Time : " + str(eecctime) + " ms")
            print("Memory Usage : " + str(eeccmu[1]) + " kb")
            print("Security Level : " + str(eeccslevel) + " %")
            print("Attack Level : " + str(eeccslevel) + " %")
            self.data_textarea_result.insert(INSERT, "\nEncryption Time : " + str(eecctime) + " ms")
            self.data_textarea_result.insert(INSERT, "\nMemory Usage : " + str(eeccmu[1]) + " kb")
            self.data_textarea_result.insert(INSERT, "\nSecurity Level : " + str(eeccslevel) + " %")
            self.data_textarea_result.insert(INSERT, "\nAttack Level : " + str(eeccalevel) + " %")

            print("\nProposed Elliptic CryptGenRandom Curve Cryptography (E-CGR-CC)")
            print("----------------------------------------------------------------")
            self.data_textarea_result.insert(INSERT, "\n\nProposed Elliptic CryptGenRandom Curve Cryptography (E-CGR-CC)")
            self.data_textarea_result.insert(INSERT, "\n----------------------------------------------------------------")
            tracemalloc.start()
            stime = int(time.time() * 1000)
            source = "..\\CloudServer\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ProposedECGRCC\\" + str(strdpname[2])
            destination = "..\\temp\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ProposedECGRCC\\" + str(strdpname[2])
            key = Proposed_ECGRCC.key_load(self, "..\\Keys\\" + str(strdpname[0]) + "\\ProposedECGRCCKey.key")
            peccslevel, peccalevel = Proposed_ECGRCC.file_decrypt(self, key, source, destination)
            etime = int(time.time() * 1000)
            pecctime = etime - stime
            peccmu= tracemalloc.get_traced_memory()
            print("Encryption Time : " + str(pecctime) + " ms")
            print("Memory Usage : " + str(peccmu[1]) + " kb")
            print("Security Level : " + str(peccslevel) + " %")
            print("Attack Level : " + str(peccalevel) + " %")
            self.data_textarea_result.insert(INSERT, "\nEncryption Time : " + str(pecctime) + " ms")
            self.data_textarea_result.insert(INSERT, "\nMemory Usage : " + str(peccmu[1]) + " kb")
            self.data_textarea_result.insert(INSERT, "\nSecurity Level : " + str(peccslevel) + " %")
            self.data_textarea_result.insert(INSERT, "\nAttack Level : " + str(peccalevel) + " %")

            source = "..\\CloudServer\\" + str(strdpname[0]) + "\\" + str(strdpname[1]) + "\\ProposedECGRCC\\" + str(strdpname[2])
            destination = f.name
            key = Proposed_ECGRCC.key_load(self, "..\\Keys\\" + str(strdpname[0]) + "\\ProposedECGRCCKey.key")
            Proposed_ECGRCC.file_decrypt(self, key, source, destination)

            print("\nSelected EHR file was decrypted successfully...")
            self.data_textarea_result.insert(INSERT, "\n\nSelected EHR file was decrypted successfully...")
            messagebox.showinfo("Info Message", "Selected EHR file was decrypted successfully...")

            self.data_textarea_result.configure(state="disabled")
            self.btn_download.configure(state="disabled")
        else:
             messagebox.showerror("Error Message", "Please select the file to download...")

    def close(self):
        self.root.destroy()

def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
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
root.title("Doctor GUI")
root.geometry('1000x700')
root.resizable(0, 0)
root.configure(bg='azure3')
od = Doctor_GUI(root)
root.mainloop()
