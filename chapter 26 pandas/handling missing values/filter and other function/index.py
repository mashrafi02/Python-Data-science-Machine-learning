import numpy as np
import pandas as pd

# creating a data frame
data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['John', 'Emma', 'Michael', 'Sophia', 'William'],
    'Department': ['HR', 'Marketing', 'Finance', 'IT', 'Operations'],
    'Salary': [60000, 70000, 80000, 90000, 65000],
    'ExperienceYears': [5, 3, 7, 4, 6]
}

df = pd.DataFrame(data)
print(df, end="\n\n")


# renaming columns
df.rename(columns={"Salary":"Monthly_Salary", "ExperienceYears":"Years_of_Experience"}, inplace=True)
print(df, end="\n\n")

# Adding a new column for yearly salary
df["Anual_Salary"] = df["Monthly_Salary"] * 12
print(df, end="\n\n")


# dropping a column from the data frame
df.drop(columns=["EmployeeID"], inplace=True)
print(df, end="\n\n")


# filtering monthly salary greater than 70000
high_salary_employees = df[df['Monthly_Salary'] > 70000] 
print(high_salary_employees, end="\n\n")


# sorting data by years of experience in descending order
sorted_df = df.sort_values(by="Years_of_Experience", ascending=False)
print(sorted_df, end="\n\n")

# replaceing
df["Department"] = df['Department'].replace({"HR":"Human Resources", "IT":"Information Technology"})
print(df, end="\n\n")


# applying a function to the salary column to convert it into hourly rate
df["Hourly_rate"] = df["Monthly_Salary"].apply(lambda x: x/(4*40))
print(df, end="\n\n")