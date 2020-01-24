import pandas as pd

def identifyUserFiles(data):
    data["Data Asset"] = "No"
    data["Data Asset"][data["Root"]=="S3"] = "Yes"
    data["Data Asset"][data["Root"]=="home"] = "Yes"
    return data

def pipeline(data):
    data = identifyUserFiles(data)
    return data
