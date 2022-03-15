import numpy as np
import os
import pickle
from model_Test.BwaveData import BwaveData as bd
from model_Test.directory import ROOT_DIR

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

        self.y_pred = str(clf.predict(result)[0])
        self.y_pred_proba = str(clf.predict_proba(result)[0][1])

        if self.y_pred == "1":
            self.y_pred = "MDD"
        else:
            self.y_pred = "HC"

        print(self.y_pred)
        print(self.y_pred_proba)
