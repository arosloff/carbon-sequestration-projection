import pandas as pd
from sklearn.model_selection import train_test_split

a = pd.read_csv("AGC.csv")
b = pd.read_csv("GPP.csv")
b["AGC"] = a

train, test = train_test_split(b, test_size=0.2, shuffle=False)

train.to_csv('GPP_v_AGC_TRAIN.csv', index=False)
test.to_csv('GPP_v_AGC_TEST.csv', index=False)