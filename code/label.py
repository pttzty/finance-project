import numpy as np
import pandas as pd

def create_label(data, delta_t, ticksize=0.01):
    '''
    input: data frame
    out: data frame
    '''
    # create mid-price label
    mid_price = (data['ask_price1']+data['bid_price1'])/2
    # shifted mid_price
    mid_shift = np.append(mid_price[delta_t:], np.array(np.nan).repeat(delta_t))
    
    # Determine up or down
    mid = (mid_shift > mid_price + ticksize)*1 + (mid_shift < mid_price - ticksize)*-1
    mid = mid.astype('float')
    mid[-delta_t:] = np.nan
    
    # Change pandas series and transform to categorical data
    mid = pd.Series(pd.Categorical(mid, categories=[-1, 0, 1]))

    # Change label
    mid.cat.categories = ['down', 'stationary', 'up']
    
    data['mid_label'] = mid
    
    # create spread-crossing label
    bid = data['bid_price1']
    ask = data['ask_price1']
    # shifted bid (append nan at the last)
    bid_shift = np.append(bid[delta_t:], np.array(np.nan).repeat(delta_t))
    ask_shift = np.append(ask[delta_t:], np.array(np.nan).repeat(delta_t))
    
    # Determine up or down
    spread = (bid_shift > ask)*1 + (ask_shift < bid)*-1
    spread = spread.astype('float')
    spread[-delta_t:] = np.nan
    
    # Change pandas series and transform to categorical data
    spread = pd.Series(pd.Categorical(spread, categories=[-1, 0, 1]))

    # Change label
    spread.cat.categories = ['down', 'stationary', 'up']
    
    data['spread_label'] = spread
    data = data.dropna(how='any')
    
    return(data)
