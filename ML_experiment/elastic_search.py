from datetime import datetime
from elasticsearch import Elasticsearch
import pandas as pd
es = Elasticsearch()

df=pd.read_csv("/home/vikrant/Downloads/test csv/test3.csv")

#delete index
# es.indices.delete(index='test-index', ignore=[400, 404])

#delete the data from index not delete index
# es.delete_by_query(index="testx", body={"query":{"range":{"Count":{"gte":0}}}})

#push csv into elasticsearch
# df['Id'] = range(0, df.shape[0])    #create id which is not present in crawler generated csv
for i in range(df.shape[0]):
    es.index(index="testx", body=df.iloc[i].to_json())
