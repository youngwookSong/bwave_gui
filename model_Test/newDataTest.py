import numpy as np
import os
import pickle
from model_Test.BwaveData import BwaveData as bd
from model_Test.BwaveData_source import BwaveData_s as bd_s
from model_Test.directory import ROOT_DIR
import matplotlib.pyplot as plt
import mne
import pandas as pd
import plotly.graph_objects as go
from PIL import Image

from model_Test.fc_plot import VisualizeFc

from resources import root

import json
from collections import OrderedDict

bands = ['Delta', 'Theta', 'LowAlpha', 'HighAlpha', 'LowBeta', 'HighBeta', 'Gamma']
ch_names = ['Fp1', 'Fp2', 'F7', 'F3', 'Fz', 'F4', 'F8', 'T7', 'C3', 'Cz', 'C4', 'T8', 'P7', 'P3', 'Pz', 'P4',
                    'P8', 'O1', 'O2']

class model_test:
    def __init__(self, file, dir):
        self.file = file
        self.dir = dir
        self.y_pred = None
        self.y_pred_proba_mdd = None
        self.y_pred_proba_hc = None
        self.best_model = None
        self.values = None

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

        self.y_pred_proba_mdd *= 100
        self.y_pred_proba_mdd = round(self.y_pred_proba_mdd, 2)
        self.y_pred_proba_hc *= 100
        self.y_pred_proba_hc = round(self.y_pred_proba_hc, 2)

        ## 확률 원형 그래프 그리기
        fig, ax = plt.subplots(figsize=(6, 6))
        wedgeprops = {'width': 0.3, 'edgecolor': 'black', 'linewidth': 1}
        ax.pie([self.y_pred_proba_mdd, 100-self.y_pred_proba_mdd], wedgeprops=wedgeprops, startangle=90, colors=['#e25d61', '#6879f7'])
        plt.title('MDD Probability', fontsize=24, loc='center')
        plt.text(0, 0, str(self.y_pred_proba_mdd)+"%", ha='center', va='center', fontsize=42)
        plt.savefig("{}/proba.png".format(self.dir), bbox_inches='tight', pad_inches=0)
        plt.close()

        self.y_pred_proba_mdd = str(self.y_pred_proba_mdd)
        self.y_pred_proba_hc = str(self.y_pred_proba_hc)

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

    def model_6_chart(self, psd, fc, ni):

        mdd_proba = (psd[1] + fc[1] + ni[1]) / 3
        hc_proba = (psd[0] + fc[0] + ni[0]) / 3

        self.y_pred_proba_mdd = mdd_proba
        self.y_pred_proba_hc = hc_proba

        if mdd_proba > hc_proba:
            self.y_pred = 'MDD'
            self.values = [psd[1] * 100, fc[1] * 100, ni[1] * 100, 78, 87, 83]
        else:
            self.y_pred = "HC"
            self.values = [psd[0] * 100, fc[0] * 100, ni[0] * 100, 78, 87, 83]

        model = ['psd', 'fc', 'ni', 's_psd', 's_fc', 's_ni']
        x = ['PSD', 'FC', 'NI', 'S_PSD', 'S_FC', 'S_NI']
        plt.figure(figsize=(9, 5))
        plt.tick_params(labelsize=13, length=3, bottom=False)
        bars = plt.bar(x, self.values, color='#54829C', alpha=0.5, width=0.7)
        bars[np.argmax(self.values)].set_color('r')
        self.best_model = model[np.argmax(self.values[:3])]
        plt.title('Predictive probability by model', fontsize=20)
        for i, v in enumerate(self.values):
            plt.text(x[i], v + 2.5, int(self.values[i]),  # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
                     fontsize=13,
                     color='black',
                     horizontalalignment='center',  # horizontalalignment (left, center, right)
                     verticalalignment='center')  # verticalalignment (top, center, bottom)
        plt.ylim(0, 107)
        plt.savefig("{}/mode_prob.png".format(self.dir), bbox_inches='tight', pad_inches=0.1)
        plt.close()


    def position_plot(self, result_psd, result_fc, result_ni):
        with open('{}/bwave_19_reg_4sec_plv/feature.pickle'.format(root), 'rb') as f:
            df = pickle.load(f)

        y_data = df['target'].to_numpy()
        x_data = [np.vstack(df['psd'].to_numpy())[:, np.load(os.path.join(ROOT_DIR, "model/idx_{}.npy".format('psd')))],
                  np.vstack(df['fc'].to_numpy())[:, np.load(os.path.join(ROOT_DIR, "model/idx_{}.npy".format('fc')))],
                  np.vstack(df['ni'].to_numpy())[:, np.load(os.path.join(ROOT_DIR, "model/idx_{}.npy".format('ni')))]]

        x_mdd = x_data[np.argmax(self.values[:3])][y_data == 1]
        x_hc = x_data[np.argmax(self.values[:3])][y_data == 0]

        plt.figure(figsize=(10, 6))
        plt.suptitle('{}'.format(self.best_model.upper()), fontsize=20)
        for i in range(3):
            y_hc = np.mean(x_hc[:, i], axis=0)
            yerr_hc = np.std(x_hc[:, i], axis=0) / np.sqrt(len(x_hc[:, i]))
            y_mdd = np.mean(x_mdd[:, i], axis=0)
            yerr_mdd = np.std(x_mdd[:, i], axis=0) / np.sqrt(len(x_mdd[:, i]))
            plt.subplot(1, 3, i + 1)
            plt.xlim(0, 1)
            data_1 = {
                'x': 0.2,
                'y': y_hc,
                'yerr': yerr_hc}
            data_2 = {
                'x': 0.8,
                'y': y_mdd,
                'yerr': yerr_mdd}
            plt.scatter(data_1['x'], y_hc, color='blue', alpha=1, marker='D', s=60)
            plt.scatter(data_2['x'], y_mdd, color='red', alpha=1, marker='D', s=60)
            plt.errorbar(**data_1, alpha=1, fmt='None', capsize=10, capthick=3, ecolor='blue', elinewidth=3)
            plt.errorbar(**data_2, alpha=1, fmt='None', capsize=10, capthick=3, ecolor='red', elinewidth=3)
            result_data=[result_psd, result_fc, result_ni]
            y_temp = result_data[np.argmax(self.values[:3])][0, i]
            # y_temp = getattr(mod, 'result_{}'.format(best))
            if y_hc > y_mdd:
                if y_temp < y_mdd - (yerr_mdd):
                    y_temp = y_mdd - (yerr_mdd)
                elif y_temp > y_hc + yerr_hc:
                    y_temp = y_hc + (yerr_hc)
            else:
                if y_temp < y_hc - yerr_hc:
                    y_temp = y_hc - (yerr_hc)
                elif y_temp > y_mdd + yerr_mdd:
                    y_temp = y_mdd + (yerr_mdd)
            plt.axhline(y=y_temp, color='g', linewidth=3, alpha=0.5)
            plt.scatter(0.47, y_temp, marker='o', s=120, color='g', alpha=0.5)
            plt.text(0.5, y_temp, 'Yours', color='black', size=16)
            plt.gca().axes.xaxis.set_ticks([])
            plt.gca().axes.yaxis.set_ticks([])
        plt.tight_layout(h_pad=0.5, w_pad=0.5)
        plt.savefig("{}/position_plot.png".format(self.dir), bbox_inches='tight', pad_inches=0.4)
        plt.close()

        # for i in range(3):
        #     y_hc = np.mean(x_hc[:, i], axis=0)
        #     yerr_hc = np.std(x_hc[:, i], axis=0) / np.sqrt(len(x_hc[:, i]))
        #     y_mdd = np.mean(x_mdd[:, i], axis=0)
        #     yerr_mdd = np.std(x_mdd[:, i], axis=0) / np.sqrt(len(x_mdd[:, i]))
        #     dist = abs(y_hc - y_mdd) / 4
        #     center = max(y_hc, y_mdd) - dist * 2
        #     result_data = [result_psd, result_fc, result_ni]
        #     y_temp = result_data[np.argmax(self.values[:3])][0, i]
        #     if y_temp >= y_mdd + dist * 5:
        #         y_temp = y_mdd + dist * 5
        #     elif y_temp <= y_hc - dist * 5:
        #         y_temp = y_hc - dist * 5
        #
        #     fig = go.Figure(
        #         go.Scatter(mode="markers", x=[3 - (y_temp - center) * 1 / dist], y=[1.05],
        #                    marker={'symbol': 'arrow-up', 'line_color': 'black', 'line_width': 1, 'color': 'yellow',
        #                            'size': 25},
        #                    hovertemplate="name: %{y}%{x}<br>number: %{marker.symbol}<extra></extra>"))
        #     image_path = os.path.join(ROOT_DIR, "data/base_F_bar.png")
        #     fig.add_layout_image(
        #         {'source': Image.open(image_path), 'xref': "x", 'yref': "y", 'x': 0, 'y': 2,
        #          'sizex': 6, 'sizey': 0.9,
        #          'sizing': "stretch", 'layer': "below"})
        #
        #     fig.update_layout(
        #         xaxis={'showgrid': False, 'zeroline': False, 'showline': False, 'showticklabels': False},
        #         yaxis={'showgrid': False, 'zeroline': False, 'showline': False, 'showticklabels': False},
        #         autosize=False,
        #         showlegend=False,
        #         plot_bgcolor='white', width=1200, height=550)
        #
        #     fig.update_layout(xaxis=dict(range=[-1, 6.5]), yaxis=dict(range=[-1, 4]))
        #     # fig.show()
        #     fig.write_image(os.path.join(self.dir, "si_bar.png"))

    def test(self):
        ## new data preprocess & feature extraction
        print(ROOT_DIR)
        file_path = self.file

        ##sensor----------------------------------------------------
        raw_file = bd()
        raw_file.load_file(file_path)
        raw_file.preprocess()

        # fig = raw_file.prep_epochs.plot_psd(fmin=1., fmax=55., show=False)
        # fig.figure.savefig("{}/psd_power.png".format(self.dir))
        # plt.close()

        raw_file.PSD()
        raw_file.FC()
        raw_file.NI()
        result_psd = raw_file.psd
        result_fc = raw_file.fc_f
        result_ni = raw_file.ni

        clf_psd, result_psd = self.prepare("psd", result_psd)
        clf_fc, result_fc = self.prepare("fc", result_fc)
        clf_ni, result_ni = self.prepare("ni", result_ni)

        ##source----------------------------------------
        # raw_file_s = bd_s()
        # raw_file_s.load_file(file_path)
        # raw_file_s.preprocess()
        #
        # raw_file_s.source_loc()
        # raw_file_s.PSD()
        # raw_file_s.FC()
        # raw_file_s.NI()
        # result_s_psd = raw_file_s.s_psd
        # result_s_fc = raw_file_s.s_fc_f
        # result_s_ni = raw_file_s.s_ni

        ## model 6개 확률 plot
        self.model_6_chart(clf_psd.predict_proba(result_psd)[0], clf_fc.predict_proba(result_fc)[0],
                           clf_ni.predict_proba(result_ni)[0])

        ## positin plot ---------------------------
        self.position_plot(result_psd, result_fc, result_ni)

        self.pred_n_plot()

        self.psd_plot(raw_file.psd[0], "rel")
        self.psd_plot(raw_file.psd_abs[0], "abs")

        self.ni_plot(raw_file.ni[0][28:])

        ##JSON
        with open('{}/info.json'.format(self.dir), 'r', encoding='utf-8') as make_file: #읽고
            data = json.load(make_file)
            data['y_pred'] = self.y_pred
            data['y_pred_proba_mdd'] = self.y_pred_proba_mdd
            data['y_pred_proba_hc'] = self.y_pred_proba_hc
            data['best_model'] = self.best_model

        with open('{}/info.json'.format(self.dir), 'w', encoding='utf-8') as make_file: #쓰기
            json.dump(data, make_file, ensure_ascii=False, indent='\t')

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