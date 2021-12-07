import pandas as pd



a = pd.read_csv("IPSL_AGC.csv", delimiter='\t')
a.dropna(inplace=True)
a['loc'] = list(zip(a['lat'], a['lon']))
a.sort_values(by=['time', 'lat', 'lon'], ascending=True)

a["AGC"] = a["AGC"].divide(a["AGC"].mean())
b = 0
for index, row in a.iterrows():
    loc = str(row['loc'])
    val = row['AGC']
    if loc not in lat_lon_dict:
        lat_lon_dict[loc] = [val]
    else:
        lat_lon_dict[loc].append(val)

c = pd.DataFrame.from_dict(lat_lon_dict)
#
# .to_csv('AGC_Tuple_test.csv', index=False)
a.to_csv('IPSL_AGC.csv', index=False)