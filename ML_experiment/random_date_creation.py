from random import randrange
from datetime import timedelta
from datetime import datetime
import pandas as pd
import os
import time
import matplotlib.pyplot as plt
import seaborn as sns

def DataLoad():
    path1="/home/vikrant/Downloads/vikrant/Ardent/Data_CSV"
    path=os.path.join(path1,"sherwood.csv")
    df=pd.read_csv(path)
    return df


def main():
    df=DataLoad()
    print(df.columns)
    # df1 = df.sort_values('Risk Score',ascending = False)

    # sum_df = df.groupby(['Extension']).agg({'Risk Score': 'sum'})

    # sum_df = df.groupby(['Extension'])["Risk Score"].mean()
    # print(sum_df)
    # df.hist(column='Risk Score')
    # sns.distplot(df["Risk Score"])
    # df.groupby(['Risk Score']).size()
    hist = df.hist(bins=3)
    print(hist)

    # x=df.groupby(["Extension"]).groups
    # x=df.groupby(["Extension"])
    #
    # for symbol, group in x:
    #     print(symbol)
    #     print(group.shape)
    # print(x)



    # for i in x:
    #     print(x.groups)
    # print(sum_df["Risk Score"].sort_values())
    # for i in sum_df:
    #     print(i)


    # df.hist()



    # df=df.loc[(df['Risk Score'] >= 55) & (df['Risk Score'] <= 85)]
    # print(df.shape)
    # print(df['Risk Score'].mean())
    # print(df['Size'].sum())
    # print(df["DateCreated"].min())

    # print(df["DateModified"].min())
    # print(df["DateModified"].max())
    # print(df["DateAccessed"].min())
    # print(df["DateAccessed"].max())
    # print(df["DateCreated"].min())
    # print(df["DateCreated"].max())




if __name__ == "__main__":
    main()
