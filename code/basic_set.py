import pandas as pd
import numpy as np 

## the function takes a panda dataframe as an input, and returns
## another dataframe with all features in the basic set.

def get_basic(sample_df):
	bid_price_names=[]
	bid_size_names=[]
	ask_price_names=[]
	ask_size_names=[]
	for i in range(1,11):
		bid_price_names.append("bid_price"+str(i))
		bid_size_names.append('bid_size'+str(i))
		ask_price_names.append('ask_price'+str(i))
		ask_size_names.append("ask_size"+str(i))
	basic_namelist=['Index','Time']+ask_price_names+ask_size_names+bid_price_names+bid_size_names
	basic_df=sample_df[basic_namelist]
	return(basic_df)
