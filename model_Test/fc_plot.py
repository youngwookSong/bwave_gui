import numpy as np
import mne
import matplotlib.pyplot as plt
import os
import pandas as pd
from sklearn import preprocessing
import pickle
from model_Test.directory import ROOT_DIR


band_num = 7
ch_names = ['FP1', 'FP2', 'F7', 'F3', 'FZ', 'F4', 'F8', 'T7', 'C3', 'CZ', 'C4', 'T8',
            'P7', 'P3', 'PZ', 'P4', 'P8', 'O1', 'O2']
idx = 'fis0.npy'
feat_name = "fc"

class VisualizeFc:
    def __init__(self,
                 plv,
                 idx_dir,
                 vmin=0.4,
                 vmax=1.,
                 freq_band=None
                 ):

        if idx_dir:
            self.idx = np.load(idx_dir) # fisher score로 할때
            self.idx = self._set_freq_band(self.idx, freq_band) # 해당 frequency의 피쳐를 뽑기위해
        else:
            self.idx = np.array([i for i in range(len(plv))])
            self.idx = self._set_freq_band(self.idx, freq_band) # 해당 frequency의 피쳐를 뽑기위해
        self.vmin = vmin
        self.vmax = vmax
        self._vis_index()
        self.plv = plv

    def mean_plot(self,start=0, end=-1):
        print("plv: ",self.plv.shape)
        feat = self.plv[self.idx]
        feat[abs(feat) < 2] = 0
        self.fig, _ = mne.viz.plot_connectivity_circle(feat, ch_names, (self.viz_i, self.viz_j),
                                          vmin=self.vmin, vmax=self.vmax, show=True, fontsize_names=13,
                                         facecolor="#ffffff", textcolor="#000000",colormap='bwr', colorbar=False)


    def _set_freq_band(self, idx, s):
        if s == None:
            return idx
        else:
            return idx[idx // 171 == s]

    def _vis_index(self):
        csv_dir = os.path.join(ROOT_DIR, "data/comb.csv")
        dataset = pd.read_csv(csv_dir, index_col=0)
        self.viz_i = np.array([], dtype=np.int64)
        self.viz_j = np.array([], dtype=np.int64)

        for fis in self.idx:
            both = dataset.iloc[fis]['comb'].split(',')
            self.viz_i = np.append(self.viz_i, int(both[0])-1)
            self.viz_j = np.append(self.viz_j, int(both[1])-1)

    def _reconsturct_tri(self):
        freq = 7
        n = 61
        A = np.zeros((n + 1, n + 1, freq))
        for f in range(freq):
            k = 0
            for i in range(n + 1):
                for j in range(i + 1, n + 1):
                    A[i, j, f] = self.features[k * 7 + f]
                    k = k + 1
        return A