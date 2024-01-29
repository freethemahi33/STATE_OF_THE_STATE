import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

stateCensusPath = "/Users/aaron/Desktop/Code/State_of_the_State/Data/State_Census_Data.csv"
educationPath = "/Users/aaron/Desktop/Code/State_of_the_State/Data/EducationState.csv"

stateCensus_df = pd.read_csv(stateCensusPath, sep=",")
education_df = pd.read_csv(educationPath, sep=",")

stateCensus_df = stateCensus_df.dropna()
education_df = education_df.dropna()

stateCensus_df = stateCensus_df.rename(columns={'Unnamed: 0' : 'State'})

# stateCensus_df['2018'] = stateCensus_df['2018'].astype(str).astype(int)

# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.bar(stateCensusPath['State'], stateCensusPath['2018'])
# plt.show()

# print(stateCensus_df.dtypes)
# print(education_df.dtypes)

print(stateCensus_df.dtypes)
print(stateCensus_df['2018'])
