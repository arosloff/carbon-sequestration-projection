import pandas as pd

ipsl_projection = pd.read_csv("AGC.txt", delimiter='\t')

ipsl_projection.dropna(inplace=True)

ipsl_projection['avgAGC'] = ipsl_projection.groupby(['time', 'lat', 'lon'])[['AGC']].transform('mean')
ipsl_projection.drop_duplicates(subset=['time', 'lat', 'lon'], keep='last', inplace=True)

ipsl_projection.drop(['AGC'], axis=1, inplace=True)

ipsl_projection.to_csv('big_clean_projection.csv', index=False)


