import os
import warnings
import numpy as np
import pandas as pd
from joblib import dump, load
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
warnings.filterwarnings('ignore')

def featureScaling(df):
    scaler = StandardScaler()
    df = scaler.fit_transform(df)
    dump(scaler, os.path.join(os.getcwd(), 'model_dumps', 'scaler.pkl'))
    return df

def trainModel(data, cols):
    features = data[cols].copy()
    targets = data["Indicator"]

    encoder = OneHotEncoder(handle_unknown='ignore')
    encoder.fit(features['Extension'].values.reshape(-1, 1))
    temp = encoder.transform(features['Extension'].values.reshape(-1, 1)).toarray()
    dump(encoder, os.path.join(os.getcwd(), 'model_dumps', 'encoder.pkl'))

    features.drop(columns=['Extension'], axis=1, inplace=True)
    features = featureScaling(features)
    features = np.concatenate((features, temp), axis=1)
    targets = np.array(targets).reshape(-1, 1)

    # Commented for deployment
    # skf = StratifiedKFold(n_splits=5, random_state=0)
    # for idx_train, idx_test in skf.split(features, targets):
    #     X_train, y_train = features[idx_train], targets[idx_train]
    #     X_test, y_test = features[idx_test], targets[idx_test]
    #     model = LogisticRegression(class_weight=None, random_state=0)
    #     model.fit(X_train, y_train)
    #     y_pred = model.predict(X_test)
    #     acc = accuracy_score(y_test, y_pred)
    #     print("Accuracy Score = {}".format(acc))

    finalModel = LogisticRegression(class_weight=None, random_state=0)
    finalModel.fit(features, targets)
    predictions = finalModel.predict_proba(features)[:, 1].reshape(-1,1)
    dump(finalModel, os.path.join(os.getcwd(), 'model_dumps', 'finalModel.pkl'))

    return predictions

def assetRiskProfiling(data):
    cols = ['Extension', 'Size', 'DataAge', 'ARecency', \
            'MRecency', 'Depth', 'Unwritten', 'Unaccessed']

    asset = data[data["Data Asset"] == "Yes"]
    asset["Indicator"] = 0
    data["Risk Score"] = 0

    idx = asset.query('Extension == "DOCX" | Extension == "PPTX" | \
                       Extension == "PDF"  | Extension == "PNG"  | \
                       Extension == "JPG"  | Extension == "DOC" | \
                       Extension == "XLS" ')["Id"]

    asset["Indicator"][idx] = 1
    riskScore = trainModel(asset, cols)
    data["Risk Score"][data["Data Asset"] == "Yes"] = riskScore*100
    data["Risk Score"] = data["Risk Score"].round(2)

    return data
