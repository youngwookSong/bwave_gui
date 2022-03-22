from scipy import signal
import time
import networkx as nx
import scipy.io
from model_Test.directory import FREQ_BANDS, FUNCDATA_DIR, ch_detect, ch_detect_62
from model_Test.helper_functions import *
from sklearn.decomposition import PCA
from joblib import Parallel, delayed
import itertools


class BwaveData:

    def __init__(self):
        self.samplefreq = 1000
        self.raw = None
        self.epoch_old = None
        self.epoch_num = None
        self.prep_epochs = None
        self.psd = None
        self.fc = None
        self.fc_f = None
        self.ni = None
        self.source = None
        self.s_psd = None
        self.s_fc = None
        self.s_fc_f = None
        self.s_ni = None
        self.kol = None
        self.crop_time = None
        self.crop_cri = None

    # def bad_ch(self, raw):

    def load_file(self, file_dir):
        root, self.extension = os.path.splitext(file_dir)
        _, filename = os.path.split(file_dir)
        print(filename)

        # TODO: change to logger
        # print(filename)

        if self.extension in ['.cnt', '.cdt']:
            self.samplefreq = 1000
            if self.extension == '.cnt':
                raw = mne.io.read_raw_cnt(file_dir, preload=True, verbose=False, data_format='int32')
            if self.extension == '.cdt':
                raw = mne.io.read_raw_curry(file_dir, preload=True, verbose=False)
            to_EOG_channels(raw)

            raw = raw.pick_channels(['FP1', 'FPZ', 'FP2', 'AF3', 'AF4', 'F7', 'F5', 'F3', 'F1', 'FZ',
                                     'F2', 'F4', 'F6', 'F8', 'FT7', 'FC5', 'FC3', 'FC1', 'FCZ', 'FC2', 'FC4',
                                     'FC6', 'FT8', 'T7', 'C5', 'C3', 'C1', 'CZ', 'C2', 'C4', 'C6', 'T8',
                                     'TP7', 'CP5', 'CP3', 'CP1', 'CPZ', 'CP2', 'CP4', 'CP6', 'TP8',
                                     'P7', 'P5', 'P3', 'P1', 'PZ', 'P2', 'P4', 'P6', 'P8', 'PO7',
                                     'PO5', 'PO3', 'POZ', 'PO4', 'PO6', 'PO8', 'CB1', 'O1', 'OZ', 'O2', 'CB2',
                                     "VEO", 'HEO'], ordered=True)

            raw.set_channel_types({'VEO': 'eog', 'HEO': 'eog'})

            # 19채널로 돌리면 이거 주석처리하기
            montage = mne.channels.read_custom_montage(os.path.join(FUNCDATA_DIR, 'channel_neuroscan_rev2_m.xyz'))
            raw.set_montage(montage)

            # raw = raw.pick_channels(['FP1', 'FP2', 'F7', 'F3', 'FZ', 'F4', 'F8', 'T7', 'C3', 'CZ', 'C4', 'T8',
            #                          'P7', 'P3', 'PZ', 'P4', 'P8', 'O1', 'O2', 'VEO', 'HEO'], ordered=True)

            new_names = dict((ch_name, ch_name.rstrip('.').upper().replace('Z', 'z').replace('FP', 'Fp')) for ch_name in
                             raw.ch_names)
            raw.rename_channels(new_names)

        elif self.extension == '.mat':
            self.samplefreq = 1000
            raw_mat = scipy.io.loadmat(file_dir)['data'] * 1e-6
            info = mne.create_info(
                ['FP1', 'FPZ', 'FP2', 'AF3', 'AF4', 'F7', 'F5', 'F3', 'F1', 'FZ', 'F2', 'F4', 'F6', 'F8', 'FT7', 'FC5',
                 'FC3', 'FC1', 'FCZ', 'FC2', 'FC4', 'FC6', 'FT8', 'T7', 'C5', 'C3', 'C1', 'CZ', 'C2', 'C4', 'C6', 'T8',
                 'TP7', 'CP5', 'CP3', 'CP1', 'CPZ', 'CP2', 'CP4', 'CP6', 'TP8', 'P7', 'P5', 'P3', 'P1', 'PZ', 'P2',
                 'P4', 'P6', 'P8', 'PO7', 'PO5', 'PO3', 'POZ', 'PO4', 'PO6', 'PO8', 'CB1', 'O1', 'OZ', 'O2', 'CB2'],
                1000, ch_types='eeg', )
            raw = mne.io.RawArray(raw_mat, info, verbose=False)

        elif self.extension == '.mff':
            self.samplefreq = 1000
            raw = mne.io.read_raw_egi(file_dir, preload=True, verbose=False)

            raw_rename_val = raw.info['ch_names']
            raw_rename_key = ['F10', 'AF4', 'F2', 'FCZ', 'FP2', 'FZ', 'FC1', 'AFZ', 'F1', 'FP1', 'AF3', 'F3', 'F5',
                              'FC5',
                              'FC3', 'C1', 'F9', 'F7', 'FT7', 'C3', 'CP1', 'C5', 'T9', 'T7', 'TP7', 'CP5', 'P5', 'P3',
                              'TP9', 'P7', 'P1', 'P9', 'PO3', 'PZ', 'O1', 'POZ', 'OZ', 'PO4', 'O2', 'P2', 'CP2', 'P4',
                              'P10', 'P8', 'P6', 'CP6', 'TP10', 'TP8', 'C6', 'C4', 'C2', 'T8', 'FC4', 'FC2', 'T10',
                              'FT8', 'FC6', 'F8', 'F6', 'F4', 'EOGR', 'EOGVR', 'EOGVL', 'EOGL', 'CZ', ]

            raw_rename = dict(zip(raw_rename_val, raw_rename_key))
            raw.rename_channels(raw_rename)
            raw.set_channel_types({'EOGR': 'eog', 'EOGVR': 'eog', 'EOGVL': 'eog', 'EOGL': 'eog'})

            to_EOG_channels_egi(raw)
            # raw = raw.pick_channels(['FP1', 'FP2', 'F7', 'F3', 'FZ', 'F4', 'F8', 'T7', 'C3', 'CZ', 'C4', 'T8',
            #                          'P7', 'P3', 'PZ', 'P4', 'P8', 'O1', 'O2', 'VEO', 'HEO'], ordered=True)

            # egi2neuro(raw) #TODO : interpolation : 여기 있으면 안됨, 위치 옮겨야댐

            new_names = dict((ch_name, ch_name.rstrip('.').upper().replace('Z', 'z').replace('FP', 'Fp')) for ch_name in
                             raw.ch_names)
            raw.rename_channels(new_names)

        raw = raw.notch_filter(freqs=np.arange(60, 241, 60))

        self.raw = raw

    def bad_ch(self, raw):
        # 상관관계 분석 알고리즘
        for key in ch_detect:
            # print("---------------", key)
            raw_dat = raw.get_data(picks=key)
            raw_dat_corr = raw.get_data(picks=ch_detect[key])
            # print("추출된 데이터 {}".format(ch_detect[key]))

            raw_dat_corr_med = np.median(raw_dat_corr, axis=0)

            corr = np.corrcoef(raw_dat, raw_dat_corr_med)[0, 1]
            # print(corr, "\n")

            # handling
            if corr < 0.2:
                raw.info['bads'].append(key)

        print("bad_ch: ", raw.info['bads'])

        # 채널을 아예 지워버리자
        for i in raw.info['bads']:
            raw.info['ch_names'].remove(i)

        print(raw.get_data().shape)
        return raw

    def preprocess(self, show=False):
        start = time.time()

        # TODO: convert to logger

        # Remove EOG
        # ssp method
        print('ssp')
        eog_projs, _ = mne.preprocessing.compute_proj_eog(self.raw, no_proj=True, n_eeg=1, eog_l_freq=0, eog_h_freq=55,
                                                          verbose=show)
        raw_clean = self.raw.add_proj(eog_projs)

        # reg method
        # print('reg')
        # epochs = mne.make_fixed_length_epochs(self.raw, duration=5, preload=True, verbose=False)
        # _, betas = mne.preprocessing.regress_artifact(epochs.copy().subtract_evoked(), verbose=False)
        # raw_clean, _ = mne.preprocessing.regress_artifact(self.raw, betas=betas, verbose=False)

        # Filtering
        filtered = raw_clean.filter(1, 55, n_jobs=1, verbose=show, method='iir')

        # bad ch detect
        # raw = self.bad_ch(self.raw)
        # print(raw.info)

        # CAR
        filtered = filtered.set_eeg_reference('average',
                                              projection=True)  # CAR (eog 제외, eeg채널들의 평균만 제외)

        # Epoch
        prep_epochs = mne.make_fixed_length_epochs(filtered, duration=5, preload=False, verbose=show).load_data()
        prep_epochs = prep_epochs.pick_types(eeg=True, verbose=show)
        prep_epochs = prep_epochs.apply_baseline((None, None))

        # Global Threshold
        epoch_dat = prep_epochs.get_data()
        epoch_no, _, _ = epoch_dat.shape
        e_index = [e for e in range(epoch_no) if
                   epoch_dat[e, :, :].max() > 100e-6 or epoch_dat[e, :, :].min() < -100e-6]  # *1e-6: uV단위 맞추기 위해
        # e_index에 중복된 값이 존재해도 상관 없는 것으로 보임
        prep_epochs.drop(e_index, verbose=show)

        # Individual Threshold
        epoch_dat = prep_epochs.get_data()
        bad_t_index = []  # raw값
        for p in range(epoch_dat[0, :, 0].shape[0]):
            maxt = np.max(abs(epoch_dat[:, p]), axis=1)
            for q in range(len(maxt)):
                # TODO: STD 범위 다시검증
                threshold = np.mean(maxt) + 5 * np.std(maxt)
                if maxt[q] > threshold:
                    bad_t_index.append(q)

        bad_t_d_index = []  # 차분값
        for p in range(epoch_dat[0, :, 0].shape[0]):
            maxt_d = np.max(abs(np.diff(epoch_dat[:, p])), axis=1)
            for q in range(len(maxt_d)):
                threshold = np.mean(maxt_d) + 5 * np.std(maxt_d)
                if maxt_d[q] > threshold:
                    bad_t_d_index.append(q)
        bad_e_index = bad_t_index + bad_t_d_index
        bad_e_index = sorted(list(set(bad_e_index)))
        prep_epochs.drop(bad_e_index, verbose=False)

        # 19ch selection
        prep_epochs = prep_epochs.pick_channels(
            ['Fp1', 'Fp2', 'F7', 'F3', 'Fz', 'F4', 'F8', 'T7', 'C3', 'Cz', 'C4', 'T8',
             'P7', 'P3', 'Pz', 'P4', 'P8', 'O1', 'O2'], ordered=True)

        # epoch 개수 저장
        self.epoch_num = prep_epochs.get_data().shape[0]
        self.epoch_old = epoch_no
        sec = time.time() - start

        prep_epochs = prep_epochs.pick_channels(
            ['Fp1', 'Fp2', 'F7', 'F3', 'Fz', 'F4', 'F8', 'T7', 'C3', 'Cz', 'C4', 'T8',
             'P7', 'P3', 'Pz', 'P4', 'P8', 'O1', 'O2'], ordered=True)

        # TODO: convert to logger
        print("Preprocessing :", int(sec), 'sec /', "epochs {} --> {}".format(epoch_no, self.epoch_num))
        self.prep_epochs = prep_epochs
        return prep_epochs

    def source_loc(self):
        # TODO : source 하기전 CAR 해야댐 -> 전체 RAW DATA - 전체 RAW DATA의 MEAN()
        print("Source :", end=" ", flush=True)
        start = time.time()
        prep_epochs = self.prep_epochs.get_data()

        imgker, vox_index = inverse_loader(self.extension)

        epoch_no, sen_no, sen_dat = prep_epochs.shape
        source_no = vox_index.shape

        source_roi = np.array([])
        img = []

        for i in range(source_no[0]):
            ik = np.array([imgker[k] for k in vox_index[i][0]])
            img.append(ik)
        for i in range(epoch_no):  # concat -1
            pca_mat = np.array([])
            for j in range(source_no[0]):
                voxels = np.dot(img[j], prep_epochs[i, :, :]).transpose()
                pca = PCA(n_components=1)  # err optimization 10e-5
                temp = pca.fit_transform(voxels)
                pca_mat = np.hstack((pca_mat, temp)) if pca_mat.size else temp
            source_roi = np.dstack((source_roi, pca_mat)) if source_roi.size else pca_mat

        source_roi = np.swapaxes(source_roi, 0, 2)
        info = mne.create_info(68, self.samplefreq, 'eeg', verbose=False)
        source_roi = mne.EpochsArray(source_roi, info, verbose=False)

        sec = time.time() - start
        print(int(sec), 'sec')
        # (epochs,sensors,time)
        self.source = source_roi
        return source_roi

    def PSD(self, source=False, show=False):
        print("PSD :", end=" ", flush=True)
        start = time.time()
        samplefreq = self.samplefreq

        arr = self.source if self.source else self.prep_epochs

        # basic
        psds, freqs = mne.time_frequency.psd_welch(arr, fmin=1., fmax=55., n_fft=5 * samplefreq, verbose=show, n_jobs=1)

        # hanning window
        # n = 3 * self.samplefreq
        # psds, freqs = mne.time_frequency.psd_welch(arr, fmin=1., fmax=55., n_fft=5 * self.samplefreq, verbose=show,
        #                                             n_jobs=1, n_overlap=n * 0.25, n_per_seg=n,
        #                                             window=signal.windows.hann(n))  # hann window

        # log
        psds = np.log10(1 + (1e12 * psds))

        # normalization
        psds /= np.sum(psds, axis=-1, keepdims=True)  # (epochs, sensors, freq)

        psds = psds.mean(axis=0)
        X = []
        for fmin, fmax in FREQ_BANDS.values():
            psds_band = psds[:, (freqs >= fmin) & (freqs < fmax)].sum(axis=1)
            X.append(psds_band)
        psd_mat_7band_av = np.concatenate(X)
        sec = time.time() - start
        print(int(sec), 'sec')
        if self.source:
            self.s_psd = psd_mat_7band_av.reshape(1, -1)  # [band0, band1, band2, ...]
        else:
            self.psd = psd_mat_7band_av.reshape(1, -1)  # [band0, band1, band2, ...]
        return psd_mat_7band_av.reshape(1, -1)  # (channels * 7)

    # plv
    def calcul(self, plvs, epoc_dat, c1, c2):
        x1_ht = epoc_dat[:, c1, :]
        x2_ht = epoc_dat[:, c2, :]
        phase1 = np.unwrap(np.angle(x1_ht))
        phase2 = np.unwrap(np.angle(x2_ht))
        complex_phase_diff = np.exp(complex(0, 1) * (phase1 - phase2))
        plv = np.mean(np.abs(np.sum(complex_phase_diff / phase1.shape[1], axis=1)))
        plvs[c1, c2] = plv
        return plvs

    def phase_locking_value(self, filtered, sens_comb):
        h_filtered = filtered.apply_hilbert()
        epoc_dat = h_filtered.get_data()
        # print("calcul start")
        _, sen_no, _ = epoc_dat.shape
        plvs = np.zeros((sen_no, sen_no, 1))
        plvs = Parallel(n_jobs=2)(delayed(self.calcul)(plvs, epoc_dat, c1, c2) for c1, c2 in sens_comb)
        return plvs[0]

    def FC(self, source=False, show=False):
        print("FC :", end=" ", flush=True)
        start = time.time()
        _, sen_no, _ = self.prep_epochs.get_data().shape
        sens_comb = list(itertools.combinations(range(sen_no), 2))

        plv_temp = Parallel(n_jobs=7)(delayed(self.phase_locking_value)(
            self.prep_epochs.copy().filter(int(fmin), int(fmax), n_jobs=1, verbose=False, method='iir'), sens_comb) for
                                      fmin, fmax
                                      in FREQ_BANDS.values())

        # plv_mat = np.concatenate(result, axis=2).swapaxes(0,1)
        plv_mat = np.concatenate(plv_temp, axis=2)
        plv_flatten = np.ravel(plv_mat.swapaxes(0, 1), order='F')
        plv_flatten = plv_flatten[plv_flatten != 0]

        if source:
            self.s_fc_f = plv_flatten.reshape(1, -1)
            self.s_fc = plv_mat
        else:
            self.fc_f = plv_flatten.reshape(1, -1)
            self.fc = plv_mat
        sec = time.time() - start
        print(int(sec), 'sec')
        return plv_mat, plv_flatten.reshape(1, -1)

    # wpli
    # def wrapToPi(self, phi1, phi2):
    #     phi = phi1 - phi2
    #     xwrap = np.remainder(phi, 2 * np.pi)
    #     mask = np.abs(xwrap) > np.pi
    #     xwrap[mask] -= 2 * np.pi * np.sign(xwrap[mask])
    #     return xwrap
    #
    # def wPLI(self, filtered, sens_comb):
    #     h_filtered = filtered.apply_hilbert()
    #     epoc_dat = h_filtered.get_data()
    #     _, sen_no, _ = epoc_dat.shape
    #     wplis = np.zeros((sen_no, sen_no, 1))
    #     for c1, c2 in sens_comb:
    #         x1_ht = epoc_dat[:, c1, :]
    #         x2_ht = epoc_dat[:, c2, :]
    #         phi1 = np.angle(x1_ht)
    #         phi2 = np.angle(x2_ht)
    #         d_phi = self.wrapToPi(phi1, phi2)
    #         wPLI_element = abs(np.mean(d_phi, axis=1)) / np.mean(abs(d_phi), axis=1)
    #         wpli = np.mean(wPLI_element)
    #         if np.isnan(wpli):
    #             wpli = 0
    #         wplis[c1, c2] = wpli
    #     return wplis
    #
    # def FC(self, source=False): #wPLI
    #     print("FC :", end=" ", flush=True)
    #     start = time.time()
    #     arr = self.source if self.source else self.prep_epochs
    #     _, sen_no, _ = arr.get_data().shape
    #     sens_comb = list(itertools.combinations(range(sen_no), 2))
    #
    #     wpli_temp = Parallel(n_jobs=7)(delayed(self.wPLI)(
    #         arr.copy().filter(int(fmin), int(fmax), n_jobs=1, verbose=False, method='iir'), sens_comb) for
    #                                   fmin, fmax in FREQ_BANDS.values())
    #
    #     wpli_mat = np.concatenate(wpli_temp, axis=2)
    #     # wpli_flatten = wpli_mat[wpli_mat != 0]
    #     wpli_flatten = np.ravel(wpli_mat.swapaxes(0, 1), order='F')
    #     wpli_flatten = wpli_flatten[wpli_flatten != 0]
    #
    #     if self.source:
    #         self.s_fc_f = wpli_flatten.reshape(1, -1)
    #         self.s_fc = wpli_mat
    #     else:
    #         self.fc_f = wpli_flatten.reshape(1, -1)
    #         self.fc = wpli_mat
    #     sec = time.time() - start
    #     print(int(sec), 'sec')
    #     return wpli_mat, wpli_flatten.reshape(1, -1)

    def NI(self, source=False):
        print("NI :", end=" ", flush=True)
        start = time.time()

        fc = self.s_fc if self.source else self.fc
        sen_no_x, sen_no_y, freq_band = fc.shape

        # global strength, clustering coef, path length
        g_st_cl_pa = list()
        n_st_cl = list()
        for i in range(freq_band):
            g = nx.convert_matrix.from_numpy_array(fc[:, :, i])
            temp_s = nx.degree(g, weight="weight")

            g_st_cl_pa.append(np.mean(temp_s, axis=0)[1])
            g_st_cl_pa.append(nx.average_clustering(g, weight="weight"))
            g_st_cl_pa.append(nx.average_shortest_path_length(g, weight='weight'))
            # small world network
            swn = nx.average_clustering(g, weight="weight") / nx.average_shortest_path_length(g, weight='weight')
            g_st_cl_pa.append(swn)

            # nodal level strength, clustering coef
            n_st_cl.append(np.array(nx.degree(g, weight="weight"))[:, 1])
            n_st_cl.append(np.array(list(nx.clustering(g, weight="weight").values())))

        ni = np.concatenate((g_st_cl_pa, n_st_cl), axis=None)

        sec = time.time() - start
        print(int(sec), 'sec')
        if self.source:
            self.s_ni = ni.reshape(1, -1)
        else:
            self.ni = ni.reshape(1, -1)
        return ni.reshape(1, -1)

    def kolmogorov_complexity(self, arr):
        mean = arr.mean()
        for i in range(len(arr)):
            if arr[i] >= mean:
                arr[i] = 1
            else:
                arr[i] = 0
        n = len(arr)
        c = 1
        l = 1
        i = 0
        k = 1
        k_max = 1
        stop = 0

        while stop == 0:
            if arr[i + k - 1] != arr[l + k - 1]:
                if k > k_max:
                    k_max = k
                i = i + 1
                if i == l:
                    c = c + 1
                    l = l + k_max
                    if l + 1 > n:
                        stop = 1
                    else:
                        i = 0
                        k = 1
                        k_max = 1
                else:
                    k = 1
            else:
                k = k + 1
                if l + k > n:
                    c = c + 1
                    stop = 1

        b = n / np.log2(n)
        complexity = c / b
        return complexity

    def complexity(self):
        print("Complexity :", end=" ", flush=True)
        start = time.time()
        import antropy as ant
        epoc_dat = self.prep_epochs.get_data()
        _, sen_no, _ = epoc_dat.shape
        comp_mat = []
        print(sen_no)
        for i in range(sen_no):
            arr = epoc_dat[:, i, :]
            temp_comp = []
            for j in range(arr.shape[0]):
                arr_1 = arr[j, :]
                k = ant.sample_entropy(arr_1)
                temp_comp.append(k)
            comp_mat.append(np.mean(temp_comp))
        self.kol = comp_mat
        sec = time.time() - start
        print(int(sec), 'sec')
        print(self.kol)
        return temp_comp
