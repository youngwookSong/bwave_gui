import numpy as np
import os
import pickle
from model_Test.BwaveData import BwaveData as bd
from model_Test.directory import ROOT_DIR
import matplotlib.pyplot as plt
import mne
import pandas as pd

from model_Test.fc_plot import VisualizeFc

bands = ['Delta', 'Theta', 'LowAlpha', 'HighAlpha', 'LowBeta', 'HighBeta', 'Gamma']
ch_names = ['Fp1', 'Fp2', 'F7', 'F3', 'Fz', 'F4', 'F8', 'T7', 'C3', 'Cz', 'C4', 'T8', 'P7', 'P3', 'Pz', 'P4',
                    'P8', 'O1', 'O2']

class model_test:
    def __init__(self, file, dir):
        self.file = file
        self.dir = dir
        self.y_pred = None
        self.y_pred_proba = None

    def prepare(self, name, result):
        model_dir = os.path.join(ROOT_DIR, "model/model_{}".format(name))
        with open(model_dir, 'rb') as f:
            clf = pickle.load(f)

        # from sklearn import preprocessing
        # scaler_dir = os.path.join(ROOT_DIR, "model/scaler_{}.pickle".format(name))
        # with open(scaler_dir, 'rb') as f:
        #     scaler = pickle.load(f)
        # result = scaler.transform(result)

        fisher_dir = os.path.join(ROOT_DIR, "model/idx_{}.npy".format(name))
        idx = np.load(fisher_dir)
        result = result[:, idx]

        return clf, result


    def pred_n_plot(self): ## 확률 원 그래프

        self.y_pred_proba *= 100
        self.y_pred_proba = round(self.y_pred_proba, 2)

        ## 확률 원형 그래프 그리기
        fig, ax = plt.subplots(figsize=(6, 6))
        wedgeprops = {'width': 0.3, 'edgecolor': 'black', 'linewidth': 1}
        ax.pie([self.y_pred_proba, 100-self.y_pred_proba], wedgeprops=wedgeprops, startangle=90, colors=['#e25d61', '#6879f7'])
        plt.title(self.y_pred, fontsize=24, loc='center')
        plt.text(0, 0, str(self.y_pred_proba)+"%", ha='center', va='center', fontsize=42)
        plt.savefig("{}/proba.png".format(self.dir), bbox_inches='tight', pad_inches=0)
        plt.close()

        self.y_pred_proba = str(self.y_pred_proba)

    def psd_plot(self, psd, power): # 위 두줄

        temp_montage = mne.channels.make_standard_montage('biosemi64')
        temp_info = mne.create_info(ch_names, 1, ch_types='eeg', verbose=None)
        temp_info.set_montage(temp_montage)

        temp = np.split(psd, 7)
        bn = [temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6]]
        band_psd = np.array([])
        for i in range(len(bn)):
            band_psd = np.hstack((band_psd, bn[i]))

        if power == "rel":
            csv_dir = os.path.join(ROOT_DIR, "data/HC_reg_rel_PSD_band_335.csv")
            hc = pd.read_csv(csv_dir)

            zscore_psd = np.zeros(133)
            for i in range(len(band_psd)):
                zscore_psd[i] = (band_psd[i] - hc.values[0][i]) / hc.values[1][i]
            zscore_psd = np.split(zscore_psd, 7)

            for i in range(len(zscore_psd)):
                fig, _ = mne.viz.plot_topomap(zscore_psd[i], pos=temp_info, vmin=-3, vmax=3, cmap='rainbow', show=False, contours=0)
                # plt.show()
                fig.figure.savefig("{}/relative_{}.png".format(self.dir, bands[i]), bbox_inches='tight', pad_inches=0.4)
                plt.close()

        if power == "abs":
            csv_dir = os.path.join(ROOT_DIR, "data/HC_reg_abs_PSD_band_335.csv")
            hc = pd.read_csv(csv_dir)

            zscore_psd = np.zeros(133)
            for i in range(len(band_psd)):
                zscore_psd[i] = (band_psd[i] - hc.values[0][i]) / hc.values[1][i]
            zscore_psd = np.split(zscore_psd, 7)

            for i in range(len(zscore_psd)):
                fig, _ = mne.viz.plot_topomap(zscore_psd[i], pos=temp_info, vmin=-3, vmax=3, cmap='rainbow', show=False,
                                              contours=0)
                # plt.show()
                fig.figure.savefig("{}/absolute_{}.png".format(self.dir, bands[i]), bbox_inches='tight', pad_inches=0.4)
                plt.close()

    def ni_plot(self, ni):

        temp_montage = mne.channels.make_standard_montage('biosemi64')
        temp_info = mne.create_info(ch_names, 1, ch_types='eeg', verbose=None)
        temp_info.set_montage(temp_montage)

        nodal = ni
        nodal_band = np.split(nodal, 7)

        clustering = np.array([])
        for i in range(len(nodal_band)):
            temp = np.array(np.split(nodal_band[i], 2)[1])
            clustering = np.hstack((clustering, temp)) if clustering.size else temp

        csv_dir = os.path.join(ROOT_DIR, "data/HC_reg_plv_ni_clustering_335.csv")
        hc_clustering = pd.read_csv(csv_dir)

        zscore_clustering = np.zeros(len(hc_clustering.columns))
        for i in range(len(clustering)):
            zscore_clustering[i] = (clustering[i] - hc_clustering.values[0][i]) / hc_clustering.values[1][i]
        zscore_clustering = np.split(zscore_clustering, 7)

        for i in range(7):
            fig_ni, _ = mne.viz.plot_topomap(zscore_clustering[i], pos=temp_info, vmin=-3, vmax=3, cmap='rainbow',
                                             show=False,
                                             contours=0)
            # plt.show()
            fig_ni.figure.savefig("{}/network_{}.png".format(self.dir, bands[i]), bbox_inches='tight', pad_inches=0.4)
            plt.close()


    def test(self):
        ## new data preprocess & feature extraction
        print(ROOT_DIR)
        file_path = self.file

        raw_file = bd()
        raw_file.load_file(file_path)
        raw_file.preprocess()

        fig = raw_file.prep_epochs.plot_psd(fmin=1., fmax=55., show=False)
        fig.figure.savefig("{}/psd_power.png".format(self.dir))
        plt.close()

        raw_file.PSD()
        raw_file.FC()
        raw_file.NI()
        result_psd = raw_file.psd
        result_fc = raw_file.fc_f
        result_ni = raw_file.ni

        clf_fc, result_fc = self.prepare("fc", result_fc)
        clf_psd, result_psd = self.prepare("psd", result_psd)
        clf_ni, result_ni = self.prepare("ni", result_ni)

        mdd_proba = (clf_fc.predict_proba(result_fc)[0][1] + clf_psd.predict_proba(result_psd)[0][1] +
                     clf_ni.predict_proba(result_ni)[0][1]) / 3
        hc_proba = (clf_fc.predict_proba(result_fc)[0][0] + clf_psd.predict_proba(result_psd)[0][0] +
                     clf_ni.predict_proba(result_ni)[0][0]) / 3


        if mdd_proba > hc_proba:
            self.y_pred = 'MDD'
            self.y_pred_proba = mdd_proba
            values = [clf_psd.predict_proba(result_psd)[0][1]*100, clf_fc.predict_proba(result_fc)[0][1]*100, clf_ni.predict_proba(result_ni)[0][1]*100,78,87,84]
            # values = [71, 92.5, 90, 78, 87, 84]
            x = ['PSD', 'FC', 'NI', 'S_PSD', 'S_FC', 'S_NI']
            plt.figure(figsize=(8, 5))
            plt.tick_params(labelsize=13, length=3, bottom=False)
            bars = plt.bar(x, values, color='#54829C', alpha=0.5, width=0.7)
            bars[np.argmax(values)].set_color('r')
            plt.title('Predictive probability by model', fontsize=20)
            for i, v in enumerate(values):
                plt.text(x[i], v + 3, int(values[i]),  # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
                         fontsize=14,
                         color='black',
                         horizontalalignment='center',  # horizontalalignment (left, center, right)
                         verticalalignment='center')  # verticalalignment (top, center, bottom)
            plt.ylim(0, 103)
            plt.savefig("{}/mode_prob.png".format(self.dir))
            plt.close()
        else:
            self.y_pred = "HC"
            self.y_pred_proba = hc_proba
            values = [clf_psd.predict_proba(result_psd)[0][0] * 100, clf_fc.predict_proba(result_fc)[0][0] * 100,
                      clf_ni.predict_proba(result_ni)[0][0] * 100, 78, 87, 84]
            # values = [71, 92.5, 90, 78, 87, 84]
            x = ['PSD', 'FC', 'NI', 'S_PSD', 'S_FC', 'S_NI']
            plt.figure(figsize=(8, 5))
            plt.tick_params(labelsize=13, length=3, bottom=False)
            bars = plt.bar(x, values, color='#54829C', alpha=0.5, width=0.7)
            bars[np.argmax(values)].set_color('r')
            plt.title('Predictive probability by model', fontsize=20)
            for i, v in enumerate(values):
                plt.text(x[i], v + 3, int(values[i]),  # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
                         fontsize=14,
                         color='black',
                         horizontalalignment='center',  # horizontalalignment (left, center, right)
                         verticalalignment='center')  # verticalalignment (top, center, bottom)
            plt.ylim(0, 103)
            plt.savefig("{}/mode_prob.png".format(self.dir))
            plt.close()

        print(mdd_proba, hc_proba)



        self.pred_n_plot()

        self.psd_plot(raw_file.psd[0], "rel")
        self.psd_plot(raw_file.psd_abs[0], "abs")

        self.ni_plot(raw_file.ni[0][28:])

        ##  ------------------- fc_plot

        csv_dir = os.path.join(ROOT_DIR, "data/HC_reg_plv_335.csv")
        hc = pd.read_csv(csv_dir)

        zscore_plv = np.zeros(len(raw_file.fc_f[0]))
        for i in range(len(zscore_plv)):
            zscore_plv[i] = (raw_file.fc_f[0][i] - hc.values[0][i]) / hc.values[1][i]


        for i in range(7):
            vis_bwave = VisualizeFc(zscore_plv, idx_dir=None, vmin=-3, vmax=3, freq_band=i)
            vis_bwave.mean_plot()
            vis_bwave.fig.figure.savefig("{}/plv_{}.png".format(self.dir, bands[i]), facecolor='#ffffff', bbox_inches='tight', pad_inches=0)
            plt.close()