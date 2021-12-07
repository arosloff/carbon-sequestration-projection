import pandas as pd

cleanDF = pd.read_csv("FeatureClean/all_clean_training.csv")

lat_lon_dict = {}

cleanDF['loc'] = list(zip(cleanDF['lat'], cleanDF['lon']))

lat_lon_dict = dict(iter(cleanDF.groupby('loc')))

def mean_norm(df_input):
    return df_input.apply(lambda x: (x-x.mean())/ x.std(), axis=0)

#normalDf = cleanDF.drop(['time', 'lat', 'lon', 'loc'])

for index, row in cleanDF.iterrows():
    loc = str(row['loc'])
    val = row
    #val = [row['BTRAN'], row['BAF'], row['CFC'], row['GPP'], row['NEE'], row['NEP'], row['NPP'], row['RA'], row['RH'], row['SA'], row['AGC']]
    if loc not in lat_lon_dict:
        lat_lon_dict[loc] = [val]
    else:
        lat_lon_dict[loc].append(val)

for key in lat_lon_dict:
    pd.DataFrame(lat_lon_dict.get(key)).to_csv(f'FeatureClean/Locations/data_{key}.csv', index=False, header = ['time','lat','lon','AGC','BTRAN','BAF','GPP','NEE','NPP','RA','RH','CFC','NEP','SA','loc'])

# pd.DataFrame.from_dict(lat_lon_dict).to_csv('hi.csv')