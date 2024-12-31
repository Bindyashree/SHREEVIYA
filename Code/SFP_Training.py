import os
import time
import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import messagebox
import csv

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

from EHR.SystemFailurePrediction.Existing_DNN import Existing_DNN
from EHR.SystemFailurePrediction.Existing_DBN import Existing_DBN
from EHR.SystemFailurePrediction.Existing_RBM import Existing_RBM
from EHR.SystemFailurePrediction.Existing_MLP import Existing_MLP
from EHR.SystemFailurePrediction.Proposed_MLLMP import Proposed_MLLMP

from EHR import config as cfg

class SFP_Training:

    boolDatasetRead = False
    boolDataDeDup = False
    boolNumeralization = False
    boolNormalization = False
    boolFeatureExtraction = False
    boolFeatureSelection = False
    boolDatasetSplitting = False
    boolTraining = False
    boolTesting = False

    ipdata = []
    ipdddata = []
    numipdata = []
    nomipdata = []
    cls = []

    trdata = []
    tsdata = []

    trcls = []
    tscls = []

    features = []

    trainingsize = 80
    testingsize = 20

    def __init__(self, root):
        self.LARGE_FONT = ("Algerian", 16)
        self.text_font = ("Constantia", 15)
        self.text_font1 = ("Constantia", 10)

        self.frame_font = ("", 9)
        self.frame_process_res_font = ("", 12)
        self.root = root
        self.feature_value = StringVar()

        label_heading = tkinter.Label(root, text="System Failure Prediction using Multi-Layer Lagrange Maxout Perceptrons (ML-LMPs)", fg="deep pink", bg="azure3", font=self.LARGE_FONT)
        label_heading.place(x=50, y=0)

        self.label_frame_system_failure_dataset = LabelFrame(root, text="System Failure Dataset", bg="azure3", fg="#00a800", font=self.frame_font)
        self.label_frame_system_failure_dataset.place(x=10, y=30, width=200, height=50)
        self.entry_ids_dataset = Entry(root, font=self.frame_font)
        self.entry_ids_dataset.place(x=20, y=50, width=100, height=25)
        self.entry_ids_dataset.insert(INSERT, "..\\\\Dataset\\\\")
        self.entry_ids_dataset.configure(state="disabled")
        self.btn_read_dataset = Button(root, text="Read", bg="deep sky blue", fg="#fff", font=self.text_font1, width=7,  command=self.read_dataset)
        self.btn_read_dataset.place(x=130, y=50)

        self.label_frame_preprocessing = LabelFrame(root, text="Pre-Processing", bg="azure3", fg="#00a800", font=self.frame_font)
        self.label_frame_preprocessing.place(x=220, y=30, width=310, height=50)
        self.btn_preprocessing_datadedup = Button(root, text="Data DeDup", bg="deep sky blue", fg="#fff", font=self.text_font1, width=10, command = self.preprocessing_datadedup)
        self.btn_preprocessing_datadedup.place(x=230, y=50)
        self.btn_preprocessing_numeralization = Button(root, text="Numeralization", bg="deep sky blue", fg="#fff", font=self.text_font1, width=10, command = self.preprocessing_numeralization)
        self.btn_preprocessing_numeralization.place(x=330, y=50)
        self.btn_preprocessing_normalization = Button(root, text="Normalization", bg="deep sky blue", fg="#fff", font=self.text_font1, width=10, command = self.preprocessing_normalization)
        self.btn_preprocessing_normalization.place(x=430, y=50)

        self.label_frame_feature_extraction = LabelFrame(root, text="Feature Extraction", bg="azure3", fg="#00a800", font=self.frame_font)
        self.label_frame_feature_extraction.place(x=540, y=30, width=110, height=50)
        self.btn_feature_extraction = Button(root, text="Proceed", bg="deep sky blue", fg="#fff", font=self.text_font1, width=10, command = self.feature_extraction)
        self.btn_feature_extraction.place(x=550, y=50)

        self.label_frame_dataset_splitting = LabelFrame(root, text="Dataset Splitting", bg="azure3", fg="#00a800", font=self.frame_font)
        self.label_frame_dataset_splitting.place(x=660, y=30, width=110, height=50)
        self.btn_dataset_splitting = Button(root, text="Proceed", bg="deep sky blue", fg="#fff", font=self.text_font1, width=10, command = self.dataset_splitting)
        self.btn_dataset_splitting.place(x=670, y=50)

        self.label_frame_classification = LabelFrame(root, text="System Failure Prediction", bg="azure3", fg="#00a800", font=self.frame_font)
        self.label_frame_classification.place(x=800, y=30, width=160, height=50)
        self.btn_training = Button(root, text="Training", bg="deep sky blue", fg="#fff", font=self.text_font1, width=6, command=self.training)
        self.btn_training.place(x=810, y=50)
        self.btn_testing = Button(root, text="Testing", bg="deep sky blue", fg="#fff", font=self.text_font1, width=6, command=self.testing)
        self.btn_testing.place(x=880, y=50)

        self.label_graph_generation = LabelFrame(root, text="Graph Generation", bg="azure3", font=self.frame_font)
        self.label_graph_generation.place(x=1000, y=30, width=110, height=50)
        self.btn_graph_generation = Button(root, text="Proceed", bg="deep sky blue", fg="#fff", width=11, command=self.graph_generation)
        self.btn_graph_generation.place(x=1010, y=50)

        self.btn_exit = Button(root, text="Exit", bg="deep sky blue", fg="#fff", width=3,command=self.exit)
        self.btn_exit.place(x=1130, y=50)

        # Horizontal (x) Scroll bar
        self.xscrollbar = Scrollbar(root, orient=HORIZONTAL)
        self.xscrollbar.pack(side=BOTTOM, fill=X)
        # Vertical (y) Scroll Bar
        self.yscrollbar = Scrollbar(root)
        self.yscrollbar.pack(side=RIGHT, fill=Y)

        self.label_output_frame = LabelFrame(root, text="Process Window", bg="azure3", fg="#0000FF", font=self.frame_process_res_font)
        self.label_output_frame.place(x=10, y=80, width=650, height=500)
        # Text Widget
        self.data_textarea_process = Text(root, wrap=WORD, xscrollcommand=self.xscrollbar.set, yscrollcommand=self.yscrollbar.set)
        self.data_textarea_process.pack()
        # Configure the scrollbars
        self.xscrollbar.config(command=self.data_textarea_process.xview)
        self.yscrollbar.config(command=self.data_textarea_process.yview)
        self.data_textarea_process.place(x=20, y=100, width=630, height=470)
        self.data_textarea_process.configure(state="disabled")

        self.label_output_frame = LabelFrame(root, text="Result Window", bg="azure3", fg="#0000FF", font=self.frame_process_res_font)
        self.label_output_frame.place(x=670, y=80, width=500, height=500)
        # Text Widget
        self.data_textarea_result = Text(root, wrap=WORD, xscrollcommand=self.xscrollbar.set, yscrollcommand=self.yscrollbar.set)
        self.data_textarea_result.pack()
        # Configure the scrollbars
        self.xscrollbar.config(command=self.data_textarea_result.xview)
        self.yscrollbar.config(command=self.data_textarea_result.yview)
        self.data_textarea_result.place(x=680, y=100, width=480, height=470)
        self.data_textarea_result.configure(state="disabled")

    def read_dataset(self):
        self.boolDatasetRead = True
        self.data_textarea_process.configure(state="normal")

        with open("..\\Dataset\\DEPL\\LCS_with_VMM.tsv", "r", encoding='utf-8') as f1:
            csvreader = csv.reader(f1)
            count = 0
            for row in csvreader:
                val = str(row).replace("[", "").replace("]", "").replace("'", "").replace("\\t", " ")
                if count == 0:
                    a = str(val).split(" ")
                    for x in range(len(a)):
                        if not self.features.__contains__(a[x]):
                            self.features.append(a[x])
                else:
                    self.ipdata.append(val)
                count = count + 1

        with open("..\\Dataset\\NET\\LCS_with_VMM.tsv", "r", encoding='utf-8') as f1:
            csvreader = csv.reader(f1)
            count = 0
            for row in csvreader:
                val = str(row).replace("[", "").replace("]", "").replace("'", "").replace("\\t", " ")
                if count == 0:
                    a = str(val).split(" ")
                    for x in range(len(a)):
                        if not self.features.__contains__(a[x]):
                            self.features.append(a[x])
                else:
                    self.ipdata.append(val)
                count = count + 1

        with open("..\\Dataset\\STO\\LCS_with_VMM.tsv", "r", encoding='utf-8') as f1:
            csvreader = csv.reader(f1)
            count = 0
            for row in csvreader:
                val = str(row).replace("[", "").replace("]", "").replace("'", "").replace("\\t", " ")
                if count == 0:
                    a = str(val).split(" ")
                    for x in range(len(a)):
                        if not self.features.__contains__(a[x]):
                            self.features.append(a[x])
                else:
                    self.ipdata.append(val)
                count = count + 1

        with open("..\\Dataset\\DEPL\\Failure_Labels.txt", "r", encoding='utf-8') as f1:
            csvreader = csv.reader(f1)
            for row in csvreader:
                self.cls.append(int(str(row).replace("[", "").replace("]", "").replace("'", "")))

        with open("..\\Dataset\\NET\\Failure_Labels.txt", "r", encoding='utf-8') as f1:
            csvreader = csv.reader(f1)
            for row in csvreader:
                self.cls.append(int(str(row).replace("[", "").replace("]", "").replace("'", "")))

        with open("..\\Dataset\\STO\\Failure_Labels.txt", "r", encoding='utf-8') as f1:
            csvreader = csv.reader(f1)
            for row in csvreader:
                self.cls.append(int(str(row).replace("[", "").replace("]", "").replace("'", "")))

        print("System Failure Prediction Dataset")
        print("=================================")

        print("Total no. of Data : "+str(len(self.ipdata)))

        print("\nSystem Failure Data")
        print("---------------------")
        for x in range(10):
            print(self.ipdata[x])

        self.data_textarea_process.insert(INSERT, "System Failure Prediction Dataset")
        self.data_textarea_process.insert(INSERT, "\n===============================")
        self.data_textarea_process.insert(INSERT, "\nTotal no. of Data : "+str(len(self.ipdata)))

        print("\nSystem Failure Prediction Dataset was read successfully...")
        self.data_textarea_process.insert(INSERT, "\n\nSystem Failure Prediction Dataset was read successfully...")
        messagebox.showinfo("showinfo", "System Failure Prediction Dataset was read successfully...")

        self.btn_read_dataset.configure(state="disabled")
        self.data_textarea_process.configure(state="disabled")

    def preprocessing_datadedup(self):
        if self.boolDatasetRead:
            self.boolDataDeDup = True
            self.data_textarea_process.configure(state="normal")

            print("\nPre-processing")
            print("================")
            self.data_textarea_process.insert(INSERT, "\n\nPre-processing")
            self.data_textarea_process.insert(INSERT, "\n================")

            print("Data DeDuplication")
            print("------------------")
            self.data_textarea_process.insert(INSERT, "\nData DeDuplication")
            self.data_textarea_process.insert(INSERT, "\n------------------")

            print("Total no. of Data before Data DeDuplication : "+str(len(self.ipdata)))
            self.data_textarea_process.insert(INSERT, "\nTotal no. of Data before Data DeDuplication : "+str(len(self.ipdata)))

            temp = list(set(self.ipdata))

            for x in range(len(self.ipdata)):
                a = str(self.ipdata[x]).split(" ")
                tem = []
                for y in range(len(a)):
                    tem.append(str(a[y]).strip())

                self.ipdddata.append(tem)

            print("Total no. of Data after Data DeDuplication : "+str(len(self.ipdata)))
            self.data_textarea_process.insert(INSERT, "\nTotal no. of Data after Data DeDuplication : "+str(len(self.ipdddata)))

            print("\nData DeDuplication was done successfully...")
            self.data_textarea_process.insert(INSERT, "\n\nData DeDuplication was done successfully...")
            messagebox.showinfo("showinfo", "Data DeDuplication was done successfully...")

            self.btn_preprocessing_datadedup.configure(state="disabled")
            self.data_textarea_process.configure(state="disabled")
        else:
            messagebox.showinfo("showinfo", "Please read the System Failure Prediction Dataset first...")

    def preprocessing_numeralization(self):
        if self.boolDataDeDup:
            self.boolNumeralization = True
            self.data_textarea_process.configure(state="normal")
            print("\nNumeralization")
            print("----------------")
            self.data_textarea_process.insert(INSERT, "\n\nNumeralization")
            self.data_textarea_process.insert(INSERT, "\n----------------")

            for x in range(len(self.ipdddata)):
                temp = []
                for y in range(len(self.ipdddata[x])):
                    temp.append(float(str(self.ipdddata[x][y]).strip()))
                self.numipdata.append(temp)

            for x in range(10):
                print(self.numipdata[x])

            print("\nNumeralization was done successfully...")
            self.data_textarea_process.insert(INSERT, "\n\nNumeralization was done successfully...")
            messagebox.showinfo("showinfo", "Numeralization was done successfully...")

            self.btn_preprocessing_numeralization.configure(state="disabled")
            self.data_textarea_process.configure(state="disabled")
        else:
            messagebox.showinfo("showinfo", "Please done the Data DeDuplication first...")

    def preprocessing_normalization(self):
        if self.boolNumeralization:
            self.boolNormalization = True
            self.data_textarea_process.configure(state="normal")
            print("\nNormalization")
            print("----------------")
            self.data_textarea_process.insert(INSERT, "\n\nNormalization")
            self.data_textarea_process.insert(INSERT, "\n----------------")

            # Min Max Normalization
            # x ′ = (x − x m i n) / (x m a x − x m i n)
            sc = MinMaxScaler()

            X = pd.DataFrame(self.numipdata)

            Normalized = sc.fit_transform(X)

            self.nomipdata = Normalized.tolist()

            for x in range(10):
                print(self.nomipdata[x])

            print("\nNormalization was done successfully...")
            self.data_textarea_process.insert(INSERT, "\n\nNormalization was done successfully...")
            messagebox.showinfo("showinfo", "Normalization was done successfully...")

            self.btn_preprocessing_normalization.configure(state="disabled")
            self.data_textarea_process.configure(state="disabled")
        else:
            messagebox.showinfo("showinfo", "Please done the Numeralization first...")

    def feature_extraction(self):
        if self.boolNormalization:
            self.boolFeatureExtraction = True
            self.data_textarea_process.configure(state="normal")
            print("\nFeature Extraction")
            print("====================")
            self.data_textarea_process.insert(INSERT, "\n\nFeature Extraction")
            self.data_textarea_process.insert(INSERT, "\n====================")

            print("Total no. of Features : " + str(len(self.features)))
            self.data_textarea_process.insert(INSERT, "\nTotal no. of Features : " + str(len(self.features)))

            print("\nFeatures are...")
            print("-----------------")
            self.data_textarea_process.insert(INSERT, "\n\nFeatures are...")
            self.data_textarea_process.insert(INSERT, "\n-----------------")

            for x in range(len(self.features)):
                print(self.features[x])
                self.data_textarea_process.insert(INSERT, "\n" + str(self.features[x]))

            print("\nFeature Extraction was done successfully...")
            self.data_textarea_process.insert(INSERT, "\n\nFeature Extraction was done successfully...")
            messagebox.showinfo("showinfo", "Feature Extraction was done successfully...")

            self.btn_feature_extraction.configure(state="disabled")
            self.data_textarea_process.configure(state="disabled")
        else:
            messagebox.showinfo("showinfo", "Please done the Normalization first...")

    def dataset_splitting(self):
        if self.boolFeatureExtraction:
            self.boolDatasetSplitting = True
            self.data_textarea_process.configure(state="normal")
            print("\nDataset Splitting")
            print("======================")
            self.data_textarea_process.insert(INSERT, "\n\nDataset Splitting")
            self.data_textarea_process.insert(INSERT, "\n======================")

            trsize = (len(self.ipdata)*self.trainingsize)/100
            tssize = (len(self.ipdata)*self.trainingsize)/100

            for x in range(int(trsize)):
                self.trdata.append(self.ipdata[x])
                self.trcls.append(self.cls[x])

            i = int(trsize)

            while i < len(self.ipdata):
                self.tsdata.append(self.ipdata[i])
                self.tscls.append(self.cls[i])

                if i == len(self.ipdata):
                    break

                i = i + 1
            print("Total no. of Data : " + str(len(self.ipdata)))
            print("Total no. of Data for Training : " + str(len(self.trdata)))
            print("Total no. of Data for Testing : " + str(len(self.tsdata)))

            self.data_textarea_process.insert(INSERT, "\nTotal no. of Data : " + str(len(self.ipdata)))
            self.data_textarea_process.insert(INSERT, "\nTotal no. of Data for Training : " + str(len(self.trdata)))
            self.data_textarea_process.insert(INSERT, "\nTotal no. of Data for Testing : " + str(len(self.tsdata)))

            messagebox.showinfo("Info Message", "Dataset Splitting was done successfully...")
            print("\nDataset Splitting was done successfully...")
            self.data_textarea_process.insert(INSERT, "\n\nDataset Splitting was done successfully...")

            self.data_textarea_process.configure(state="disabled")
            self.btn_dataset_splitting.configure(state="disabled")
        else:
            messagebox.showinfo("showinfo", "Please done Feature Extraction first...")

    def training(self):
        if self.boolDatasetSplitting:
            self.data_textarea_process.configure(state="normal")
            self.data_textarea_result.configure(state="normal")
            self.data_textarea_process.insert(INSERT, "\n\nSystem Failure Prediction Training")
            self.data_textarea_process.insert(INSERT, "\n====================================")
            self.data_textarea_result.insert(INSERT, "\n\nSystem Failure Prediction Training")
            self.data_textarea_result.insert(INSERT, "\n====================================")
            print("\nSystem Failure Prediction Training")
            print("====================================")

            print("Existing Deep Neural Network (DNN) Algorithm")
            print("--------------------------------------------")
            self.data_textarea_process.insert(INSERT, "\nExisting Deep Neural Network (DNN) Algorithm")
            self.data_textarea_process.insert(INSERT, "\n--------------------------------------------")
            self.data_textarea_result.insert(INSERT, "\nExisting DNN")
            self.data_textarea_result.insert(INSERT, "\n------------")

            stime = int(time.time() * 1000)
            Existing_DNN.training(self, self.trdata, self.trcls)
            etime = int(time.time() * 1000)
            trtime = etime - stime
            print("Training Time : " + str(trtime) + " ms")
            self.data_textarea_result.insert(INSERT, "\nTraining Time : " + str(trtime) + " ms")

            print("\nExisting Deep Belief Network (DBN) Algorithm")
            print("----------------------------------------------")
            self.data_textarea_process.insert(INSERT, "\n\nExisting Deep Belief Network (DBN) Algorithm")
            self.data_textarea_process.insert(INSERT, "\n-----------------------------------------------")
            self.data_textarea_result.insert(INSERT, "\n\nExisting DBN")
            self.data_textarea_result.insert(INSERT, "\n---------------")

            stime = int(time.time() * 1000)
            Existing_DBN.training(self, self.trdata, self.trcls)
            etime = int(time.time() * 1000)
            trtime = etime - stime
            print("Training Time : " + str(trtime) + " ms")
            self.data_textarea_result.insert(INSERT, "\nTraining Time : " + str(trtime) + " ms")

            print("\nExisting Restricted Boltzmann Machine (RBM) Algorithm")
            print("-------------------------------------------------------")
            self.data_textarea_process.insert(INSERT, "\n\nExisting Restricted Boltzmann Machine (RBM) Algorithm")
            self.data_textarea_process.insert(INSERT, "\n-------------------------------------------------------")
            self.data_textarea_result.insert(INSERT, "\n\nExisting RBM Algorithm")
            self.data_textarea_result.insert(INSERT, "\n---------------------------")

            stime = int(time.time() * 1000)
            Existing_RBM.training(self, self.trdata, self.trcls)
            etime = int(time.time() * 1000)
            trtime = etime - stime
            print("Training Time : " + str(trtime) + " ms")
            self.data_textarea_result.insert(INSERT, "\nTraining Time : " + str(trtime) + " ms")

            print("\nExisting Multi-layer Perceptron (MLP) Algorithm")
            print("-------------------------------------------------")
            self.data_textarea_process.insert(INSERT, "\n\nExisting Multi-layer Perceptron (MLP) Algorithm")
            self.data_textarea_process.insert(INSERT, "\n-------------------------------------------------")
            self.data_textarea_result.insert(INSERT, "\n\nExisting MLP Algorithm")
            self.data_textarea_result.insert(INSERT, "\n------------------------")

            stime = int(time.time() * 1000)
            Existing_MLP.training(self, self.trdata, self.trcls)
            etime = int(time.time() * 1000)
            trtime = etime - stime
            print("Training Time : " + str(trtime) + " ms")
            self.data_textarea_result.insert(INSERT, "\nTraining Time : " + str(trtime) + " ms")

            print("\nProposed Multi-Layer Lagrange Maxout Perceptrons (ML-LMP) Algorithm")
            print("---------------------------------------------------------------------")
            self.data_textarea_process.insert(INSERT, "\n\nProposed Multi-Layer Lagrange Maxout Perceptrons (ML-LMP) Algorithm")
            self.data_textarea_process.insert(INSERT, "\n---------------------------------------------------------------------")
            self.data_textarea_result.insert(INSERT, "\n\nProposed ML-LMP Algorithm")
            self.data_textarea_result.insert(INSERT, "\n---------------------------")

            stime = int(time.time() * 1000)
            Proposed_MLLMP.training(self, self.trdata, self.trcls)
            etime = int(time.time() * 1000)
            trtime = etime - stime
            print("Training Time : " + str(trtime) + " ms" + " ms")
            self.data_textarea_result.insert(INSERT, "\nTraining Time : " + str(trtime) + " ms")

            messagebox.showinfo("Info Message", "System Failure Prediction Training was done successfully...")
            print("\nSystem Failure Prediction Training was done successfully...")
            self.data_textarea_process.insert(INSERT, "\n\nSystem Failure Prediction Training was done successfully...")

            self.data_textarea_process.configure(state="disabled")
            self.btn_training.configure(state="disabled")
        else:
            messagebox.showinfo("showinfo", "Please done Dataset Splitting first...")

    def testing(self):
        if os.path.exists("..\\Models\\"):
            if not os.path.exists("..\\CM\\"):
                os.mkdir("..\\CM\\")
            self.data_textarea_process.configure(state="normal")
            self.data_textarea_result.configure(state="normal")
            self.data_textarea_process.insert(INSERT, "\n\nSystem Failure Prediction Testing")
            self.data_textarea_process.insert(INSERT, "\n===================================")
            self.data_textarea_result.insert(INSERT, "\n\nSystem Failure Prediction Testing")
            self.data_textarea_result.insert(INSERT, "\n===================================")
            print("\nSystem Failure Prediction Testing")
            print("===================================")

            print("Existing Deep Neural Network (DNN) Algorithm")
            print("--------------------------------------------")
            self.data_textarea_process.insert(INSERT, "\nExisting Deep Neural Network (DNN) Algorithm")
            self.data_textarea_process.insert(INSERT, "\n--------------------------------------------")
            self.data_textarea_result.insert(INSERT, "\nExisting DNN")
            self.data_textarea_result.insert(INSERT, "\n------------")
            Existing_DNN.testing(self, self.tsdata, self.tscls)

            print("Precision : " + str(cfg.ednnpre))
            print("Recall : " + str(cfg.ednnrec))
            print("F-Measure : " + str(cfg.ednnfsc))
            print("Accuracy : " + str(cfg.ednnacc))
            print("Sensitivity : " + str(cfg.ednnsens))
            print("Specificity : " + str(cfg.ednnspec))
            print("TPR : " + str(cfg.ednntpr))
            print("TNR : " + str(cfg.ednntnr))
            print("PPV : " + str(cfg.ednnppv))
            print("NPV : " + str(cfg.ednnnpv))
            print("FNR : " + str(cfg.ednnfnr))
            print("FPR : " + str(cfg.ednnfpr))

            self.data_textarea_result.insert(INSERT, "\nPrecision : " + str(cfg.ednnpre))
            self.data_textarea_result.insert(INSERT, "\nRecall : " + str(cfg.ednnrec))
            self.data_textarea_result.insert(INSERT, "\nF-Measure : " + str(cfg.ednnfsc))
            self.data_textarea_result.insert(INSERT, "\nAccuracy : " + str(cfg.ednnacc))
            self.data_textarea_result.insert(INSERT, "\nSensitivity : " + str(cfg.ednnsens))
            self.data_textarea_result.insert(INSERT, "\nSpecificity : " + str(cfg.ednnspec))
            self.data_textarea_result.insert(INSERT, "\nTPR : " + str(cfg.ednntpr))
            self.data_textarea_result.insert(INSERT, "\nTNR : " + str(cfg.ednntnr))
            self.data_textarea_result.insert(INSERT, "\nPPV : " + str(cfg.ednnppv))
            self.data_textarea_result.insert(INSERT, "\nNPV : " + str(cfg.ednnnpv))
            self.data_textarea_result.insert(INSERT, "\nFNR : " + str(cfg.ednnfnr))
            self.data_textarea_result.insert(INSERT, "\nFPR : " + str(cfg.ednnfpr))

            print("\nExisting Deep Belief Network (DBN) Algorithm")
            print("----------------------------------------------")
            self.data_textarea_process.insert(INSERT, "\n\nExisting Deep Belief Network (DBN) Algorithm")
            self.data_textarea_process.insert(INSERT, "\n-----------------------------------------------")
            self.data_textarea_result.insert(INSERT, "\n\nExisting DBN")
            self.data_textarea_result.insert(INSERT, "\n---------------")
            Existing_DBN.testing(self, self.tsdata, self.tscls)

            print("Precision : " + str(cfg.edbnpre))
            print("Recall : " + str(cfg.edbnrec))
            print("F-Measure : " + str(cfg.edbnfsc))
            print("Accuracy : " + str(cfg.edbnacc))
            print("Sensitivity : " + str(cfg.edbnsens))
            print("Specificity : " + str(cfg.edbnspec))
            print("TPR : " + str(cfg.edbntpr))
            print("TNR : " + str(cfg.edbntnr))
            print("PPV : " + str(cfg.edbnppv))
            print("NPV : " + str(cfg.edbnnpv))
            print("FNR : " + str(cfg.edbnfnr))
            print("FPR : " + str(cfg.edbnfpr))

            self.data_textarea_result.insert(INSERT, "\nPrecision : " + str(cfg.edbnpre))
            self.data_textarea_result.insert(INSERT, "\nRecall : " + str(cfg.edbnrec))
            self.data_textarea_result.insert(INSERT, "\nF-Measure : " + str(cfg.edbnfsc))
            self.data_textarea_result.insert(INSERT, "\nAccuracy : " + str(cfg.edbnacc))
            self.data_textarea_result.insert(INSERT, "\nSensitivity : " + str(cfg.edbnsens))
            self.data_textarea_result.insert(INSERT, "\nSpecificity : " + str(cfg.edbnspec))
            self.data_textarea_result.insert(INSERT, "\nTPR : " + str(cfg.edbntpr))
            self.data_textarea_result.insert(INSERT, "\nTNR : " + str(cfg.edbntnr))
            self.data_textarea_result.insert(INSERT, "\nPPV : " + str(cfg.edbnppv))
            self.data_textarea_result.insert(INSERT, "\nNPV : " + str(cfg.edbnnpv))
            self.data_textarea_result.insert(INSERT, "\nFNR : " + str(cfg.edbnfnr))
            self.data_textarea_result.insert(INSERT, "\nFPR : " + str(cfg.edbnfpr))

            print("\nExisting Restricted Boltzmann Machine (RBM) Algorithm")
            print("-------------------------------------------------------")
            self.data_textarea_process.insert(INSERT, "\n\nExisting Restricted Boltzmann Machine (RBM) Algorithm")
            self.data_textarea_process.insert(INSERT, "\n-------------------------------------------------------")
            self.data_textarea_result.insert(INSERT, "\n\nExisting RBM Algorithm")
            self.data_textarea_result.insert(INSERT, "\n---------------------------")
            Existing_RBM.testing(self, self.tsdata, self.tscls)

            print("Precision : " + str(cfg.erbmpre))
            print("Recall : " + str(cfg.erbmrec))
            print("F-Measure : " + str(cfg.erbmfsc))
            print("Accuracy : " + str(cfg.erbmacc))
            print("Sensitivity : " + str(cfg.erbmsens))
            print("Specificity : " + str(cfg.erbmspec))
            print("TPR : " + str(cfg.erbmtpr))
            print("TNR : " + str(cfg.erbmtnr))
            print("PPV : " + str(cfg.erbmppv))
            print("NPV : " + str(cfg.erbmnpv))
            print("FNR : " + str(cfg.erbmfnr))
            print("FPR : " + str(cfg.erbmfpr))

            self.data_textarea_result.insert(INSERT, "\nPrecision : " + str(cfg.erbmpre))
            self.data_textarea_result.insert(INSERT, "\nRecall : " + str(cfg.erbmrec))
            self.data_textarea_result.insert(INSERT, "\nF-Measure : " + str(cfg.erbmfsc))
            self.data_textarea_result.insert(INSERT, "\nAccuracy : " + str(cfg.erbmacc))
            self.data_textarea_result.insert(INSERT, "\nSensitivity : " + str(cfg.erbmsens))
            self.data_textarea_result.insert(INSERT, "\nSpecificity : " + str(cfg.erbmspec))
            self.data_textarea_result.insert(INSERT, "\nTPR : " + str(cfg.erbmtpr))
            self.data_textarea_result.insert(INSERT, "\nTNR : " + str(cfg.erbmtnr))
            self.data_textarea_result.insert(INSERT, "\nPPV : " + str(cfg.erbmppv))
            self.data_textarea_result.insert(INSERT, "\nNPV : " + str(cfg.erbmnpv))
            self.data_textarea_result.insert(INSERT, "\nFNR : " + str(cfg.erbmfnr))
            self.data_textarea_result.insert(INSERT, "\nFPR : " + str(cfg.erbmfpr))

            print("\nExisting Multi-layer Perceptron (MLP) Algorithm")
            print("-------------------------------------------------")
            self.data_textarea_process.insert(INSERT, "\n\nExisting Multi-layer Perceptron (MLP) Algorithm")
            self.data_textarea_process.insert(INSERT, "\n-------------------------------------------------")
            self.data_textarea_result.insert(INSERT, "\n\nExisting MLP Algorithm")
            self.data_textarea_result.insert(INSERT, "\n------------------------")
            Existing_MLP.testing(self, self.tsdata, self.tscls)

            print("Precision : " + str(cfg.emlppre))
            print("Recall : " + str(cfg.emlprec))
            print("F-Measure : " + str(cfg.emlpfsc))
            print("Accuracy : " + str(cfg.emlpacc))
            print("Sensitivity : " + str(cfg.emlpsens))
            print("Specificity : " + str(cfg.emlpspec))
            print("TPR : " + str(cfg.emlptpr))
            print("TNR : " + str(cfg.emlptnr))
            print("PPV : " + str(cfg.emlpppv))
            print("NPV : " + str(cfg.emlpnpv))
            print("FNR : " + str(cfg.emlpfnr))
            print("FPR : " + str(cfg.emlpfpr))

            self.data_textarea_result.insert(INSERT, "\nPrecision : " + str(cfg.emlppre))
            self.data_textarea_result.insert(INSERT, "\nRecall : " + str(cfg.emlprec))
            self.data_textarea_result.insert(INSERT, "\nF-Measure : " + str(cfg.emlpfsc))
            self.data_textarea_result.insert(INSERT, "\nAccuracy : " + str(cfg.emlpacc))
            self.data_textarea_result.insert(INSERT, "\nSensitivity : " + str(cfg.emlpsens))
            self.data_textarea_result.insert(INSERT, "\nSpecificity : " + str(cfg.emlpspec))
            self.data_textarea_result.insert(INSERT, "\nTPR : " + str(cfg.emlptpr))
            self.data_textarea_result.insert(INSERT, "\nTNR : " + str(cfg.emlptnr))
            self.data_textarea_result.insert(INSERT, "\nPPV : " + str(cfg.emlpppv))
            self.data_textarea_result.insert(INSERT, "\nNPV : " + str(cfg.emlpnpv))
            self.data_textarea_result.insert(INSERT, "\nFNR : " + str(cfg.emlpfnr))
            self.data_textarea_result.insert(INSERT, "\nFPR : " + str(cfg.emlpfpr))

            print("\nProposed Multi-Layer Lagrange Maxout Perceptrons (ML-LMP) Algorithm")
            print("---------------------------------------------------------------------")
            self.data_textarea_process.insert(INSERT, "\n\nProposed Multi-Layer Lagrange Maxout Perceptrons (ML-LMP) Algorithm")
            self.data_textarea_process.insert(INSERT, "\n---------------------------------------------------------------------")
            self.data_textarea_result.insert(INSERT, "\n\nProposed ML-LMP Algorithm")
            self.data_textarea_result.insert(INSERT, "\n---------------------------")
            Proposed_MLLMP.testing(self, self.tsdata, self.tscls)

            print("Precision : " + str(cfg.pmllmppre))
            print("Recall : " + str(cfg.pmllmprec))
            print("F-Measure : " + str(cfg.pmllmpfsc))
            print("Accuracy : " + str(cfg.pmllmpacc))
            print("Sensitivity : " + str(cfg.pmllmpsens))
            print("Specificity : " + str(cfg.pmllmpspec))
            print("TPR : " + str(cfg.pmllmptpr))
            print("TNR : " + str(cfg.pmllmptnr))
            print("PPV : " + str(cfg.pmllmpppv))
            print("NPV : " + str(cfg.pmllmpnpv))
            print("FNR : " + str(cfg.pmllmpfnr))
            print("FPR : " + str(cfg.pmllmpfpr))

            self.data_textarea_result.insert(INSERT, "\nPrecision : " + str(cfg.pmllmppre))
            self.data_textarea_result.insert(INSERT, "\nRecall : " + str(cfg.pmllmprec))
            self.data_textarea_result.insert(INSERT, "\nF-Measure : " + str(cfg.pmllmpfsc))
            self.data_textarea_result.insert(INSERT, "\nAccuracy : " + str(cfg.pmllmpacc))
            self.data_textarea_result.insert(INSERT, "\nSensitivity : " + str(cfg.pmllmpsens))
            self.data_textarea_result.insert(INSERT, "\nSpecificity : " + str(cfg.pmllmpspec))
            self.data_textarea_result.insert(INSERT, "\nTPR : " + str(cfg.pmllmptpr))
            self.data_textarea_result.insert(INSERT, "\nTNR : " + str(cfg.pmllmptnr))
            self.data_textarea_result.insert(INSERT, "\nPPV : " + str(cfg.pmllmpppv))
            self.data_textarea_result.insert(INSERT, "\nNPV : " + str(cfg.pmllmpnpv))
            self.data_textarea_result.insert(INSERT, "\nFNR : " + str(cfg.pmllmpfnr))
            self.data_textarea_result.insert(INSERT, "\nFPR : " + str(cfg.pmllmpfpr))

            messagebox.showinfo("Info Message", "System Failure Prediction Testing was done successfully...")
            print("\nSystem Failure Prediction Testing was done successfully...")
            self.data_textarea_process.insert(INSERT, "\n\nSystem Failure Prediction Testing was done successfully...")

            self.data_textarea_process.configure(state="disabled")
            self.btn_testing.configure(state="disabled")
        else:
            messagebox.showinfo("showinfo", "Please done System Failure Prediction Training first...")

    def graph_generation(self):
        if not os.path.exists("..\\Result\\"):
            os.mkdir("..\\Result\\")

        from EHR.Code import Graph

        messagebox.showinfo("Info Message","Generate Tables and Graphs was done successfully...")

    def exit(self):
        self.root.destroy()

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

root = Tk()
root.title("SYSTEM FAILURE PREDICTION TRAINING")
root.geometry("1200x600")
root.resizable(0, 0)
root.configure(bg="azure3")
od = SFP_Training(root)
root.mainloop()
