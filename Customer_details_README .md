# E-commerce Customer Data Analysis

This repository contains  data cleaning and exploratory analysis of customer details from an e-commerce dataset. 
The analysis focuses on age, gender, and tenure of customers, with data preprocessing to handle anomalies and insightful visualizations.

---

## Dataset Overview

The dataset (`customer_details.xlsx`) contains the following columns:
                              

--> customer_id  - Unique identifier for each customer      
--> sex          - Gender of the customer (`Male` / `Female`) 
--> customer_age - Age of the customer (in years)           
--> tenure       - Customer tenure in months                

---

## Key Findings

- Cleaned invalid gender entries (`"UNKNOWN"`, `"kvkktalepsilindi"`) → mapped to `Female` and `Male`
- Fixed negative and unrealistic ages:
  - Ages < 18 → replaced with 24
  - Ages > 100 → replaced with 44
- Identified:
  - Youngest & oldest customers by gender
  - Customers with highest & lowest tenure
  - Gender distribution via bar chart
