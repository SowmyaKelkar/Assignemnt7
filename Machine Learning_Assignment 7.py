
import numpy as np
import pandas as pd

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})


#Importing the dataset
X=df.iloc[:,:-1].values
y=df.iloc[:,-1].values

#missing values
df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)

#splitting the From_To column
df['From'], df['To'] = zip(*df['From_To'].map(lambda x: x.split('_')))

#removing From_To column from dataset
df.drop(['From_To'],axis=1,inplace=True)

#Applying the Ttile format to From and To columns
df.From = df.From.apply(lambda x: x.title())

df.To = df.To.apply(lambda x: x.title())




    
