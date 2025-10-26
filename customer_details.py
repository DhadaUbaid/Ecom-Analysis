# Customer Details
# customer_id: Unique ID given to the Customer.
# sex: Sex of customer.
# customer_age: Age of customer.
# tenure: tenure of customer as month

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_excel("Data Analyst\\Ecom analysis\\customer_details.xlsx")

#checking the size and column names
print(df.size)
print(df.columns)

#There are a few abnormal values in the dataset, hence changing the value in a column
df['sex'].mask(df['sex'] == "UNKNOWN", "Female", inplace=True)
df['sex'].mask(df['sex'] == "kvkktalepsilindi", "Male", inplace=True)

#checking if the values were replaced properly
print(df['sex'].value_counts())

#Checking the top 5 youngest customer(Both Male and Female)
print(df.query('sex == "Male"').nsmallest(5, 'customer_age')[['customer_id', 'sex', 'customer_age', 'tenure']])
print(df.query('sex == "Female"').nsmallest(5, 'customer_age')[['customer_id', 'sex', 'customer_age', 'tenure']])

#checking the top 5 oldest Customers(Both Male and Female)
print(df.query('sex == "Male"').nlargest(5, 'customer_age')[['customer_id', 'sex', 'customer_age', 'tenure']])
print(df.query('sex == "Female"').nlargest(5, 'customer_age')[['customer_id', 'sex', 'customer_age', 'tenure']])


#Upon checking, found out that the age columns had negative values, hence replacing all the values with 24
df['customer_age'] = df['customer_age'].mask(df['customer_age'] < 18, 24)

#The oldest customer age came out to be more than 2000, hence changing those values as well
df['customer_age'] = df['customer_age'].mask(df['customer_age'] > 100, 44)

#checking the most eldest customers both male and female 
max_age = df['customer_age'].max()
print(df.query('sex == "Male" & customer_age == @max_age'),'\n')
print(df.query('sex == "Female" & customer_age == @max_age'),'\n')

#checking the youngest customers, both male and female
min_age = df['customer_age'].min()
print(df.query('sex == "Male" & customer_age == @min_age'), '\n')
print(df.query('sex == "Female" & customer_age == @min_age'))

#checking the customers with the highest tenure
print(df.loc[df['tenure'].idxmax()],'\n')

max_tenure = df['tenure'].max()
print(df.query('sex == "Male" & tenure == @max_tenure'),'\n')

female_max_tenure = df.query('sex == "Female"')['tenure'].max()
print(df.query('sex == "Female" & tenure == @female_max_tenure'))

#checking customers with lowest tenure
print(df.loc[df['tenure'].idxmin()])

#becasue a female holds the smallest tenure , now we need to check which male has the smallest tenure
min_male_tenure = df.query('sex == "Male"')['tenure'].min()
print(df.query('sex == "Male" & tenure == @min_male_tenure'))

#plotting a graph to show the count of customers by gender
df['sex'].value_counts().plot(kind='bar', title="Male and Female customers")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()