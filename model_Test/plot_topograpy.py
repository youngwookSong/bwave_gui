import numpy as np
from matplotlib import pyplot as plt
import pickle

import mne
from model_Test.BwaveData import BwaveData as bd

raw_data_path = "C:/Users/Bwave/Desktop/bwave_pro_data/bwave/MDD/0383662.cnt"

raw_file = bd()
raw_file.load_file(raw_data_path)

print(raw_file.raw)
print(raw_file.raw.info)
print(raw_file.raw.get_data().shape) #(ch, time)
print("---------------" * 4, "preprocessing")

raw_file.preprocess()

print(raw_file.prep_epochs.get_data().shape) #(epoch, ch, time)
print(raw_file.prep_epochs.info)


fig = raw_file.prep_epochs.plot_psd(fmin=1., fmax=55.)
fig.savefig("./plot_image/psd.png")
#
# for i in range(7):
#     fig = raw_file.prep_epochs.plot_psd_topomap(bands=[(1,4,"Delta")], ch_type='eeg', normalize=True,
#                                                vlim=(-3,3), cmap='rainbow')
#
#     # plt.close(fig)
#     fig.savefig("./plot_image/psd_topomap.png")

raw_file.PSD()
print(raw_file.psd.shape)

import pandas as pd
bands = ['Delta', 'Theta', 'Low Alpha', 'High Alpha', 'Low Beta', 'High Beta', 'Gamma']
ch_names = ['Fp1', 'Fp2','F7', 'F3', 'Fz','F4','F8','T7', 'C3', 'Cz', 'C4', 'T8', 'P7', 'P3', 'Pz', 'P4', 'P8', 'O1', 'O2']
temp_montage = mne.channels.make_standard_montage('biosemi64')
temp_info = mne.create_info(ch_names, 1, ch_types='eeg', verbose=None)
temp_info.set_montage(temp_montage)

hc = pd.read_csv('HC_PSD_info_378.csv')

zscore_psd = np.zeros(133)
for i in range(len(raw_file.psd[0])):
    zscore_psd[i] = (raw_file.psd[0][i] - hc.values[0][i])/hc.values[1][i]
zscore_psd = np.split(zscore_psd, 7)

for i in range(len(zscore_psd)):
    plt.title(bands[i])
    fig, _ = mne.viz.plot_topomap(zscore_psd[i], pos=temp_info, vmin=-3, vmax=3, cmap='rainbow', show=False)
    fig.figure.savefig("./plot_image/psd_topomap_{}.png".format(bands[i]))




