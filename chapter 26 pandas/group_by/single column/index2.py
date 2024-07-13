import numpy as np
import pandas as pd
from index import df

print(df, end="\n\n")


# grouping by department and calculating average salary

avg_salary_by_department = df.groupby("Department")["Monthly_Salary"].mean()
print(avg_salary_by_department, end="\n\n") 


data = {
    'City': ['Dhaka', 'Chittagong', 'Khulna', 'Rajshahi', 'Sylhet',
             'Dhaka', 'Chittagong', 'Khulna', 'Rajshahi', 'Sylhet'],
    'Population': [8906039, 2683447, 663342, 763952, 531663,
                   8906039, 2683447, 663342, 763952, 531663],
    'Area': [306.38, 168.07, 59.57, 96.68, 26.50,
             306.38, 168.07, 59.57, 96.68, 26.50],
    'Temperature': [30, 29, 28, 32, 31,
                    33, 34, 35, 29, 30]
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df, end="\n\n")


average_population = df.groupby("City")["Population"].mean()
print(average_population, end="\n\n")


total_area = df.groupby("City")["Area"].sum()
print(total_area, end="\n\n")


average_temperature = df.groupby("City")["Temperature"].mean()
print(average_temperature, end="\n\n")


# Group by and aggregate multiple functions at once
agg_df = df.groupby("City").agg({
    "Population":"mean",
    "Area":"sum",
    "Temperature":["mean","max"]
})
print(agg_df, end="\n\n")