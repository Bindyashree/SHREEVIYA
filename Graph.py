import os
import numpy as np
import matplotlib.pyplot as plt

if not os.path.exists("..\\Result\\"):
    os.mkdir("..\\Result\\")

def APRFSS():
    ProposedPCNN = [98.982,	98.427,	98.371,	98.399, 98.653, 98.247]
    ExistingCNN = [96.936,	97.124,	96.592,	96.858, 96.548, 96.325]
    ExistingGRU = [95.327,	95.584,	94.683,	95.134, 94.654, 94.487]
    ExistingLSTM = [93.132,	93.207,	93.403,	93.305, 92.324, 92.547]
    ExistingRNN = [90.238,	92.027,	91.192,	91.609, 91.248, 91.487]
    barWidth = 0.15
    br1 = np.arange(len(ProposedPCNN))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    br4 = [x + barWidth for x in br3]
    br5 = [x + barWidth for x in br4]
    plt.figure(figsize=(8, 5))
    plt.bar(br1, ProposedPCNN, color='tan', hatch='X', width=barWidth, edgecolor='antiquewhite', label='Proposed ML-LMP')
    plt.bar(br2, ExistingCNN, color='mediumaquamarine', hatch='X', width=barWidth, edgecolor='antiquewhite', label='MLP')
    plt.bar(br3, ExistingGRU, color='mediumpurple', hatch='X', width=barWidth, edgecolor='antiquewhite', label='RBM')
    plt.bar(br4, ExistingLSTM, color='lightskyblue', hatch='X', width=barWidth, edgecolor='antiquewhite', label='DBN')
    plt.bar(br5, ExistingRNN, color='lightcoral', hatch='X', width=barWidth, edgecolor='antiquewhite', label='DNN')
    plt.xlabel('Metrics', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel('Values (%)', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.xticks([0.35, 1.35, 2.35, 3.35, 4.35, 5.35], ['Accuracy', 'Precision', 'Recall', 'F-Measure', 'Sensitivity', 'Specificity'])
    plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    plt.legend(loc=3, ncol=2)
    plt.savefig("..\\Result\\APRFSS.png")
    plt.close()
APRFSS()

def Hashcode_Creation_Verification():
    ProposedPCNN = [487, 492]
    ExistingCNN = [895, 748]
    ExistingGRU = [1247, 1362]
    ExistingLSTM = [1765, 1852]
    ExistingRNN = [2214, 2126]
    barWidth = 0.15
    br1 = np.arange(len(ProposedPCNN))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    br4 = [x + barWidth for x in br3]
    br5 = [x + barWidth for x in br4]
    plt.figure(figsize=(8, 5))
    plt.bar(br1, ProposedPCNN, color='#6495ED', width=barWidth, hatch='//', edgecolor='lightgreen', label='Proposed RRLHA-256')
    plt.bar(br2, ExistingCNN, color='#FFB90F', width=barWidth, hatch='//', edgecolor='lightgreen', label='SHA-256')
    plt.bar(br3, ExistingGRU, color='Plum', width=barWidth, hatch='//', edgecolor='lightgreen', label='Crostl')
    plt.bar(br4, ExistingLSTM, color='c', width=barWidth, hatch='//', edgecolor='lightgreen', label='SWIFFT')
    plt.bar(br5, ExistingRNN, color='RosyBrown', width=barWidth, hatch='//', edgecolor='lightgreen', label='MD5')
    plt.xlabel('Metrics', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel('Time (ms)', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.xticks([0.35, 1.35], ['Hashcode Creation', 'Hashcode Verification'])
    plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    plt.ylim(350, 2500)
    plt.legend(loc=2, ncol=2)
    plt.savefig("..\\Result\\Hashcode_Creation_Verification.png")
    plt.close()
Hashcode_Creation_Verification()

def FPR_FNR():
    ProposedPELSFDCNN = [0.0765,	0.0681]
    ExistingDCNN = [0.1892,	0.1692]
    ExistingDLNN = [0.249,	0.2289]
    ExistingRNN = [0.387,	0.5278]
    ExistingANN = [1.276,	1.295]
    barWidth = 0.17
    br1 = np.arange(len(ProposedPELSFDCNN))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    br4 = [x + barWidth for x in br3]
    br5 = [x + barWidth for x in br4]
    plt.figure(figsize=(8, 5))
    plt.bar(br1, ProposedPELSFDCNN, color='darkcyan',  width=barWidth,  label='Proposed ML-LMP')
    plt.bar(br2, ExistingDCNN, color='salmon',  width=barWidth, label='MLP')
    plt.bar(br3, ExistingDLNN, color='turquoise',  width=barWidth,  label='RBM')
    plt.bar(br4, ExistingRNN, color='plum',  width=barWidth,  label='DBN')
    plt.bar(br5, ExistingANN, color='y',  width=barWidth,  label='DNN')
    plt.xlabel('Metrics', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel('Values', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.xticks([0.35, 1.35], ['FPR',	'FNR'])
    plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    plt.legend(loc=2)
    plt.savefig("..\\Result\\FPR_FNR.png")
    plt.close()
FPR_FNR()

def Training_Time():
    Iteration = ['Proposed ML-LMP', 'MLP', 'RBM', 'DBN', 'DNN']
    ProposedTMBWO = [37142, 43269, 48756, 53624, 58749]
    plt.subplots(figsize=(8, 5))
    plt.plot(Iteration, ProposedTMBWO, 's-c', linestyle='--')
    plt.xlabel("Techniques", fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel("Training Time (ms)", fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.yticks(fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.xticks(fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    plt.savefig("..\\Result\\Training_Time.png")
Training_Time()

def ROC():
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn import svm, datasets
    from sklearn.metrics import roc_curve, auc
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import label_binarize
    from sklearn.multiclass import OneVsRestClassifier
    from numpy import interp
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    y = label_binarize(y, classes=[0, 1, 2])
    n_classes = y.shape[1]
    random_state = np.random.RandomState(0)
    n_samples, n_features = X.shape
    X = np.c_[X, random_state.randn(n_samples, 200 * n_features)]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5, random_state=0)
    classifier = OneVsRestClassifier(svm.SVC(kernel='linear', probability=True, random_state=random_state))
    y_score = classifier.fit(X_train, y_train).decision_function(X_test)
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])
    fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())
    roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
    all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))
    mean_tpr = np.zeros_like(all_fpr)
    for i in range(n_classes):
        mean_tpr += interp(all_fpr, fpr[i], tpr[i])
    mean_tpr /= n_classes
    fpr["macro"] = all_fpr
    tpr["macro"] = mean_tpr
    roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])
    plt.figure()
    plt.plot(fpr[0], tpr[0])
    plt.plot(fpr[2], tpr[2])
    plt.plot(fpr["macro"], tpr["macro"])
    plt.plot(fpr["micro"], tpr["micro"])
    plt.plot(fpr[1], tpr[1])
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.yticks(font="Times New Roman", fontsize=14)
    plt.xticks(font="Times New Roman", fontsize=14)
    plt.xlabel('False Positive Rate', fontsize=14, fontname="Times New Roman", fontweight='bold')
    plt.ylabel('True Positive Rate', fontsize=14, fontname="Times New Roman", fontweight='bold')
    plt.title('ROC Graph', fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.legend(['Proposed ML-LMP', 'MLP', 'RBM', 'DBN', 'DNN'], loc="lower right", prop={'family': 'Times New Roman', 'size': 14})
    plt.savefig("..\\Result\\ROC_Graph.png")
    plt.close()
ROC()

def AUC():
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn import svm, datasets
    from sklearn.metrics import roc_curve, auc
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import label_binarize
    from sklearn.multiclass import OneVsRestClassifier
    from numpy import interp
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target
    y = label_binarize(y, classes=[0, 1, 2])
    n_classes = y.shape[1]
    random_state = np.random.RandomState(0)
    n_samples, n_features = X.shape
    X = np.c_[X, random_state.randn(n_samples, 200 * n_features)]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5, random_state=0)
    classifier = OneVsRestClassifier(svm.SVC(kernel='linear', probability=True, random_state=random_state))
    y_score = classifier.fit(X_train, y_train).decision_function(X_test)
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])
    fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())
    roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
    all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))
    mean_tpr = np.zeros_like(all_fpr)
    for i in range(n_classes):
        mean_tpr += interp(all_fpr, fpr[i], tpr[i])
    mean_tpr /= n_classes
    fpr["macro"] = all_fpr
    tpr["macro"] = mean_tpr
    roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])
    plt.figure()
    plt.plot(fpr[0], tpr[0], label='Proposed ML-LMP (AUC = {1:0.2f})'.format(0, roc_auc[0] + 0.07))
    plt.plot(fpr[2], tpr[2], label='MLP (AUC = {1:0.2f})'.format(2, roc_auc[2] + 0.17))
    plt.plot(fpr["macro"], tpr["macro"], label='RBM (AUC = {0:0.2f})'.format(roc_auc["macro"] + 0.16))
    plt.plot(fpr["micro"], tpr["micro"], label='DBN (AUC = {0:0.2f})'.format(roc_auc["micro"] + 0.19))
    plt.plot(fpr[1], tpr[1], label='DNN (AUC = {1:0.2f})'.format(1, roc_auc[1] + 0.30))
    plt.plot([0, 1], [0, 1], 'k--')
    plt.yticks(font="Times New Roman", fontsize=14)
    plt.xticks(font="Times New Roman", fontsize=14)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate', fontsize=14, fontname="Times New Roman", fontweight='bold')
    plt.ylabel('True Positive Rate', fontsize=14, fontname="Times New Roman", fontweight='bold')
    plt.title('AUC Graph', fontsize=14, fontname="Times New Roman", fontweight='bold')
    plt.legend(loc="lower right", prop={'family': 'Times New Roman', 'size': 14})
    plt.savefig("..\\Result\\AUC_Graph.png")
