import os
import datetime
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_DIR = os.path.join(ROOT_DIR, 'bwave_pro_data.xlsx')
ROOT_DIR_con = "/".join(ROOT_DIR.split("\\"))


#now = datetime.datetime.now()
#dNt = '{}.{}-{}.{}'.format(now.month, now.day, now.hour,now.minute)
#TRAIN_DIR = ROOT_DIR + '/train/{dnt}'.format(dnt=dNt)
#TEST_FUNC_DIR = ROOT_DIR + "/tests/tests_functions"
FUNCDATA_DIR = os.path.join(ROOT_DIR, 'data')
#PERFORMANCE_DIR = ROOT_DIR +'/performance_test'
#PERFORMANCE_WORK_DIR = PERFORMANCE_DIR + '/{dnt}'.format(dnt=dNt)


FREQ_BANDS = {'delta': [1, 4],
              'theta': [4, 8],
              'low-alpha': [8, 10],
              'high-alpha': [10, 12],
              'low-beta': [12, 22],
              'high-beta': [22, 30],
              'gamma': [30, 55]}

ch_detect = {'Fp1': ['Fp2', 'F7', 'F3', 'Fz'],
             'Fp2': ['Fp1', 'F8', 'F4', 'Fz'],
             'F7': ['Fp1', 'F3', 'T7', 'C3'],
             'F3': ['Fz', 'F7', 'Fp1', 'C3'],
             'Fz': ['F3', 'F4', 'Cz', 'Fp1'],
             'F4': ['F8', 'Fz', 'Fp2', 'C4'],
             'F8': ['T8', 'F4', 'Fp2', 'C4'],
             'T7': ['P7', 'F7', 'C3', 'F3'],
             'C3': ['F3', 'P3', 'T7', 'Cz'],
             'Cz': ['Pz', 'C4', 'Fz', 'C3'],
             'C4': ['P4', 'F4', 'T8', 'Cz'],
             'T8': ['F8', 'P8', 'C4', 'F4'],
             'P7': ['T7', 'O1', 'P3', 'C3'],
             'P3': ['Pz', 'O1', 'P7', 'C3'],
             'Pz': ['P3', 'P4', 'Cz', 'O2'],
             'P4': ['P8', 'Pz', 'O2', 'C4'],
             'P8': ['O2', 'T8', 'P4', 'C4'],
             'O1': ['P7', 'O2', 'P3', 'Pz'],
             'O2': ['P8', 'O1', 'P4', 'Pz']}

