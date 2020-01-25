from datetime import datetime
from elasticsearch import Elasticsearch
import pandas as pd
es = Elasticsearch()

df=pd.read_csv("/home/vikrant/Downloads/vikrant/Ardent/Data_CSV/sherwood.csv")

# print(df.head())df.shape[0]df.shape[0]

#insert below data into elasticsearchdf.shape[0]
# doc = {
#     'author': 'kimchy',
#     'text': 'Elasticsearch: cool. bonsai cool.',
#     'timestamp': datetime.now(),
# }
# res = es.index(index="test-index", id=1, body=doc)
# print(res['result'])

#delete index
# es.indices.delete(index='test-index', ignore=[400, 404])



df['Id'] = range(0, df.shape[0])

for i in range(df.shape[0]):
    # print(df.iloc[i].to_json())
    # break
    es.index(index="sherwood", body=df.iloc[i].to_json())
