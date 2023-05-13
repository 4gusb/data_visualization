import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_excel("./Canada.xlsx",
        sheet_name='Canada by Citizenship',
        skiprows= range(20))

# print(df.head(5))


# Changes to the og df

df.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
df.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)
print(df.head(5))


# Creation of a copy df w the information needed for the plot. 

processed_df = df.assign(Total = df.iloc[:,9:43].sum(axis=1))
processed_df.set_index("Country", inplace=True)
# print(processed_df.head(5))

processed_df.sort_values(['Total'], ascending=False, axis=0, inplace=True)
# print(processed_df.head(5))

years = list(range(1980,2014))
df_top5 = processed_df.head()
df_top5 = df_top5[years].transpose()
# print(df_top5.head())


# Plot creation

df_top5.plot(kind='area')
plt.title("Inmigration trend of top 5 countries")
plt.ylabel("Number of inmigrants")
plt.xlabel("Years")
plt.show()

--
