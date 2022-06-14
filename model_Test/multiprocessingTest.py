from model_Test.BwaveData import BwaveData as bd
from multiprocessing import Pool

file_path = 'C:/Users/Bwave/Desktop/bwave_pro_data/bwave/MDD/0015690.cnt'

raw_file = bd()
raw_file.load_file(file_path)
raw_file.preprocess()

raw_file.FC()
result_fc = raw_file.fc_f

print(result_fc)

