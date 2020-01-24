import os
import click
import warnings
import pandas as pd
import data_processing.preprocessing as prep
from deduplication.hasher import metaHashing
from risk_profiling.analyze import analyzeRisk
from deduplication.finder import metaDuplicates
import feature_extraction.derivedfeatures as fext
import asset_classifier.fileclassification as fcls
from risk_profiling.modeling import assetRiskProfiling
from data_processing.elastichandler import readElastic, insertElastic
warnings.filterwarnings('ignore')

@click.command()
@click.option('--mode', default="test", help='Mode of Program')
def main(mode):
    if mode == "train":
        # Loading data from various sources
        syst = pd.read_csv(os.path.join("scan_data", "system.csv"))
        home = pd.read_csv(os.path.join("scan_data", "home.csv"))
        # Merging the data together
        data = pd.concat([syst, home], ignore_index=True)
        # Data Preprocessing
        data = prep.pipeline(data)
        # Feature Extraction
        data = fext.pipeline(data)
        # Data Classification
        data = fcls.pipeline(data)
        # Data Risk Model Training
        data["Id"] = range(data.shape[0])
        data = assetRiskProfiling(data)
        #data.to_csv(os.path.join("scan_data", "output.csv"), index=False)
        print("Model Training Completed Successfully...")
    elif mode == "test":
        data = readElastic("ardent_test")
        # Data Preprocessing
        data = prep.pipeline(data)
        # Feature Extraction
        data = fext.pipeline(data)
        # Data Classification
        data = fcls.pipeline(data)
        # Analyzing Risk Score
        data = analyzeRisk(data)
        # Generating MD5 Hashes
        data = metaHashing(data)
        # Insert Into Elasticsearch
        insertElastic(data)
        metaDuplicates(data)
        print("Risk Score Analysis Successfull...")
    return

if __name__ == '__main__':
    main()
