import numpy as np
import pandas as pd

def get_statistics(data_df, fea_names):
    result_df = data_df[fea_names]
    vol_ratio = np.sum(data_df[["ask_size"+str(i) for i in range(1, 6)]], axis = 1) / np.sum(data_df[["bid_size"+str(i) for i in range(1, 6)]], axis = 1)
    result_df['vol_ratio'] = vol_ratio
    result_df['mid_label'] = data_df['mid_label']
    result_df['spread_label'] = data_df['spread_label']
    return(result_df)