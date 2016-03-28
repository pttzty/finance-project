import numpy as np
import pandas as pd


# def sampling_labels(y_labels, sample_size):
#     '''
#     input: pd.Series
#     output: list of indices
#     '''
#     y_labels = list(y_labels[y_labels.isnull() == False])
#     total_size = len(y_labels)
#     total_indices = range(total_size)
#     total_up_indices = [total_indices[i] for i in range(len(total_indices)) if y_labels[i] == "up"]
#     total_down_indices = [total_indices[i] for i in range(len(total_indices)) if y_labels[i] == "down"]
#     total_stat_indices = [total_indices[i] for i in range(len(total_indices)) if y_labels[i] == "stationary"]
#     up_size = int(np.floor(sample_size / 3))
#     down_size = int(np.floor(sample_size / 3))
#     stat_size = sample_size - up_size - down_size
#     up_indices = np.random.choice(total_up_indices, size=up_size, replace=True)
#     down_indices = np.random.choice(total_down_indices, size=down_size, replace=True)
#     stat_indices = np.random.choice(total_stat_indices, size=stat_size, replace=True)
#     return(list(up_indices) + list(down_indices) + list(stat_indices))


###
def sampling_labels(y_labels,sample_size,sample_random=False,up_prob=1/3,down_prob=1/3):
	y_labels = list(y_labels[y_labels.isnull() == False])
	total_size = len(y_labels)
	total_indices = range(total_size)
	if sample_random == False:
		total_up_indices = [total_indices[i] for i in range(len(total_indices)) if y_labels[i] == "up"]
		total_down_indices = [total_indices[i] for i in range(len(total_indices)) if y_labels[i] == "down"]
		total_stat_indices = [total_indices[i] for i in range(len(total_indices)) if y_labels[i] == "stationary"]
		up_size = int(np.floor(sample_size * up_prob))
		down_size = int(np.floor(sample_size * down_prob))
		stat_size = sample_size - up_size - down_size
		up_indices = np.random.choice(total_up_indices, size=up_size, replace=True)
		down_indices = np.random.choice(total_down_indices, size=down_size, replace=True)
		stat_indices = np.random.choice(total_stat_indices, size=stat_size, replace=True)
		return(list(up_indices) + list(down_indices) + list(stat_indices))
	else:
		random_result = np.random.choice(total_indices, size=sample_size, replace=True)
		return(list(random_result))

def general_sampling(tfm_df,sample_size,mid=True,sample_random=False,up_prob=1/3,down_prob=1/3):
	total_size=tfm_df.shape[0]
	total_indices=range(total_size)
	if sample_random == False:
		if mid == True:
			y_labels =np.asarray(tfm_df['mid_label'])
		else:
			y_labels = np.asarray(tfm_df['spread_label'])
		total_up_indices = [total_indices[i] for i in range(len(total_indices)) if y_labels[i] == "up"]
		total_down_indices = [total_indices[i] for i in range(len(total_indices)) if y_labels[i] == "down"]
		total_stat_indices = [total_indices[i] for i in range(len(total_indices)) if y_labels[i] == "stationary"]
		up_size = int(np.floor(sample_size * up_prob))
		down_size = int(np.floor(sample_size * down_prob))
		stat_size = sample_size - up_size - down_size
		up_indices = np.random.choice(total_up_indices, size=up_size, replace=True)
		down_indices = np.random.choice(total_down_indices, size=down_size, replace=True)
		stat_indices = np.random.choice(total_stat_indices, size=stat_size, replace=True)
		indices = list(up_indices) + list(down_indices) + list(stat_indices)
		result_df = tfm_df.iloc[indices]
	else:
		random_result = np.random.choice(total_indices, size=sample_size, replace=False)
		indices = list(random_result)
		result_df = tfm_df.iloc[indices]
	return(result_df)