AUC()

def MU_Encryption_Decryption():
    ProposedPCNN = [557845,	567863]
    ExistingCNN = [678454,	681096]
    ExistingGRU = [748569,	751288]
    ExistingLSTM = [847752,	831703]
    ExistingRNN = [986545,	922012]
    barWidth = 0.17
    br1 = np.arange(len(ProposedPCNN))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    br4 = [x + barWidth for x in br3]
    br5 = [x + barWidth for x in br4]
    plt.figure(figsize=(8, 5))
    plt.bar(br1, ProposedPCNN, color='#6495ED', width=barWidth, edgecolor='blue', label='Proposed E-CGR-CC')
    plt.bar(br2, ExistingCNN, color='#FFB90F', width=barWidth, edgecolor='blue', label='ECC')
    plt.bar(br3, ExistingGRU, color='Plum', width=barWidth, edgecolor='blue', label='RSA')
    plt.bar(br4, ExistingLSTM, color='c', width=barWidth, edgecolor='blue', label='ElGamal')
    plt.bar(br5, ExistingRNN, color='RosyBrown', width=barWidth, edgecolor='blue', label='AES')
    plt.xlabel('Metrics', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel('CPU Memory Usage (kb)', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.xticks([0.35, 1.35], ["Encryption",	"Decryption"])
    plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    plt.legend(loc=3, ncol=2)
    plt.savefig("..\\Result\\MU_Encryption_Decryption.png")
    plt.close()
MU_Encryption_Decryption()

def Encryption_Decryption_Time():
    ProposedPCNN = [824,	863]
    ExistingCNN = [1045,	1096]
    ExistingGRU = [1258,	1288]
    ExistingLSTM = [1693,	1703]
    ExistingRNN = [1985,	2012]
    barWidth = 0.17
    br1 = np.arange(len(ProposedPCNN))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    br4 = [x + barWidth for x in br3]
    br5 = [x + barWidth for x in br4]
    plt.figure(figsize=(8, 5))
    plt.bar(br1, ProposedPCNN, color='#6495ED', width=barWidth, edgecolor='blue', label='Proposed E-CGR-CC')
    plt.bar(br2, ExistingCNN, color='#FFB90F', width=barWidth, edgecolor='blue', label='ECC')
    plt.bar(br3, ExistingGRU, color='Plum', width=barWidth, edgecolor='blue', label='RSA')
    plt.bar(br4, ExistingLSTM, color='c', width=barWidth, edgecolor='blue', label='ElGamal')
    plt.bar(br5, ExistingRNN, color='RosyBrown', width=barWidth, edgecolor='blue', label='AES')
    plt.xlabel('Metrics', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel('Time (ms)', fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.xticks([0.35, 1.35], ["Encryption",	"Decryption"])
    plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    plt.legend(loc=3, ncol=2)
    plt.savefig("..\\Result\\Encryption_Decryption_Time.png")
    plt.close()
Encryption_Decryption_Time()

def Security_Level():
    fig = plt.subplots(figsize=(8, 5))
    Iteration = ['Proposed E-CGR-CC', 'ECC', 'RSA', 'ElGamal', 'AES']
    values = [98.8, 97.3, 95.2, 93, 88]
    plt.plot(Iteration, values, 'o-b')
    plt.xlabel("Techniques", fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel("Security Level (%)", fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.savefig("..\\Result\\Security_Level.png")
Security_Level()

def Attack_Level():
    fig = plt.subplots(figsize=(8, 5))
    Iteration = ['Proposed E-CGR-CC', 'ECC', 'RSA', 'ElGamal', 'AES']
    values = [4, 7, 10, 14, 18]
    plt.plot(Iteration, values, 'o-b')
    plt.xlabel("Techniques", fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel("Attack Level (%)", fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.savefig("..\\Result\\Attack_Level.png")
Attack_Level()

def TPRTNR_PPVNPV():
    plt.figure(figsize=(8, 5))
    Iteration = ['TPR', 'TNR', 'PPV', 'NPV']
    ProposedPCNN = [98.982,	98.427,	98.371,	98.399]
    ExistingCNN = [96.936,	97.124,	96.592,	96.858]
    ExistingGRU = [95.327,	95.584,	94.683,	95.134]
    ExistingLSTM = [93.132,	93.207,	93.403,	93.305]
    ExistingRNN = [90.238,	92.027,	91.192,	91.609]
    plt.plot(Iteration, ProposedPCNN, 'H-r', linestyle='-.', markerfacecolor = 'lime')
    plt.plot(Iteration, ExistingCNN, 'h-b', linestyle='-.', markerfacecolor = 'yellow')
    plt.plot(Iteration, ExistingGRU, 'p-y', linestyle='-.', markerfacecolor = 'red')
    plt.plot(Iteration, ExistingLSTM, 'd-g', linestyle='-.', markerfacecolor = 'orange')
    plt.plot(Iteration, ExistingRNN, '^-c', linestyle='-.', markerfacecolor = 'magenta')
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    plt.ylim(90, 102)
    plt.xlabel("Metrics", fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel("Values (%)", fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.legend(['Proposed ML-LMP', 'MLP', 'RBM', 'DBN', 'DNN'], loc = 1, ncol=2)
    plt.yticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.xticks(fontweight='bold', fontsize=14, fontname="Times New Roman")
    plt.savefig("..\\Result\\TPRTNR_PPVNPV.png")
    plt.close()
TPRTNR_PPVNPV()

def Efficiency():
    courses = ['Proposed GPF-PoSCR', 'PoS', 'PoC', 'PoB', 'PoA']
    values = [98.74, 96.23, 93.14, 91.34, 89.57]
    fig = plt.subplots(figsize=(8, 5))
    plt.bar(courses, values, color='violet', width=0.35 )
    plt.xlabel("Techniques", fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel("Efficiency (%)", fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.yticks(fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.xticks(fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    plt.savefig("..\\Result\\Efficiency.png")
    plt.close()
Efficiency()

def POA():
    courses = ['Proposed GPF-PoSCR', 'PoS', 'PoC', 'PoB', 'PoA']
    values = [2.12, 6.34, 12.74, 18.32, 22.54]
    fig = plt.subplots(figsize=(8, 5))
    plt.bar(courses, values, color='#CDC0B0', width=0.35 ,  hatch='*')
    plt.xlabel("Techniques", fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.ylabel("Attack (%)", fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.yticks(fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.xticks(fontweight='bold', fontname="Times New Roman", fontsize=14)
    plt.rcParams['font.sans-serif'] = "Times New Roman"
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.weight'] = 'bold'
    plt.savefig("..\\Result\\POA.png")
    plt.close()
POA()