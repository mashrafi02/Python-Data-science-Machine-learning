import numpy as np
import pandas as pd

# creating a data frame
data = {
    'City': ['Dhaka', 'Chittagong', 'Khulna', 'Rajshahi', 'Sylhet',
             'Dhaka', 'Chittagong', 'Khulna', 'Rajshahi', 'Sylhet'],
    'Year': [2023, 2023, 2023, 2023, 2023,
             2024, 2024, 2024, 2024, 2024],
    'Population': [8906039, 2683447, 663342, 763952, 531663,
                   8906039, 2683447, 663342, 763952, 531663],
    'Area': [306.38, 168.07, 59.57, 96.68, 26.50,
             306.38, 168.07, 59.57, 96.68, 26.50],
    'Temperature': [30, 29, 28, 32, 31,
                    33, 34, 35, 29, 30]
}

df = pd.DataFrame(data)

# Display the DataFrame with 'Year'
print(df, end="\n\n")


group_city_year = df.groupby(["City","Year"])["Temperature"].mean()
print(group_city_year)