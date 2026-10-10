# preparing raw data for machine learning

#1. data cleaning
# What if data is not clear or incomplete

#2. hadling missing values

#3. ecoding
#converting values, text to numbers, repeated texts

#4. feature scaling
#making sure the data has values of different scale and level
#if salary and age are analysed, different units but use with same level

#5. removing outliers
#data that does not represent the actual pattern of the data

#6. dividing our existing data into training and testing. 
#have some test data, that you can check how close your analysis is. take some data to train the machine

import pandas as pd
 


sample_data_set = {
    "Age" : [23, 28, 30, 25, 33, 26, None, 34, None, None],
    "Gender" : ["Male", "Female", None, "Female ", "Male", "Male", None, "Female", "Male ", "Female"], 
    "Salary" : [30, 20, None, 32, 20, 45, 34, 26, 33, 17],
    "Department" : ["HR", "Finance", "IT", "Creative", "Manager", "HR", "IT", None, "Creative", "Finance"],
    "Car" : ["No", "Yes", "Yes", "No", "Yes", "No", "No", "No", "Yes", "No"]
}

df = pd.DataFrame(sample_data_set)
print(df)
print("----" * 45)


#starting data cleaning
# removing spaces from all text based columns

for col in df.columns:
    if df[col].dtype == "object" :
        df[col] = df[col].str.strip()
        