import numpy as np
from matplotlib import pyplot as plt
import pickle
import os

import mne
from model_Test.BwaveData import BwaveData as bd
from model_Test.directory import ROOT_DIR

name = "psd"
band = ['delta','theta','low alpha','high alpha','low beta','high beta','gamma']
ch = ['FP1', 'FP2', 'F7', 'F3', 'FZ', 'F4', 'F8', 'T7', 'C3', 'CZ', 'C4', 'T8',
                                     'P7', 'P3', 'PZ', 'P4', 'P8', 'O1', 'O2', 'VEO', 'HEO']
idx = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
# fisher_dir = os.path.join(ROOT_DIR, "fis.npy")
# idx = np.load(fisher_dir)

with open('../3.15-11.15_bwave_19_4sec_imcoh/feature.pickle', 'rb') as f: # mdd
    df = pickle.load(f)
    print("전체 df: ", df.shape)

x_data = df[name].to_numpy()
x_data = np.vstack(x_data)
# x = pd.DataFrame(x)
y_data = df['target'].to_numpy()

x_mdd_b = x_data[y_data == 1]
x_hc_b = x_data[y_data == 0]

from scipy import stats
count = 0
for i in idx:
    t_stat, p_val = stats.ttest_ind(x_mdd_b[:, i], x_hc_b[:, i])
    if p_val < 0.05:
        if name == 'psd':
            print(band[i//19], ch[i%19]) # if psd
        data_1 = {
            'x': ['mdd'],
            'y': np.mean(x_mdd_b[:,i], axis=0),
            'yerr': np.std(x_mdd_b[:,i], axis=0)/np.sqrt(len(x_mdd_b[:,i]))}
        data_2 = {
            'x': ['hc'],
            'y': np.mean(x_hc_b[:, i], axis=0),
            'yerr': np.std(x_hc_b[:, i], axis=0)/np.sqrt(len(x_hc_b[:, i]))}
        data1 = {
            'x': data_1['x'],
            'y1': data_1['y']-data_1['yerr'],
            'y2': data_1['y']+data_1['yerr']}
        data2 = {
            'x': data_2['x'],
            'y1': data_2['y']-data_2['yerr'],
            'y2': data_2['y']+data_2['yerr']}


        plt.figure(figsize=(8,5))
        plt.scatter(data_1['x'],data_1['y'], color='red', alpha=1, marker='D',s=60)
        plt.scatter(data_2['x'],data_2['y'], color='blue', alpha=1, marker='D',s=60)
        plt.errorbar(**data_1, alpha=1, fmt='None',capsize=10,capthick=3, color='red')
        plt.errorbar(**data_2, alpha=1, fmt='None',capsize=10,capthick=3, color='blue')
        plt.xticks( fontsize=15)
        plt.yticks( fontsize=13)
        plt.title('psd', fontsize=20)
        plt.legend(['mdd','hc'])
        plt.show()
        count = count+1
print(count)
