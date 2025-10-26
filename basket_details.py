# Basket Details
# customer_id: Unique ID given to the Customer.
# product_id: Unique ID of the product which has been added to the basket by the customer.
# basket_date: Date of transaction.
# basket_count: How many times this event occured during this date

import pandas as pd
from datetime import date as dt
from matplotlib import pyplot as plt

df = pd.read_excel("Data Analyst//Ecom analysis//basket_details.xlsx")

#printing the size and the columns of the dataset
print(f"Size: {df.size}", '\n')
print(f"Columns: {df.columns}", '\n')

#printing the row with largest number of basket count
print(df.loc[df['basket_count'].idxmax()], '\n')
print(df.loc[df['basket_count'].idxmin()], '\n')

#counting total number of basket counts monthly and day wise

print("Value Count on Monthly basis: ")
print(df['basket_date'].dt.month.value_counts(), '\n')

print("Value Count on day to day basis: ")
print(df['basket_date'].dt.day.value_counts().sort_index(ascending=True), '\n')

#printing the everyday transactions for both the months separately
print("For May")
print(df.query('basket_date.dt.month == 5').sort_values(by='basket_date'), '\n')
print("For June: ")
print(df.query('basket_date.dt.month == 6').sort_values(by='basket_date'), '\n')

#checking to see the unique customer ID's
print("Top 5 customers:")
print(df['customer_id'].value_counts().head(5), '\n')

#printing all the customer id's that are repeated
print("All the repeated customer id's")
duplicates = df['customer_id'].duplicated()
print(df.query('@duplicates == True'),'\n')

#checking to see if the product Id's are repeated
product_id_repeat = df['product_id'].duplicated()
print("Which product has been purchased more than once")
print(df.query('@product_id_repeat == True'), '\n')

#checking the most purchased products
print("Which product has been purchased the most: ")
print(df['product_id'].value_counts().head(5))

#plotting a graph to see the top 5 most purchased products
df['product_id'].value_counts().head(5).plot(kind='bar', title="Top 5 Most purchased products")
plt.show()