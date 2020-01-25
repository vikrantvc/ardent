from random import randrange
from datetime import timedelta
from datetime import datetime
import pandas as pd
import os
import time

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def DataLoad():
    df=pd.read_csv("ML_experiment/metatable.csv")
    return df

def main():

    d1 = datetime.strptime('1/1/2018 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/1/2019 4:50 AM', '%m/%d/%Y %I:%M %p')
    old_date_in_seconds = datetime.strptime(str(random_date(d1, d2)), "%Y-%m-%d %H:%M:%S")
    print(old_date_in_seconds)

    df=DataLoad()
    print(df.head())

    min_Datemodified=df["DateModified"].str[0:4]
    # x=f.DateModified.astype(str).str.pad(6,'left','0')
    print(min_Datemodified)
    # print(x)


    # print(min_Datemodified)
    # x=datetime.strptime(min_Datemodified, "%Y-%m-%d %H:%M:%S")
    # new_date_in_seconds =time.mktime(old_date_in_seconds.timetuple()) - 31556952
    # End_time_of_window=datetime.fromtimestamp(new_date_in_seconds).strftime("%Y-%m-%d %H:%M:%S")
    # print(type(End_time_of_window))

if __name__ == "__main__":
    main()
