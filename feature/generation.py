import pandas as pd
class generation:
    '''
    获取原始数据并进行特征工程，返回处理后的数据
    用法：
    gen = generation()
    change_data = gen.fit_transform(data)
    '''
    def fit_transform(self,data:pd.DataFrame):
        
