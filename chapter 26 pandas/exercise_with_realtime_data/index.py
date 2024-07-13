import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob, os

df = pd.concat(map(pd.read_csv, glob.glob(os.path.join("E:\Gentle Hero\python_course\chapter 26 pandas\exercise_with_realtime_data\dataset","*.csv"))))

print(df.head(), end="\n\n")
print(df.shape, end="\n\n")
print(df.columns, end="\n\n")
print(df.describe(), end="\n\n")
print(df.info(), end="\n\n")


print(df["Product"].value_counts(), end="\n\n")





############################################################### DATA CLEANING ##########################################################




# seeing how many NaN values are in each column
print(df.isna().sum(), end="\n\n")


# dropping each NaN rows
df.dropna(inplace=True)
print(df.shape, end="\n\n")


# converting the columns into right types
df["Order ID"] = pd.to_numeric(df["Order ID"], errors="coerce")
df["Quantity Ordered"] = pd.to_numeric(df["Quantity Ordered"], errors="coerce")
df["Price Each"] = pd.to_numeric(df["Price Each"], errors="coerce")

print(df.info(), end="\n\n")


# there are some strings in Order date
print(df[df["Order Date"].str[:2] == "Or"])


# removing those strings and making new df
df = df[df["Order Date"].str[:2] != "Or"]


print(df.head(30), end="\n\n")




##################################################### Feature Engineering/ Data Featuring ####################################################




# creating new month column in numeric form for further calculation
df["Month"] = pd.to_datetime(df["Order Date"]).dt.month    
print(df.head(), end="\n\n")


# creating new city column

# creating specific functions for the purpose
def get_city(address):
    return address.split(",")[1].strip()

def get_state(address):
    return address.split(",")[2].split(" ")[1].strip()

# now applying those functions to create the city column
df["City"] = df["Purchase Address"].apply(lambda x: f"{get_city(x)} ({get_state(x)})")

print(df.head(20), end="\n\n")


df["Total Sales"] = df["Quantity Ordered"] * df["Price Each"].astype("float")

print(df.head(20), end="\n\n")

print(df.groupby("Month").sum())


df["Hour"] = pd.to_datetime(df["Order Date"]).dt.hour
df["Minutes"] = pd.to_datetime(df["Order Date"]).dt.minute
df["Count"] = 1

print(df.head())


########################################################## Data Insight Exploration ###########################################################


########### Best sold Month ##############
sales_by_month = df.groupby("Month")

for month, sales in sales_by_month:
    print(f"{month} : {sales["Total Sales"].sum()}")

# months = range(1,13)
# yticks = list(range(1000000,5000001,500000))
# plt.title("Sales in each month")
# plt.xlabel("Months")
# plt.ylabel("Sales($)")
# plt.yticks(yticks)
# plt.bar(months,df.groupby("Month").sum()["Total Sales"], color="aqua", align="center", width=0.7, edgecolor="blue", lw=2)
# plt.savefig("sales_each_month.png")
# plt.tight_layout()
# plt.show()



########## Best sold city ##########
sales_by_city = df.groupby("City")

for city, sales in sales_by_city:
    print(f"{city} : {sales["Quantity Ordered"].sum()}")

# cities = [city for city, loc in df.groupby("City")]
# yticks2 = list(range(10000,60001,4000))


# plt.bar(cities, df.groupby("City").sum()["Quantity Ordered"], color = "aqua", width=0.7)
# plt.xticks(cities, rotation="vertical")
# plt.yticks(yticks2)
# plt.title("Sales by Cities")
# plt.xlabel("cities")
# plt.ylabel("Sold Products")
# plt.savefig("Salesbycities.png")
# plt.tight_layout()
# plt.show()




################### Best time for advertisement ###################
sales_by_hour = df.groupby("Hour")

for hour, count in sales_by_hour:
    print(f"{hour} : {count["Count"].count()}")

# hours = [hour for hour,loc in df.groupby("Hour")]
# yticks = list(range(500,15001,800))

# plt.plot(hours, df.groupby("Hour").count()["Count"], c="aqua")
# # plt.figure()
# plt.yticks(yticks)
# plt.xlabel("Hours")
# plt.ylabel("Times a product has been sold")
# plt.title("Hourly product sales")
# plt.tight_layout()
# plt.savefig("HourlyProductSales.png")
# plt.grid(True)
# plt.show()





####################### Products Often Sold Together ######################
df1 = df[df["Order ID"].duplicated(keep=False)]
print(df1.head(20))

df1["Grouped"] = df1.groupby("Order ID")["Product"].transform(lambda x: ",".join(x))
print(df1.head(20))

print(df1[["Order ID", "Grouped"]].drop_duplicates())




