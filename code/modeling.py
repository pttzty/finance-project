import pandas as pd
import numpy as np
from datetime import datetime
from label import mid_label, spread_label
from basic_set import get_basic
from insensitive_set import get_spread_midprice, get_price_diff, get_mean, get_accumulated_diff
from sampling import sampling_labels
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier as RF

# load data
data=pd.read_csv('AAPL_05222012_0930_1300_LOB_2.csv')

# change column name
col_names = [x[:-19][16:].lower() for x in data.columns]
col_names[0]='Index'
col_names[1]='Time'
data.columns = col_names

# get new data
basics = get_basic(data)
spreads_mids = get_spread_midprice(data)
price_diff = get_price_diff(data)
means = get_mean(data)
accum_diff = get_accumulated_diff(data)
data = pd.merge(basics, spreads_mids, on = ['Index', 'Time'])
data = pd.merge(data, price_diff, on = ['Index', 'Time'])
data = pd.merge(data, means, on = ['Index', 'Time'])
data = pd.merge(data, accum_diff, on = ['Index', 'Time'])

# Create time variable
time = np.array([datetime.strptime(time, "%Y/%m/%d %H:%M:%S.%f") for time in data['Time']])

# training set is before 11:00, rest is test
train_index = time < datetime(2012, 5, 22, 11, 0)
train = data.iloc[train_index]
test = data.iloc[np.logical_not(train_index)]
train.shape

# create y labels
y_lab_train = mid_label(train['mid-price_spread1'], 20)[:-20]
y_lab_test = mid_label(test['mid-price_spread1'], 20)[:-20]

# Sample
t_ind = sampling_labels(y_lab_train, 2000)
v_ind = sampling_labels(y_lab_test, 2000)


# fit SVM
# from sklearn import svm
# clf = svm.SVC(kernel='poly') # too slow, couldn't get it to work
# model
clf = svm.SVC(decision_function_shape='ovr')
clf.fit(train[data.columns[2:]].iloc[t_ind], y_lab_train[t_ind])
# accuracy
clf.score(train[data.columns[2:]].iloc[t_ind], y_lab_train[t_ind])
clf.score(test[data.columns[2:]].iloc[v_ind], y_lab_test[v_ind])
# prediction and confusion matrix
predict_train = clf.predict(train[data.columns[2:]].iloc[t_ind])
confusion_matrix(predict_train, y_lab_train[t_ind])
predict_test = clf.predict(test[data.columns[2:]].iloc[v_ind])
confusion_matrix(predict_test, y_lab_test[v_ind])

# fit linear SVM
# model
clf = svm.LinearSVC()
clf.fit(train[data.columns[2:]].iloc[t_ind], y_lab_train[t_ind])
# accuracy
clf.score(train[data.columns[2:]].iloc[t_ind], y_lab_train[t_ind])
clf.score(test[data.columns[2:]].iloc[v_ind], y_lab_test[v_ind])
# prediction and confusion matrix
predict_train = clf.predict(train[data.columns[2:]].iloc[t_ind])
confusion_matrix(predict_train, y_lab_train[t_ind])
predict_test = clf.predict(test[data.columns[2:]].iloc[v_ind])
confusion_matrix(predict_test, y_lab_test[v_ind])


# from sklearn.ensemble import RandomForestClassifier as RF
# model
cand = RF(n_estimators=100, max_depth=3,criterion='entropy')
cand = cand.fit(train[data.columns[2:]].iloc[t_ind], y_lab_train[t_ind])
# accuracy
cand.score(train[data.columns[2:]].iloc[t_ind], y_lab_train[t_ind])
cand.score(test[data.columns[2:]].iloc[v_ind], y_lab_test[v_ind])
# prediction and confusion matrix
predict_train = cand.predict(train[data.columns[2:]].iloc[t_ind])
confusion_matrix(predict_train, y_lab_train[t_ind])
predict_test = cand.predict(test[data.columns[2:]].iloc[v_ind])
confusion_matrix(predict_test, y_lab_test[v_ind])



