from random import randrange
from datetime import timedelta
from datetime import datetime
import pandas as pd
import os
import time

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def DataLoad():
    path=os.path.join("/home/mangesh/Downloads/vikrant","metatable.csv")
    df=pd.read_csv(path)
    return df


def main():

    d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')

    # print(random_date(d1, d2))
    # print("vvvvvv/")
    df=DataLoad()
    # print(df)
    min_Datemodified=df["DateModified"].min()
    print(type(min_Datemodified))
    print(min_Datemodified)
    # x=datetime.strptime(min_Datemodified, "%Y-%m-%d %H:%M:%S")
    old_date_in_seconds = datetime.strptime(min_Datemodified, "%Y-%m-%d %H:%M:%S")
    new_date_in_seconds =time.mktime(old_date_in_seconds.timetuple()) - 31556952    #172800
    End_time_of_window=datetime.fromtimestamp(new_date_in_seconds).strftime("%Y-%m-%d %H:%M:%S")
    print(End_time_of_window)
    # print(min_Datemodified.AddYears(-1))

if __name__ == "__main__":
    main()
