
import datetime
import pandas as pd

df = pd.io.parsers.read_csv("labdata_2014-07-10_2.csv")

grouped = df.groupby(['patient', 'lab_id'])

for name, group in df.groupby(['patient', 'lab_id']):
    m = group.lab_dmy.dropna().min()
    group['diff2'] = pd.to_datetime(group['lab_dmy']) - pd.to_datetime(m)
    group.to_csv("out3.csv", mode="a", header=False)

