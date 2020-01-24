import pandas as pd

def dateFeatures(data):
    data["DataAge"] = (pd.Timestamp.now()-data["DateCreated"]).dt.days
    data["ARecency"] = (pd.Timestamp.now()-data["DateAccessed"]).dt.days
    data["MRecency"] = (pd.Timestamp.now()-data["DateModified"]).dt.days

    data["Unwritten"] = (data["DateCreated"]>data["DateModified"]).astype('int')
    data["Unaccessed"] = (data["DateCreated"]>data["DateAccessed"]).astype('int')
    return data

def pathFeatures(data):
    data["Depth"] = data["Path"].str.strip("/").str.count("/")+1
    data["Root"] = [item[0] for item in data["Path"].str.strip("/").str.split("/").to_list()]
    return data

def pipeline(data):
    data = dateFeatures(data)
    data = pathFeatures(data)
    return data