ch_detect_62 = {'Fp1': ['AF3', 'Fpz', 'F5', 'Fp2'],
 'Fpz': ['Fp2', 'Fp1', 'AF3', 'AF4'],
 'Fp2': ['Fpz', 'AF4', 'F6', 'Fp1'],
 'AF3': ['Fp1', 'F3', 'Fpz', 'F5'],
 'AF4': ['Fp2', 'F4', 'F6', 'Fpz'],
 'F7': ['F5', 'FT7', 'FC5', 'Fp1'],
 'F5': ['F7', 'F3', 'FC5', 'AF3'],
 'F3': ['F1', 'F5', 'FC3', 'AF3'],
 'F1': ['F3', 'Fz', 'FC1', 'AF3'],
 'Fz': ['F1', 'F2', 'FCz', 'FC2'],
 'F2': ['F4', 'Fz', 'FC2', 'AF4'],
 'F4': ['F6', 'F2', 'FC4', 'AF4'],
 'F6': ['F8', 'F4', 'FC6', 'AF4'],
 'F8': ['F6', 'FT8', 'FC6', 'T8'],
 'FT7': ['F7', 'T7', 'FC5', 'F5'],
 'FC5': ['F5', 'C5', 'FC3', 'FT7'],
 'FC3': ['F3', 'FC5', 'FC1', 'C3'],
 'FC1': ['FCz', 'FC3', 'F1', 'C1'],
 'FCz': ['FC1', 'FC2', 'Fz', 'Cz'],
 'FC2': ['FCz', 'F2', 'FC4', 'C2'],
 'FC4': ['F4', 'FC6', 'C4', 'FC2'],
 'FC6': ['C6', 'F6', 'FT8', 'FC4'],
 'FT8': ['T8', 'F8', 'FC6', 'F6'],
 'T7': ['TP7', 'FT7', 'C5', 'FC5'],
 'C5': ['CP5', 'FC5', 'T7', 'C3'],
 'C3': ['CP3', 'FC3', 'C5', 'C1'],
 'C1': ['FC1', 'CP1', 'Cz', 'C3'],
 'Cz': ['C1', 'C2', 'CPz', 'FCz'],
 'C2': ['CP2', 'FC2', 'C4', 'Cz'],
 'C4': ['CP4', 'FC4', 'C6', 'C2'],
 'C6': ['CP6', 'FC6', 'T8', 'C4'],
 'T8': ['FT8', 'TP8', 'C6', 'FC6'],
 'TP7': ['T7', 'P7', 'CP5', 'C5'],
 'CP5': ['C5', 'P5', 'TP7', 'CP3'],
 'CP3': ['P3', 'C3', 'CP1', 'CP5'],
 'CP1': ['CPz', 'P1', 'C1', 'CP3'],
 'CPz': ['CP1', 'Pz', 'Cz', 'CP2'],
 'CP2': ['P2', 'C2', 'CP4', 'CPz'],
 'CP4': ['P4', 'C4', 'CP6', 'CP2'],
 'CP6': ['C6', 'P6', 'TP8', 'CP4'],
 'TP8': ['P8', 'T8', 'CP6', 'C6'],
 'P7': ['PO7', 'TP7', 'P5', 'PO5'],
 'P5': ['PO5', 'P7', 'P3', 'CP5'],
 'P3': ['P1', 'P5', 'PO3', 'CP3'],
 'P1': ['Pz', 'P3', 'CP1', 'POz'],
 'Pz': ['P1', 'P2', 'CPz', 'POz'],
 'P2': ['P4', 'Pz', 'CP2', 'PO4'],
 'P4': ['P2', 'P6', 'CP4', 'PO4'],
 'P6': ['PO6', 'P8', 'P4', 'CP6'],
 'P8': ['PO8', 'TP8', 'P6', 'PO6'],
 'PO7': ['PO5', 'P7', 'O1', 'P5'],
 'PO5': ['PO7', 'PO3', 'O1', 'P5'],
 'PO3': ['PO5', 'O1', 'P3', 'PO7'],
 'POz': ['Oz', 'Pz', 'PO3', 'PO4'],
 'PO4': ['PO6', 'O2', 'P4', 'PO8'],
 'PO6': ['PO8', 'PO4', 'O2', 'P6'],
 'PO8': ['PO6', 'P8', 'O2', 'P6'],
 'CB1': ['O1', 'PO7', 'Oz', 'PO5'],
 'O1': ['PO5', 'PO7', 'Oz', 'PO3'],
 'Oz': ['O1', 'O2', 'POz', 'PO4'],
 'O2': ['PO6', 'PO8', 'Oz', 'PO4'],
 'CB2': ['O2', 'PO8', 'Oz', 'PO6']}

odd_arr = ['0025834.cnt', '0041292.cnt', '0049931.cnt', '0055522.cnt', '0078031.cnt', '0087486.cnt', '0144645.cnt', '0153443.cnt', '0165295.cnt', '0263403.cnt', '0275574.cnt', '0315729.cnt', '0351449.cnt', '0372242.cnt', '0375161.cnt', '0392870.cnt', '0422433.cnt', '0427597.cnt', '0452987.cnt', '0454480.cnt', '0464629.cnt', '0502977.cnt', '0526991.cnt', '0547810.cnt', '0589266.cnt', '0644644.cnt', '0645938_2.cnt', '0653597.cnt', '0663059.cnt', '0665524.cnt', '0686050.cnt', '0689241.cnt', '0690171.cnt', '0701418.cnt', '0707644.cnt', '0711899.cnt', '0717405.cnt', '0722281.cnt', '0725260.cnt', '0728532.cnt', '0731647.cnt', '0731701.cnt', '0732172.cnt', '0733667.cnt', '0734080.cnt', '0735297.cnt', '0737127.cnt', '0743215.cnt', '0746682_1.cnt', '0749666_1.cnt', '0749738.cnt', '0755138.cnt', '0755758.cnt', '0756488.cnt', '0759318.cnt', '0761105.cnt', '0769442.cnt', '0771450.cnt', '0771505.cnt', '0773831.cnt', '0774364.cnt', '0779781.cnt', '0783441.cnt', '0784839.cnt', '0791634.cnt', '0792470.cnt', '0794496.cnt', '0795393.cnt', '0795496.cnt', '0796550.cnt', '0798209.cnt', '0807671.cnt', '0807836.cnt', '0808972.cnt', '0812818.cnt', '0813782.cnt', '0819599.cnt', '0823669.cnt', '0040910.cnt']
