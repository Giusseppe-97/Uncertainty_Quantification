import numpy as np
import pandas as pd
import os
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import mean_squared_error, accuracy_score

# load datasets function
def load_data(data_file_name):
    task_flag = data_file_name.split("_")[-1]
    data_dir = "./datasets"
    data_path = os.path.join(data_dir, data_file_name)
    df = pd.read_csv(data_path)
    data_X = df.iloc[:,:-1]
    data_y = df.iloc[:,-1]
    scaler_X = StandardScaler()
    data_X = scaler_X.fit_transform(data_X)
    if task_flag == "regression":
        scaler_y = MinMaxScaler()
        data_y = scaler_y.fit_transform(data_y.reshape(-1,1)).reshape(-1)
    else:
        data_y = pd.Categorical(data_y).codes.reshape(-1)
    return data_X, data_y

# runing model function
def runRandomForestClassifier(train_X, train_y, test_X, test_y, n_estimators):
    # Import the model
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(n_estimators=n_estimators)
    model.fit(train_X, train_y)
    pred_y = model.predict(test_X)
    ## if regression
    # res = mean_squared_error(test_y, pred_y)
    ## if classification
    res = accuracy_score(test_y, pred_y)
    return res

# main function
def main():
    # predefining parameters
    random_state = 404

    # model-specified parameters
    n_estimators = 5

    # read dataset from csv file
    data_name = "abalone_classification"
    data_X, data_y = load_data("{}.csv".format(data_name))

    # CrossValidation with 5 splits
    kf = KFold(n_splits=5, random_state=random_state)
    res_list = []
    for train_index, test_index in kf.split(data_X):
        train_X, train_y = data_X.iloc[train_index,:], data_y[train_index]
        test_X, test_y = data_X.iloc[test_index,:], data_y[test_index]
        res = runRandomForestClassifier(train_X, train_y, test_X, test_y, n_estimators)
        res_list.append(res)
    AveragedPerformance = np.mean(res_list)
    print(AveragedPerformance)