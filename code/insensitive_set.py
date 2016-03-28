import pandas as pd
import numpy as np 
from basic_set import get_basic

#def get_spread_midprice(sample_df):
#	spread_names=[]
#	midprice_names=[]
#	bid_price_names=[]
#	ask_price_names=[]
#	for i in range(1,11):
#		spread_names.append("bid-ask_spread"+str(i))
#		midprice_names.append("mid-price_spread"+str(i))
#		bid_price_names.append("bid_price"+str(i))
#		ask_price_names.append('ask_price'+str(i))
#	raw_spread=pd.DataFrame(np.asarray(sample_df[ask_price_names])-np.asarray(sample_df[bid_price_names]))
#	raw_mid=pd.DataFrame((np.asarray(sample_df[ask_price_names])+np.asarray(sample_df[bid_price_names]))/2)
#	raw_spread.columns=spread_names
#	raw_mid.columns=midprice_names
#	spread_mid=pd.concat([sample_df[['Index','Time']],raw_spread,raw_mid],axis=1)
#	return(spread_mid)


##
def get_spread_midprice(sample_df):
    spread_names=[]
    midprice_names=[]
    bid_price_names=[]
    ask_price_names=[]
    for i in range(1,11):
        spread_names.append("bid-ask_spread"+str(i))
        midprice_names.append("mid-price_spread"+str(i))
        bid_price_names.append("bid_price"+str(i))
        ask_price_names.append('ask_price'+str(i))
    raw_spread=pd.DataFrame(np.asarray(sample_df[ask_price_names])-np.asarray(sample_df[bid_price_names]))
    raw_mid=pd.DataFrame((np.asarray(sample_df[ask_price_names])+np.asarray(sample_df[bid_price_names]))/2)
    raw_spread.columns=spread_names
    raw_mid.columns=midprice_names
    index_time = sample_df[['Index','Time']]
    raw_spread.index = index_time.index
    raw_mid.index = index_time.index
    spread_mid=pd.concat([index_time,raw_spread,raw_mid],axis=1)
    return(spread_mid)
#
#
def get_price_diff(sample_df):
    
    ask_diff = sample_df.ask_price10 - sample_df.ask_price1
    bid_diff = sample_df.bid_price1 - sample_df.bid_price10
    
    ask_abs_diff_cols = ["ask_price"+str(i) for i in range(1,11)]
    ask_abs_diff = pd.DataFrame(np.abs(np.asarray(sample_df[ask_abs_diff_cols[1:]]) - np.asarray(sample_df[ask_abs_diff_cols[:9]])))
    bid_abs_diff_cols = ["bid_price"+str(i) for i in range(1,11)]
    bid_abs_diff = pd.DataFrame(np.abs(np.asarray(sample_df[bid_abs_diff_cols[1:]]) - np.asarray(sample_df[bid_abs_diff_cols[:9]])))
    index_time = sample_df[['Index','Time']]
    ask_diff.index = index_time.index
    bid_diff.index = index_time.index
    ask_abs_diff.index = index_time.index
    bid_abs_diff.index = index_time.index
    result = pd.concat([index_time, ask_diff, bid_diff, ask_abs_diff, bid_abs_diff], axis = 1)
    colnames = ["Index", "Time", "ask_diff", "bid_diff"] + ["ask_abs"+str(i)+"_"+str(i-1) for i in range(2,11)] + ["bid_abs"+str(i)+"_"+str(i-1) for i in range(2,11)]
    result.columns = colnames
    return(result)

##
def get_mean(sample_df):
    bid_price_names=[]
    bid_size_names=[]
    ask_price_names=[]
    ask_size_names=[]
    for i in range(1,11):
        bid_price_names.append("bid_price"+str(i))
        bid_size_names.append('bid_size'+str(i))
        ask_price_names.append('ask_price'+str(i))
        ask_size_names.append("ask_size"+str(i))
    mean_ask=pd.DataFrame(np.mean(np.asarray(sample_df[ask_price_names]),axis=1))
    mean_bid=pd.DataFrame(np.mean(np.asarray(sample_df[bid_price_names]),axis=1))
    mean_ask_vol=pd.DataFrame(np.mean(np.asarray(sample_df[ask_size_names]),axis=1))
    mean_bid_vol=pd.DataFrame(np.mean(np.asarray(sample_df[bid_size_names]),axis=1))
    index_time = sample_df[['Index','Time']]
    mean_ask.index = index_time.index
    mean_bid.index = index_time.index
    mean_ask_vol.index = index_time.index
    mean_bid_vol.index = index_time.index
    mean_price_vol=pd.concat([index_time,mean_ask,mean_bid,mean_ask_vol,mean_bid_vol],axis=1)
    mean_price_vol.columns=['Index','Time','mean_ask_price','mean_bid_price','mean_ask_vol','mean_bid_vol']
    return(mean_price_vol)

##
def get_accumulated_diff(sample_df):
    ask_price_cols = ["ask_price"+str(i) for i in range(1,11)]
    bid_price_cols = ["bid_price"+str(i) for i in range(1,11)]
    ask_size_cols = ["ask_size"+str(i) for i in range(1,11)]
    bid_size_cols = ["bid_size"+str(i) for i in range(1,11)]
    ask_price_mat = np.asarray(sample_df[ask_price_cols])
    bid_price_mat = np.asarray(sample_df[bid_price_cols])
    ask_size_mat = np.asarray(sample_df[ask_size_cols])
    bid_size_mat = np.asarray(sample_df[bid_size_cols])
    price_accumulated_diff = pd.DataFrame(np.sum(ask_price_mat - bid_price_mat, axis = 1))
    size_accumulated_diff = pd.DataFrame(np.sum(ask_size_mat - bid_size_mat, axis = 1))
    index_time = sample_df[['Index','Time']]
    price_accumulated_diff.index = index_time.index
    size_accumulated_diff.index = index_time.index
    result = pd.concat([index_time, price_accumulated_diff, size_accumulated_diff], axis = 1)
    cols = ["Index", "Time", "price_accumulated_diff", "size_accumulated_diff"]
    result.columns = cols
    return(result)
