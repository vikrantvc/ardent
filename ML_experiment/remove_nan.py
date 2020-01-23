import pandas as pd
import os


def DataLoad():
    path1="/home/vikrant/Downloads/vikrant/Ardent/File_Scanner_copy/ardent-filescanner"
    path=os.path.join(path1,"ardent.csv")
    df=pd.read_csv(path)
    df=df.drop(['Id','HashMD5'], axis = 1)
    df=df.iloc[0:405000,:]
    df=df.dropna()
    return df

def Create_csv(df):
    df.to_csv("/home/vikrant/Downloads/vikrant/Ardent/File_Scanner_copy/ardent-filescanner/ar.csv",index=False)


def main():

    df=DataLoad()
    Create_csv(df)
    print(df)

if __name__ == "__main__":
    main()
