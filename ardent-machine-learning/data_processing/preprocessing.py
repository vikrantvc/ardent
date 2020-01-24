import pandas as pd

def dataTypeHandling(data):
    data['DateModified'] = data['DateModified'].astype('datetime64[ns]')
    data['DateAccessed'] = data['DateAccessed'].astype('datetime64[ns]')
    data['DateCreated'] = data['DateCreated'].astype('datetime64[ns]')
    return data

def cleanData(data):
    data.drop(data[data["Name"].isna()].index, inplace=True)
    data.drop(columns=["HashMD5"], axis=1, inplace=True)
    data["Extension"][data["Extension"].isna()] = "EXE"
    return data

def pipeline(data):
    data = dataTypeHandling(data)
    data = cleanData(data)
    return data
