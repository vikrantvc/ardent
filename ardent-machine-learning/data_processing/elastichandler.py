import pandas as pd
from elasticsearch import Elasticsearch

def cleanSize(tpl):
    empty_string = ''
    string = str(tpl['Size'])
    for i in range(0, len(string)):
        if (string[i]>='0') and (string[i]<='9'):
            empty_string = empty_string + string[i]
        else:
            break
    tpl['Size'] = empty_string
    return tpl

def readElastic(idxname):
    es = Elasticsearch()
    # Get number of documents from index ardent_test
    index_size = es.count(index=idxname)['count']
    # Get all documents
    data = es.search(index=idxname, size=index_size, filter_path=['hits.hits._source'])['hits']['hits']
    # Clean data and create dataframe
    data = [sample['_source'] for sample in data]
    df = pd.DataFrame([cleanSize(tpl) for tpl in data])

    df['Deleted'] = 0
    df['HashMD5'] = 0
    df['Id'] = df['Id'].astype('int32')
    df['Size'] = df['Size'].astype('int32')
    return df

def insertElastic(data):
    es = Elasticsearch()
    try:
        maxid = es.search(index="ardent1k", body={"aggs": {"maxid": {"max": { "field": "Id"}}}})
        maxid = int(maxid['aggregations']['maxid']['value'])
        data["Id"] = range(maxid+1, maxid+data.shape[0]+1)
    except:
        data["Id"] = range(1, data.shape[0]+1)

    data['DateModified'] = data['DateModified'].astype('str')
    data['DateAccessed'] = data['DateAccessed'].astype('str')
    data['DateCreated'] = data['DateCreated'].astype('str')

    for i in range(data.shape[0]):
        es.index(index="ardent1k", body=data.iloc[i].to_json())
    es.indices.delete(index="ardent_test")
    return
