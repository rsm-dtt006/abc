import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Read in the data
salaries = pd.read_csv('ds_salaries.csv')
salaries.head()

# Cross check for null values
salaries.isnull().sum()


# Find the city with highest salary
city = salaries.groupby('company_location')['salary_in_usd'].mean()
city.sort_values(ascending=False).head(10)

# Plotting a graph of the salaries
sns.histplot(data=salaries, x='salary_in_usd', kde = True, bins=20)
