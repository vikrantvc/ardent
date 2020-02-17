import os
import pandas as pd
from elasticsearch import Elasticsearch

def createIndex(data):
    es = Elasticsearch()
    for idx in range(data.shape[0]):
        #es.index(index="ardent_test", body=data.iloc[idx].to_json())
        es.index(index="ardent1k", body=data.iloc[idx].to_json())
    return

if __name__ == '__main__':
    dfr = pd.read_csv(os.path.join('/home/vikrant/Downloads/vikrant/Ardent/Data_CSV', 'sherwood.csv'))
    dfr["Id"] = range(1, dfr.shape[0]+1)
    # createIndex(dfr)
    print(dfr.isnull().sum())
