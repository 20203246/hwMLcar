import sys
sys.path.append('.')
sys.path.append('..')
import os
from collections import namedtuple
import pandas as pd
currentDirname = os.path.dirname(__file__)

config = {
    'train_path':f'{currentDirname}/../data/used_car_train_20200313.csv',
    'test_path':f'{currentDirname}/../data/used_car_testB_20200421.csv',
    'prediction_path':f'{currentDirname}/../prediction_result/predictions.csv',
    'tmp_path':f'{currentDirname}/../user_data',
}

# 获取数据
train_data = pd.read_csv(config['train_path'],sep=' ')
test_data  = pd.read_csv(config['test_path'],sep=' ')

from feature import generation
data = generation().fit_transform(pd.concat([train_data,test_data],axis=0))
