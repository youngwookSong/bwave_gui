import numpy as np
import pickle
from model_Test.BwaveData import BwaveData as bd

class model_test:
    def __init__(self, file):
        self.file = file
        self.y_pred = None
        self.y_pred_proba = None

    def test(self):
        ## new data preprocess & feature extraction
        file_path = self.file

        raw_file = bd()
        raw_file.load_file(file_path)
        raw_file.preprocess()
        raw_file.FC()
        result = raw_file.fc_f

        name = "fc"
        with open("C:/Users/Bwave/Documents/GitHub/bwave_gui/model_Test/model_{}_proba.pickle".format(name), 'rb') as f:
            clf = pickle.load(f)

        from sklearn import preprocessing
        with open("C:/Users/Bwave/Documents/GitHub/bwave_gui/model_Test/scaler.pickle", 'rb') as f:
            scaler = pickle.load(f)
        result = scaler.transform(result)

        idx = np.load('C:/Users/Bwave/Documents/GitHub/bwave_gui/model_Test/fis.npy')
        result = result[:, idx]

        self.y_pred = str(clf.predict(result)[0])
        self.y_pred_proba = str(clf.predict_proba(result)[0][1])

        if self.y_pred == "1":
            self.y_pred = "MDD"
        else:
            self.y_pred = "HC"

        print(self.y_pred)
        print(self.y_pred_proba)
