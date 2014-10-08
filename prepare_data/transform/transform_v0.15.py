
import datetime
import pandas as pd
import numpy as np

df = pd.io.parsers.read_csv("demo_data.csv")

grouped = df.groupby(['patient', 'lab_id'])

for name, group in df.groupby(['patient', 'lab_id'], sort=False):
    m = group.lab_dmy.dropna().min()
    group['diff'] = pd.Series(np.nan, index = group.index)
    for i in range(len(group['lab_dmy'])):
        print "i: " + str(i)
        print group
        print group['lab_dmy'][i]
        if not pd.isnull(group['lab_dmy'][i]):
            print "-----------"
            print group['diff'][i]
            group['diff'][i] = "rawr"
            print group['lab_dmy'][i]
            print "min: " + str(m)
            print pd.to_datetime(group['lab_dmy'][i])
            print pd.to_datetime(m)
            print pd.to_datetime(group['lab_dmy'][i]) - pd.to_datetime(m)
            group['diff'][i] = pd.to_datetime(group['lab_dmy'][i]) - pd.to_datetime(m)
            print group

    group.to_csv("demo_out.csv", mode="a", header=False)

