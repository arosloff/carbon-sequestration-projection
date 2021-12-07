
import pandas as pd

df = pd.read_csv("all_clean_training_raw.csv")
print(df.shape)
df[['avgAGC','avgBTRAN','avgBAF','avgGPP','avgNEE','avgNPP','avgRA','avgRH','avgCFC','avgNEP','avgSA']] = df.groupby(['time', 'loc'])[['AGC','BTRAN','BAF','GPP','NEE','NPP','RA','RH','CFC','NEP','SA']].transform('mean')
df.drop_duplicates(subset=['time', 'loc'], keep='last', inplace=True)

df.drop(['AGC','BTRAN','BAF','GPP','NEE','NPP','RA','RH','CFC','NEP','SA','loc'], axis=1, inplace=True)
df.reset_index(drop=True, inplace=True)

df.reset_index(drop=True, inplace=True)
df.reset_index(drop=True, inplace=True)
print(df)
print(df.shape)

s = df.groupby(['time']).cumcount()

df1 = df.set_index(['time', s]).unstack().sort_index(level=1, axis=1)
df1.columns = [f'{x}' for x in df1.columns]
df1 = df1.reset_index()

print(df1)
print(df1.shape)

df1.to_csv('pivot_all_clean_training.csv', index=False, escapechar='\n')