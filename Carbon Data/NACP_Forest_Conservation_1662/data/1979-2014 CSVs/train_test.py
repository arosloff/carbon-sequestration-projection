import pandas as pd
from sklearn.model_selection import train_test_split

a = pd.read_csv("FeatureClean/Locations/data_(31.396, -106.04749999999736).csv")

train, test = train_test_split(a, test_size=0.2, shuffle=False)

train.to_csv('data_(31.396, -106.04749999999736).train.csv', index=False)
test.to_csv('data_(31.396, -106.04749999999736).test.csv', index=False)