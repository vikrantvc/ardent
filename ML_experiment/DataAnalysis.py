import pandas as pd
import os
import matplotlib.pyplot as plt

def DataLoad():
    path=os.path.join("sherwood.csv")
    df=pd.read_csv(path)
    df=df.drop(['Id','Name','Type1', 'Type2', 'Path', 'DateCreated', 'DateModified', 'DateAccessed', 'Size', 'Deleted', 'DataAge', 'ARecency', 'MRecency', 'Unwritten', 'Unaccessed', 'Depth', 'Root', 'Data Asset'], axis=1)
    return df

def BoxPlot(df):                              # plots the box plot groupby Extension & risk score
    df.boxplot(column=["Risk Score"],by="Extension")
    plt.xlabel('Extensions')
    plt.ylabel('Risk Scores')
    plt.show()

def BarChart(df):                             # plots bar BarChart for extension category with mean risk score
    x=df.groupby(["Extension"],as_index=False)["Risk Score"].median()
    df=x.sort_values('Risk Score',ascending = False).head(10)
    df.plot.bar(x='Extension', y='Risk Score',rot=20)
    plt.xlabel('Extensions')
    plt.ylabel('Mean')
    plt.show()
    print(df)

def main():
    df=DataLoad()
    df=df.sort_values('Risk Score',ascending = False)
    df=df.head(412)
    print(df)

    # c=0
    # for i in df["Risk Score"]:
    #     if int(i) > 59:
    #         c+=1
    # print(c)

    # BoxPlot(df)
    # BarChart(df)
    # x=df.groupby(["Extension"],as_index=False)["Risk Score"].median()
    # df=x.sort_values('Risk Score',ascending = False).head(10)
    df.plot.hist(column=["Risk Score"],by="Extension",range=[10, 85])#,bins=10)
    plt.show()


if __name__ == "__main__":
    main()
