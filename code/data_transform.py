import pandas as pd
import numpy as np
from datetime import datetime
from label import mid_label, spread_label
from basic_set import get_basic
from insensitive_set import get_spread_midprice, get_price_diff, get_mean, get_accumulated_diff
from sampling import sampling_labels

def transform_data_tinsen(data_raw):
    spreads_mids = get_spread_midprice(data_raw)
    price_diff = get_price_diff(data_raw)
    means = get_mean(data_raw)
    accum_diff = get_accumulated_diff(data_raw)
    data_tfm = pd.merge(spreads_mids, price_diff, on = ['Index', 'Time'])
    data_tfm = pd.merge(data_tfm, means, on = ['Index', 'Time'])
    data_tfm = pd.merge(data_tfm, accum_diff, on = ['Index', 'Time'])
    return(data_tfm)


def transform_data(data_raw, feature_basic = True, feature_tinsen = True, feature_tsen = True):
    if feature_basic * feature_tinsen * feature_tsen:
        basics = get_basic(data_raw)
        data_tinsen = transform_data_tinsen(data_raw)
        data_tfm = pd.merge(basics, data_tinsen, on = ['Index', 'Time'])
        return(data_tfm)
    elif (feature_basic == True) and (feature_tinsen == True):
        basics = get_basic(data_raw)
        data_tinsen = transform_data_tinsen(data_raw)
        data_tfm = pd.merge(basics, data_tinsen, on = ['Index', 'Time'])
        return(data_tfm)
    elif (feature_basic == True):
        basics = get_basic(data_raw)
        return(basics)


def split_rawdata(data_raw, split_time = datetime(2012, 5, 22, 11, 0)):
    time = np.array([datetime.strptime(time, "%Y/%m/%d %H:%M:%S.%f") for time in data_raw['Time']])
    train_index = time < datetime(2012, 5, 22, 11, 0)
    train = data_raw.iloc[train_index]
    test = data_raw.iloc[np.logical_not(train_index)]
    return({"train": train, "test": test})
