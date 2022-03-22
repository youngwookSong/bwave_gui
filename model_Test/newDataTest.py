import numpy as np
import os
import pickle
from model_Test.BwaveData import BwaveData as bd
from model_Test.directory import ROOT_DIR
import matplotlib.pyplot as plt

class model_test:
    def __init__(self, file):
        self.file = file
        self.y_pred = None
        self.y_pred_proba = None

    def test(self):
        ## new data preprocess & feature extraction
        print(ROOT_DIR)
        file_path = self.file

        raw_file = bd()
        raw_file.load_file(file_path)
        raw_file.preprocess()
        raw_file.FC()
        result = raw_file.fc_f

        name = "fc"
        model_dir = os.path.join(ROOT_DIR, "model_{}_proba.pickle".format(name))
        with open(model_dir, 'rb') as f:
            clf = pickle.load(f)

        from sklearn import preprocessing
        scaler_dir = os.path.join(ROOT_DIR, "scaler.pickle")
        with open(scaler_dir, 'rb') as f:
            scaler = pickle.load(f)
        result = scaler.transform(result)

        fisher_dir = os.path.join(ROOT_DIR, "fis.npy")
        idx = np.load(fisher_dir)
        result = result[:, idx]


        if str(clf.predict(result)[0]) == "1":
            self.y_pred = "MDD"
            self.y_pred_proba = clf.predict_proba(result)[0][1]
        else:
            self.y_pred = "HC"
            self.y_pred_proba = clf.predict_proba(result)[0][0]

        self.y_pred_proba *= 100
        self.y_pred_proba = round(self.y_pred_proba, 2)

        fig, ax = plt.subplots(figsize=(6, 6))
        wedgeprops = {'width': 0.3, 'edgecolor': 'black', 'linewidth': 1}
        ax.pie([self.y_pred_proba, 100-self.y_pred_proba], wedgeprops=wedgeprops, startangle=90, colors=['#e25d61', '#6879f7'])
        plt.title(self.y_pred, fontsize=24, loc='center')
        plt.text(0, 0, str(self.y_pred_proba)+"%", ha='center', va='center', fontsize=42)
        plt.savefig("proba.png")


        self.y_pred_proba = str(self.y_pred_proba)
