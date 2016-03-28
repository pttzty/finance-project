import pandas as pd
import numpy as np 
from basic_set import get_basic

def get_derivatives(sample_df,delta_t):
	bid_price_names=[]
	bid_size_names=[]
	ask_price_names=[]
	ask_size_names=[]
	ask_price_derivative_names=[]
	ask_size_derivative_names=[]
	bid_price_derivative_names=[]
	bid_size_derivative_names=[]
	for i in range(1,11):
		bid_price_names.append("bid_price"+str(i))
		bid_size_names.append('bid_size'+str(i))
		ask_price_names.append('ask_price'+str(i))
		ask_size_names.append("ask_size"+str(i))
		ask_price_derivative_names.append('ask_price_derivative'+str(i))
		ask_size_derivative_names.append('ask_size_derivative'+str(i))
		bid_price_derivative_names.append('bid_price_derivative'+str(i))
		bid_size_derivative_names.append('bid_size_derivative'+str(i))
	original_df=sample_df[ask_price_names+ask_size_names+bid_price_names+bid_size_names][:(sample_df.shape[0]-delta_t)]
	shift_df=sample_df[ask_price_names+ask_size_names+bid_price_names+bid_size_names][delta_t:]
	derivative_df=pd.DataFrame((np.matrix(shift_df)-np.matrix(original_df))/delta_t)
#	derivative_df=pd.concat([pd.DataFrame(np.array(np.nan).repeat(delta_t*derivative_df.shape[1]).reshape((delta_t, derivative_df.shape[1]))), derivative_df])
#	time_index_sub=sample_df[['Index','Time']][delta_t:]
	derivative_df.index=[i for i in range(delta_t,len(sample_df))]
	time_index_sub=sample_df[['Index','Time']][delta_t:]
	derivative_df.index = time_index_sub.index
	derivative_df=pd.concat([time_index_sub,derivative_df],axis=1)
	derivative_df.columns=['Index','Time']+ask_price_derivative_names+ask_size_derivative_names+bid_price_derivative_names+bid_size_derivative_names
	return(derivative_df)


	
