import os
import numpy as np
import pandas as pd
from joblib import dump, load

def nameRiskIdentifier(filename):
    def preprocess(filename, dictionary, extensions):
        filename['Name'] = filename['Name'].str.upper()
        filename['Name'] = filename['Name'].str.split('.', expand=True)
        dictionary['names'] = dictionary['names'].str.upper()
        dictionary['names'] = dictionary['names'].str.replace(' ', '_')
        extensions['extension'] = extensions['extension'].str.upper()
        return filename, dictionary, extensions

    def exact_match(filename, dictionary, extensions):
        nameBool = []
        nameRisk = []
        for idx in range(filename.shape[0]):
            fname = filename["Name"][idx]
            fexts = filename["Extension"][idx]
            wtext, wtfile = 0, 0
            if fexts in extensions["extension"].to_list() and fname in dictionary["names"].to_list():
                wtfile = dictionary[dictionary["names"]==fname]["weight"].values[0]
                wtext = extensions[extensions["extension"]==fexts]["weight"].values[0]
                nameBool.append(True)
                nameRisk.append((wtext+wtfile)/2)
            else:
                nameBool.append(False)
                nameRisk.append(0)
        return nameBool, nameRisk

    extensions = pd.read_csv(os.path.join(os.getcwd(), "scan_data", "extensions.csv"))
    dictionary = pd.read_csv(os.path.join(os.getcwd(), "scan_data", "dictionary.csv"))
    filename, dictionary, extensions = preprocess(filename, dictionary, extensions)
    nameBool, nameRisk = exact_match(filename, dictionary, extensions)
    return nameBool, nameRisk

def analyzeRisk(data):
    cols = ['Extension', 'Size', 'DataAge', 'ARecency', \
            'MRecency', 'Depth', 'Unwritten', 'Unaccessed']

    features = data[cols].copy()
    scaler = load(os.path.join(os.getcwd(), 'model_dumps', 'scaler.pkl'))
    encoder = load(os.path.join(os.getcwd(), 'model_dumps', 'encoder.pkl'))
    finalModel = load(os.path.join(os.getcwd(), 'model_dumps', 'finalModel.pkl'))

    temp = encoder.transform(features['Extension'].values.reshape(-1, 1)).toarray()
    features.drop(columns=['Extension'], axis=1, inplace=True)
    features = np.concatenate((scaler.transform(features), temp), axis=1)
    predictions = finalModel.predict_proba(features)[:, 1].reshape(-1,1)

    nameBool, nameRisk = nameRiskIdentifier(data.copy())
    data["Risk Score"] = predictions*100
    data["Risk Score"] = data["Risk Score"].round(2)
    data["Risk Score"][nameBool] = nameRisk

    return data
