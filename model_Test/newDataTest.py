import matplotlib
import numpy as np
import os
import pickle
from model_Test.BwaveData import BwaveData as bd
from model_Test.BwaveData_source import BwaveData_s as bd_s
from model_Test.directory import ROOT_DIR
import matplotlib.pyplot as plt
import mne
import pandas as pd

from PIL import Image
import matplotlib.image as img
from matplotlib.figure import Figure
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt

from model_Test.fc_plot import VisualizeFc
from model_Test.directory import FUNCDATA_DIR

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
        self.tr_proba = None
        self.psd_infl_band = None
        self.fc_infl_band = None
        self.ni_infl_band = None

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
        print("{} best_fisher_idx_3: ".format(name), idx[:3])

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

        temp_montage = mne.channels.read_custom_montage(os.path.join(FUNCDATA_DIR, 'biosemi64.txt'))
        temp_info = mne.create_info(ch_names, 1, ch_types='eeg', verbose=None)
        temp_info.set_montage(temp_montage)

        temp = np.split(psd, 7)
        bn = [temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6]]
        band_psd = np.array([])
        for i in range(len(bn)):
            band_psd = np.hstack((band_psd, bn[i]))

        if power == "rel":
            hc = pd.read_csv(os.path.join(ROOT_DIR, "data/st_database2/HC_psd_338.csv"))

            zscore_psd = np.zeros(133)
            for i in range(len(band_psd)):
                zscore_psd[i] = (band_psd[i] - hc.values[0][i]) / hc.values[1][i]
            zscore_psd = np.split(zscore_psd, 7)

            for i in range(len(zscore_psd)): # zscore_psd = (7*19) 19개 채널을 plot_topomap에 넣어서 topomap 그림
                fig, _ = mne.viz.plot_topomap(zscore_psd[i], pos=temp_info, vmin=-3, vmax=3, cmap='rainbow', show=False,
                                              contours=4, sensors=True, onselect=True, names=ch_names)
                # plt.show()
                fig.figure.savefig("{}/relative_{}.png".format(self.dir, bands[i]), bbox_inches='tight', pad_inches=0.4)
                plt.close()

        if power == "abs":
            hc = pd.read_csv(os.path.join(ROOT_DIR, "data/st_database1/HC_reg_abs_PSD_band_335.csv"))

            zscore_psd = np.zeros(133)
            for i in range(len(band_psd)):
                zscore_psd[i] = (band_psd[i] - hc.values[0][i]) / hc.values[1][i]
            zscore_psd = np.split(zscore_psd, 7)

            for i in range(len(zscore_psd)):
                fig, _ = mne.viz.plot_topomap(zscore_psd[i], pos=temp_info, vmin=-3, vmax=3, cmap='rainbow', show=False,
                                              contours=4, sensors=True, onselect=True, names=ch_names)
                # plt.show()
                fig.figure.savefig("{}/absolute_{}.png".format(self.dir, bands[i]), bbox_inches='tight', pad_inches=0.4)
                plt.close()

    def psd_fre_make_png(self, power):
        ## plot 하나에 이미지로 만듬
        new_im = [Image.new('RGB', (509 * 5, 525 * 6), "white"), Image.new('RGB', (509 * 5, 525 * 6), "white")]
        x_offset = 0
        y_offset = 0
        change_new = 0
        for i in range(55):
            file = os.path.join(self.fre_dir, "{}{}.png".format(power, i))
            im = Image.open(file)
            new_im[change_new].paste(im, (x_offset, y_offset))
            x_offset += im.size[0]
            if x_offset == 509 * 5:
                y_offset += im.size[1]
                x_offset = 0
            if y_offset == 525 * 6:
                y_offset = 0
                change_new = 1
            os.remove(file)

        new_im[0].save(os.path.join(self.fre_dir, 'frequency_{}_1.png'.format(power)))
        new_im[1].save(os.path.join(self.fre_dir, 'frequency_{}_2.png'.format(power)))

    def psd_fre(self, psd_hz, power):
        hz = np.linspace(1, 55, 55).astype(int)
        ch_names = ['Fp1', 'Fp2', 'F7', 'F3', 'Fz', 'F4', 'F8', 'T7', 'C3', 'Cz', 'C4', 'T8', 'P7', 'P3', 'Pz', 'P4',
                    'P8', 'O1', 'O2']

        temp_montage = mne.channels.read_custom_montage(os.path.join(FUNCDATA_DIR, 'biosemi64.txt'))
        temp_info = mne.create_info(ch_names, 1, ch_types='eeg', verbose=None)
        temp_info.set_montage(temp_montage)

        self.fre_dir = os.path.join(self.dir, "frequency")
        try:
            if not os.path.exists(self.fre_dir):
                os.makedirs(self.fre_dir)
        except OSError:
            print('Error: Creating directory. ' + self.fre_dir)

        if power == "rel":
            hc = pd.read_csv(os.path.join(ROOT_DIR, "data/st_database1/HC_reg_rel_PSD_Hz_335.csv"))

            zscore_psd_hz = np.zeros(len(hc.columns))
            for i in range(len(psd_hz)):
                zscore_psd_hz[i] = (psd_hz[i] - hc.values[0][i]) / hc.values[1][i]
            zscore_psd_hz = np.split(zscore_psd_hz, 55)

            for i in range(len(zscore_psd_hz)):
                plt.title(str(hz[i]) + " Hz", fontsize=30)
                fig, _ = mne.viz.plot_topomap(zscore_psd_hz[i], pos=temp_info, vmin=-3, vmax=3, cmap='rainbow',
                                              show=False)
                fig.figure.savefig("{}/rel{}.png".format(self.fre_dir, i), bbox_inches='tight', pad_inches=0.4)
                plt.close()

        if power == "abs":
            hc = pd.read_csv(os.path.join(ROOT_DIR, "data/st_database1/HC_reg_abs_PSD_Hz_335.csv"))

            zscore_psd_hz = np.zeros(len(hc.columns))
            for i in range(len(psd_hz)):
                zscore_psd_hz[i] = (psd_hz[i] - hc.values[0][i]) / hc.values[1][i]
            zscore_psd_hz = np.split(zscore_psd_hz, 55)

            for i in range(len(zscore_psd_hz)):
                plt.title(str(hz[i]) + " Hz", fontsize=30)
                fig, _ = mne.viz.plot_topomap(zscore_psd_hz[i], pos=temp_info, vmin=-3, vmax=3, cmap='rainbow',
                                              show=False)
                fig.figure.savefig("{}/abs{}.png".format(self.fre_dir, i), bbox_inches='tight', pad_inches=0.4)
                plt.close()

        self.psd_fre_make_png(power)

    def fc_plot(self, fc):
        hc = pd.read_csv(os.path.join(ROOT_DIR, "data/st_database2/HC_fc_338.csv"))

        zscore_plv = np.zeros(len(fc))
        for i in range(len(zscore_plv)):
            zscore_plv[i] = (fc[i] - hc.values[0][i]) / hc.values[1][i]

        for i in range(7):
            vis_bwave = VisualizeFc(zscore_plv, idx_dir=None, vmin=-3, vmax=3, freq_band=i, n_lines=5)
            vis_bwave.mean_plot()
            vis_bwave.fig.figure.savefig("{}/plv_{}.png".format(self.dir, bands[i]), facecolor='#ffffff',
                                         bbox_inches='tight', pad_inches=0)
            plt.close()

    def ni_plot(self, ni):

        temp_montage = mne.channels.read_custom_montage(os.path.join(FUNCDATA_DIR, 'biosemi64.txt'))
        temp_info = mne.create_info(ch_names, 1, ch_types='eeg', verbose=None)
        temp_info.set_montage(temp_montage)

        nodal = ni
        nodal_band = np.split(nodal, 7)

        clustering = np.array([])
        for i in range(len(nodal_band)):
            temp = np.array(np.split(nodal_band[i], 2)[1])
            clustering = np.hstack((clustering, temp)) if clustering.size else temp

        csv_dir = os.path.join(ROOT_DIR, "data/st_database1/HC_reg_plv_ni_clustering_335.csv")
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
        for i, v in enumerate(self.values):
            plt.text(x[i], v + 2.5, int(self.values[i]),  # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
                     fontsize=13,
                     color='black',
                     horizontalalignment='center',  # horizontalalignment (left, center, right)
                     verticalalignment='center')  # verticalalignment (top, center, bottom)
        plt.ylim(0, 107)
        plt.savefig("{}/mode_prob.png".format(self.dir), bbox_inches='tight', pad_inches=0.1)
        plt.close()

    def find_idx_plot(self, list, name, x_new):
        band = ['delta', 'theta', 'low alpha', 'high alpha', 'low beta', 'high beta', 'gamma']
        ch = ['FP1', 'FP2', 'F7', 'F3', 'FZ', 'F4', 'F8', 'T7', 'C3', 'CZ', 'C4', 'T8',
              'P7', 'P3', 'PZ', 'P4', 'P8', 'O1', 'O2']

        with open('{}/bwave_19_reg_4sec_plv/feature.pickle'.format(ROOT_DIR), 'rb') as f:
            df = pickle.load(f)

        x = df[name].to_numpy()
        x_data = np.vstack(x)
        sort = df['sort'].to_numpy()
        y_data = df['target'].to_numpy()
        x_ref = x_data[sort == 'treatment refractory']
        x_good = x_data[sort == 'good treatment response']

        score_list = []
        for i in list:
            score = 1
            print("###########################################")

            new = x_new[0, i]
            good = np.mean(x_good[:, i], axis=0)
            ref = np.mean(x_ref[:, i], axis=0)

            # print(i, band[i // 19] + " " + str(ch[i % 19]) + ", idx: " + str(i))
            print("idx: ", i)
            print("new: ", new)
            print("good: ", good)
            print("refractory", ref)

            if abs(good - new) < abs(ref - new):
                score = 0

            score_list.append(score)

        print(score_list)

        return score_list

    def tr_probabilty(self, result_psd, result_fc, result_ni):
        psd_eff_idx = [81, 80, 85, 84, 116, 79, 82, 90, 86, 77]
        fc_eff_idx = [840, 1182, 305, 1011, 1022, 327, 498, 156, 338, 254]
        ni_eff_idx = [110, 185, 113, 160, 109, 111, 189, 33, 118, 223]

        all_score = self.find_idx_plot(psd_eff_idx, "psd", result_psd) + \
                    self.find_idx_plot(fc_eff_idx, "fc", result_fc) + self.find_idx_plot(ni_eff_idx, "ni", result_ni)

        print(all_score)
        self.tr_proba = str(round(all_score.count(1)/len(all_score) * 100, 2))

    def main_detail(self, result, name, prenum, nexnum):
        # TODO: ni 활성화 (지금은 그냥 psd3-6idx로 ni를 넣어둠. idx계산해서 psd랑 똑같이 해놓기)
        band = ['Delta', 'Theta', 'LowAlpha', 'HighAlpha', 'LowBeta', 'HighBeta', 'Gamma']
        ch_names = ['Fp1', 'Fp2', 'F7', 'F3', 'Fz', 'F4', 'F8', 'T7', 'C3', 'Cz', 'C4', 'T8', 'P7', 'P3', 'Pz', 'P4',
                    'P8', 'O1', 'O2']

        temp_data = result
        zscore_psd = np.zeros(len(temp_data))
        hc = pd.read_csv(os.path.join(ROOT_DIR, "data/st_database2/HC_{}_338.csv".format(name)))
        for i in range(len(zscore_psd)):
            zscore_psd[i] = (temp_data[i] - hc.values[0][i]) / hc.values[1][i]

        idx = np.load(os.path.join(ROOT_DIR, "model/idx_psd.npy"))
        idx = idx[prenum:nexnum] # TODO: ni 활성화 (지금은 그냥 psd3-6idx로 ni를 넣어둠)

        marker_params = dict(marker='o', markerfacecolor='w', markeredgecolor='k', markeredgewidth=1.5,
                             markersize=35, fillstyle='full', alpha=.6)
        temp_montage = mne.channels.read_custom_montage(os.path.join(FUNCDATA_DIR, 'biosemi64.txt'))
        temp_info = mne.create_info(ch_names, 1, ch_types='eeg', verbose=None)
        temp_info.set_montage(temp_montage)

        for i in range(len(idx)):
            freq_band = idx[i] // 19
            print("psd_idx:", freq_band, idx[i] % 19)
            zscore_psd_freq = zscore_psd[19 * freq_band:19 * (freq_band + 1)]
            mask = np.zeros(zscore_psd_freq.shape, dtype='bool')
            mask[idx[i] % 19] = True
            plt.rcParams.update({'font.size': 22, 'font.weight': 'bold', 'text.color': 'k'})
            fig, _ = mne.viz.plot_topomap(zscore_psd_freq, pos=temp_info, show=False, cmap='rainbow', vmin=-3, vmax=3,
                                          contours=4,
                                          sensors=True, show_names=True, names=ch_names,
                                          mask=mask, mask_params=marker_params)

            # TODO: ni 활성화 (지금은 그냥 psd3-6idx로 ni를 넣어둠. )
            fig.figure.savefig("{}/{}_detail_{}.png".format(self.dir, name, i), bbox_inches='tight', pad_inches=0.4)
            plt.close()

        if self.y_pred == "MDD":  # MDD
            print("max index:", np.argmax(abs(zscore_psd)), "freq band:", (band[np.argmax(abs(zscore_psd)) // 19]),
                  "channel:", ch_names[np.argmax(abs(zscore_psd)) % 19])
            freq_band = np.argmax(abs(zscore_psd)) // 19
            zscore_psd = zscore_psd[19 * freq_band:19 * (freq_band + 1)]
            mask = np.zeros(zscore_psd.shape, dtype='bool')
            mask[np.argmax(abs(zscore_psd))] = True
        else:
            print("min index:", np.argmin(abs(zscore_psd)), "freq band:", band[np.argmin(abs(zscore_psd)) // 19],
                  "channel:", ch_names[np.argmin(abs(zscore_psd)) % 19])
            freq_band = np.argmin(abs(zscore_psd)) // 19
            zscore_psd = zscore_psd[19 * freq_band:19 * (freq_band + 1)]
            mask = np.zeros(zscore_psd.shape, dtype='bool')
            mask[np.argmin(abs(zscore_psd))] = True

        # TODO: ni 활성화 (지금은 그냥 topo theta를 넣음)
        self.psd_infl_band = band[freq_band]
        self.ni_infl_band = band[freq_band + 1]
        plt.rcParams.update({'font.size': 22, 'font.weight': 'bold', 'text.color': 'k'})
        fig, _ = mne.viz.plot_topomap(zscore_psd, pos=temp_info, show=False, cmap='bwr',
                                      vmin=-3, vmax=3, contours=4,
                                      sensors=True, show_names=True, names=ch_names,
                                      mask=mask, mask_params=marker_params)
        fig.figure.savefig("{}/psd_infl.png".format(self.dir), bbox_inches='tight', pad_inches=0.4)
        plt.close()

    def main_detail_fc(self, result):
        temp_data = result
        zscore_plv = np.zeros(len(temp_data))
        hc = pd.read_csv(os.path.join(ROOT_DIR, "data/st_database2/HC_fc_338.csv"))
        for i in range(len(zscore_plv)):
            zscore_plv[i] = (temp_data[i] - hc.values[0][i]) / hc.values[1][i]
        print(zscore_plv.shape)

        band_num = 7
        band = ['Delta', 'Theta', 'LowAlpha', 'HighAlpha', 'LowBeta', 'HighBeta', 'Gamma']
        ch_names = ['FP1', 'FP2', 'F7', 'F3', 'FZ', 'F4', 'F8', 'T7', 'C3', 'CZ', 'C4', 'T8',
                    'P7', 'P3', 'PZ', 'P4', 'P8', 'O1', 'O2']
        comb_data = pd.read_csv(os.path.join(ROOT_DIR, "data/comb.csv"))
        idx_1 = os.path.join(ROOT_DIR, "model/idx_fc.npy")
        idx = np.load(idx_1)[:3]

        for i in range(len(idx)):
            freq_band = idx[i] // 171
            print(idx[i], freq_band)
            # print(comb[idx[i]], band[freq_band])
            vis_bwave = VisualizeFc(zscore_plv, idx_dir=idx_1, vmin=-3, vmax=3,
                                    freq_band=freq_band, n_lines=1)
            vis_bwave.mean_plot()
            vis_bwave.fig.figure.savefig("{}/plv_detail_{}.png".format(self.dir, i), facecolor='#ffffff',
                                         bbox_inches='tight', pad_inches=0)
            plt.close()

        if self.y_pred == "MDD":  # MDD
            print("max index:", np.argmax(abs(zscore_plv)), "freq band:", band[np.argmax(abs(zscore_plv)) // 171])
            freq_band = np.argmax(abs(zscore_plv)) // 171
        else:
            print("min index:", np.argmin(abs(zscore_plv)), "freq band:", band[np.argmin(abs(zscore_plv)) // 171])
            freq_band = np.argmin(abs(zscore_plv)) // 171

        self.fc_infl_band = band[freq_band]
        vis_bwave = VisualizeFc(zscore_plv, idx_dir=None, vmin=-3, vmax=3, freq_band=freq_band, n_lines=1)
        vis_bwave.mean_plot()
        vis_bwave.fig.figure.savefig("{}/plv_infl.png".format(self.dir), facecolor='#ffffff',
                                     bbox_inches='tight', pad_inches=0)
        plt.close()

    def gradientbars(self, bars):
        ax = bars[0].axes
        lim = ax.get_xlim() + ax.get_ylim()
        for bar in bars:
            bar.set_zorder(1)
            bar.set_facecolor("none")
            x, y = bar.get_xy()
            w, h = bar.get_width(), bar.get_height()
            grad = np.atleast_2d(np.linspace(0, 1 * w / 6, 256))
            cmap = plt.get_cmap('coolwarm_r')
            ax.imshow(grad, extent=[x, x + w, y, y + h], aspect="auto", zorder=0,
                      norm=matplotlib.colors.NoNorm(vmin=0, vmax=1), cmap=cmap)
        ax.axis(lim)

    def feature_detail(self, result, feature):
        band = ['delta', 'theta', 'low alpha', 'high alpha', 'low beta', 'high beta', 'gamma']
        ch = ['FP1', 'FP2', 'F7', 'F3', 'FZ', 'F4', 'F8', 'T7', 'C3', 'CZ', 'C4', 'T8', 'P7', 'P3', 'PZ', 'P4', 'P8',
              'O1', 'O2', 'VEO', 'HEO']

        hc = pd.read_csv(os.path.join(ROOT_DIR, "data/st_database2/HC_{}_338.csv".format(feature)))
        mdd = pd.read_csv(os.path.join(ROOT_DIR, "data/st_database2/MDD_{}_478.csv".format(feature)))
        idx = np.load(os.path.join(ROOT_DIR, "model/idx_{}.npy".format(feature)))

        idx_num = [0, 1, 2, 3, 4]
        print(idx[idx_num[0]], idx[idx_num[1]], idx[idx_num[2]], idx[idx_num[3]], idx[idx_num[4]])
        temp_data = [result[idx[i]] for i in idx_num]
        mean_mdd = [mdd[str(idx[i])][0] for i in idx_num]
        mean_hc = [hc[str(idx[i])][0] for i in idx_num]
        mean = [(mean_mdd[i] + mean_hc[i]) / 2 for i in range(len(temp_data))]
        distance = [abs(mean[i] - mean_mdd[i]) for i in range(len(temp_data))]
        xarr = [(temp_data[i] - mean[i]) / (distance[i] / 1.5) if mean_mdd[i] < mean_hc[i] else -(
                    temp_data[i] - mean[i]) / (distance[i] / 2) for i in range(len(temp_data))]
        xarr = np.array(xarr)
        print(xarr)
        xarr = np.clip(xarr, 0.2, 5.8)

        Y = [1,2,3,4,5]
        plt.figure(figsize=(10, 6))
        plt.xlim(0, 6)
        plt.ylim(0, 6)
        bar = plt.barh(Y, 6, height=0.7, align='center', alpha=0.8)
        self.gradientbars(bar)
        plt.scatter(xarr, Y, s=300, color='k', alpha=1, marker="d", )
        plt.axis('off')
        plt.savefig("{}/feature_detail_{}.png".format(self.dir, feature), bbox_inches='tight', pad_inches=0)
        plt.close()

    def position_plot(self, result_psd, result_fc, result_ni):
        with open('{}/bwave_19_reg_4sec_plv/feature.pickle'.format(ROOT_DIR), 'rb') as f:
            df = pickle.load(f)

        y_data = df['target'].to_numpy()
        x_data = [np.vstack(df['psd'].to_numpy())[:, np.load(os.path.join(ROOT_DIR, "model/idx_{}.npy".format('psd')))],
                  np.vstack(df['fc'].to_numpy())[:, np.load(os.path.join(ROOT_DIR, "model/idx_{}.npy".format('fc')))],
                  np.vstack(df['ni'].to_numpy())[:, np.load(os.path.join(ROOT_DIR, "model/idx_{}.npy".format('ni')))]]

        x_mdd = x_data[np.argmax(self.values[:3])][y_data == 1]
        x_hc = x_data[np.argmax(self.values[:3])][y_data == 0]

        y_hc = np.mean(x_hc[:, 0], axis=0)
        y_mdd = np.mean(x_mdd[:, 0], axis=0)
        dist = abs(y_hc - y_mdd) / 7
        center = max(y_hc, y_mdd) - dist * 3.5

        for i in range(3):
            fig, ax = plt.subplots(figsize=(14, 3))
            ax.set_xlim(0, 10)
            ax.set_ylim(0, 10)
            image_path = os.path.join(ROOT_DIR, "plot_image/base_F_bar.png")
            image_arr = np.array(plt.imread(image_path))
            imagebox = OffsetImage(image_arr, zoom=1.02)
            ab = AnnotationBbox(imagebox, (0, 2), bboxprops={'edgecolor': 'none', 'alpha': 1}, box_alignment=(0, 0))
            ax.add_artist(ab)
            ax.spines['bottom'].set_visible(False)
            ax.spines['left'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['top'].set_visible(False)
            plt.draw()
            result_data = [result_psd, result_fc, result_ni]
            best_model_idx = np.argmax(self.values[:3])
            y_temp = result_data[best_model_idx][0, i]
            temp_dist = 5 - (y_temp - center) * 1 / dist
            if temp_dist > 10:
                temp_dist = 9.5
            if temp_dist < 0:
                temp_dist = 0.5
            ax.scatter(temp_dist, 1.2, marker="^", s=600, color='yellow', edgecolors='black',
                        linewidth=0.7)
            plt.gca().axes.yaxis.set_ticks([])
            plt.gca().axes.xaxis.set_ticks([])
            fig.figure.savefig("{}/position_plot_{}.png".format(self.dir, i), bbox_inches='tight')
            # plt.show()
            plt.close()

    def test(self):
        ## new data preprocess & feature extraction
        print(ROOT_DIR)
        file_path = self.file

        ##sensor----------------------------------------------------
        raw_file = bd()
        raw_file.load_file(file_path)
        raw_file.preprocess()

        raw_file.PSD()
        raw_file.FC()
        raw_file.NI()

        clf_psd, result_psd = self.prepare("psd", raw_file.psd)
        clf_fc, result_fc = self.prepare("fc", raw_file.fc_f)
        clf_ni, result_ni = self.prepare("ni", raw_file.ni)

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

        ## tr probabilty 표시
        self.tr_probabilty(raw_file.psd, raw_file.fc_f, raw_file.ni)

        ## positin plot ---------------------------
        # self.position_plot(result_psd, result_fc, result_ni)

        self.pred_n_plot()

        self.psd_plot(raw_file.psd[0], "rel")
        self.psd_plot(raw_file.psd_abs[0], "abs")
        self.psd_fre(raw_file.psd_hz[0], "rel")
        self.psd_fre(raw_file.psd_hz_abs[0], "abs")
        self.fc_plot(raw_file.fc_f[0])
        self.ni_plot(raw_file.ni[0][28:])

        self.main_detail(raw_file.psd[0], "psd", 0, 3)
        self.main_detail(raw_file.psd[0], "ni", 3, 6)
        self.main_detail_fc(raw_file.fc_f[0])

        self.feature_detail(raw_file.psd[0], "psd")
        self.feature_detail(raw_file.fc_f[0], "fc")
        self.feature_detail(raw_file.ni[0], "ni")

        ##JSON
        with open('{}/info.json'.format(self.dir), 'r', encoding='utf-8') as make_file: #읽고
            data = json.load(make_file)
            data['y_pred'] = self.y_pred
            data['y_pred_proba_mdd'] = self.y_pred_proba_mdd
            data['y_pred_proba_hc'] = self.y_pred_proba_hc
            data['best_model'] = self.best_model
            data['tr_proba'] = self.tr_proba
            data['psd_sensor'] = clf_psd.predict_proba(result_psd)[0][1]
            data['fc_sensor'] = clf_fc.predict_proba(result_fc)[0][1]
            data['ni_sensor'] = clf_ni.predict_proba(result_ni)[0][1]
            data['psd_infl_band'] = self.psd_infl_band
            data['fc_infl_band'] = self.fc_infl_band
            data['ni_infl_band'] = self.ni_infl_band
            ## 임의로 설정
            data['psd_source'] = 0.582396
            data['fc_source'] = 0.6839863
            data['ni_source'] = 0.6232363

        with open('{}/info.json'.format(self.dir), 'w', encoding='utf-8') as make_file: #쓰기
            json.dump(data, make_file, ensure_ascii=False, indent='\t')


