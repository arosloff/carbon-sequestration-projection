import csv

import pandas as pd

def dfSort(frames, col):
    df = pd.concat(frames)
    sortedDf = df.sort_values(by=['time', 'lat', 'lon'], ascending=True)
    return sortedDf[col].divide(sortedDf[col].mean())

fmec = pd.read_csv("FMEC/AGC.txt", delimiter='\t')
ipsl = pd.read_csv("IPSL/AGC.txt", delimiter='\t')
miroc = pd.read_csv("MIROC/AGC.txt", delimiter='\t')

fmec.dropna(inplace=True)
ipsl.dropna(inplace=True)
miroc.dropna(inplace=True)

frames = [fmec, ipsl, miroc]

df = pd.concat(frames)
df = df.sort_values(by=['time', 'lat', 'lon'], ascending=True)
df = df.drop('AGC', 1)

# fmecAGC = pd.read_csv("FMEC/AGC.txt", delimiter='\t')
# ipslAGC = pd.read_csv("IPSL/AGC.txt", delimiter='\t')
# mirocAGC = pd.read_csv("MIROC/AGC.txt", delimiter='\t')
# fmecAGC.dropna(inplace=True)
# ipslAGC.dropna(inplace=True)
# mirocAGC.dropna(inplace=True)
# df['AGC'] = dfSort([fmecAGC, ipslAGC, mirocAGC], 'AGC')
#
# fmecBTRAN = pd.read_csv("FMEC/BTRAN.txt", delimiter='\t')
# ipslBTRAN = pd.read_csv("IPSL/BTRAN.txt", delimiter='\t')
# mirocBTRAN = pd.read_csv("MIROC/BTRAN.txt", delimiter='\t')
# fmecBTRAN.dropna(inplace=True)
# ipslBTRAN.dropna(inplace=True)
# mirocBTRAN.dropna(inplace=True)
# df['BTRAN'] = dfSort([fmecBTRAN, ipslBTRAN, mirocBTRAN], 'BTRAN')
#
# fmecBAF = pd.read_csv("FMEC/burned_area_fraction.txt", delimiter='\t')
# ipslBAF = pd.read_csv("IPSL/burned_area_fraction.txt", delimiter='\t')
# mirocBAF = pd.read_csv("MIROC/burned_area_fraction.txt", delimiter='\t')
# fmecBAF.dropna(inplace=True)
# ipslBAF.dropna(inplace=True)
# mirocBAF.dropna(inplace=True)
# df['BAF'] = dfSort([fmecBAF, ipslBAF, mirocBAF], 'burned_area_fraction')
#
# fmecGPP = pd.read_csv("FMEC/GPP.txt", delimiter='\t')
# ipslGPP = pd.read_csv("IPSL/GPP.txt", delimiter='\t')
# mirocGPP = pd.read_csv("MIROC/GPP.txt", delimiter='\t')
# fmecGPP.dropna(inplace=True)
# ipslGPP.dropna(inplace=True)
# mirocGPP.dropna(inplace=True)
# df['GPP'] = dfSort([fmecGPP, ipslGPP, mirocGPP], 'GPP')
#
# fmecNEE = pd.read_csv("FMEC/NEE.txt", delimiter='\t')
# ipslNEE = pd.read_csv("IPSL/NEE.txt", delimiter='\t')
# mirocNEE = pd.read_csv("MIROC/NEE.txt", delimiter='\t')
# fmecNEE.dropna(inplace=True)
# ipslNEE.dropna(inplace=True)
# mirocNEE.dropna(inplace=True)
# df['NEE'] = dfSort([fmecNEE, ipslNEE, mirocNEE], 'NEE')
#
# fmecNPP = pd.read_csv("FMEC/NPP.txt", delimiter='\t')
# ipslNPP = pd.read_csv("IPSL/NPP.txt", delimiter='\t')
# mirocNPP = pd.read_csv("MIROC/NPP.txt", delimiter='\t')
# fmecNPP.dropna(inplace=True)
# ipslNPP.dropna(inplace=True)
# mirocNPP.dropna(inplace=True)
# df['NPP'] = dfSort([fmecNPP, ipslNPP, mirocNPP], 'NPP')
#
# fmecRA = pd.read_csv("FMEC/RA.txt", delimiter='\t')
# ipslRA = pd.read_csv("IPSL/RA.txt", delimiter='\t')
# mirocRA = pd.read_csv("MIROC/RA.txt", delimiter='\t')
# fmecRA.dropna(inplace=True)
# ipslRA.dropna(inplace=True)
# mirocRA.dropna(inplace=True)
# df['RA'] = dfSort([fmecRA, ipslRA, mirocRA], 'RA')
#
# fmecRH = pd.read_csv("FMEC/RH.txt", delimiter='\t')
# ipslRH = pd.read_csv("IPSL/RH.txt", delimiter='\t')
# mirocRH = pd.read_csv("MIROC/RH.txt", delimiter='\t')
# fmecRH.dropna(inplace=True)
# ipslRH.dropna(inplace=True)
# mirocRH.dropna(inplace=True)
# df['RH'] = dfSort([fmecRH, ipslRH, mirocRH], 'RH')

df['loc'] = list(zip(df['lat'], df['lon']))

df['loc'].to_csv('clean.csv', index=False, header=False, escapechar='\n')