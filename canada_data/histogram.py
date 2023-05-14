import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


df = pd.read_excel("./Canada.xlsx",
        sheet_name='Canada by Citizenship',
        skiprows=range(20),
        skipfooter=2)

# print(df.head(5))


# Changes to the original table.

df.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)

df.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)

df['Total'] = df.sum(axis=1)


# Histogram creation.

count, bin_edges = np.histogram(df[2013])
plt.hist(df[2013], color='#1D267D')
plt.xticks(bin_edges)
plt.title('Histogram of Inmigration from 195 countries in 2013')
plt.ylabel('Number of Countries')
plt.xlabel('Number of inmigrants')

plt.show()

--
