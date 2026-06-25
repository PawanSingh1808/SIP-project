# SIP-project
# Telco Customer Churn Data Analysis

This project focuses on Exploratory Data Analysis (EDA) of the Telco Customer Churn dataset. The objective is to identify key factors that influence customer churn, analyze customer behavior, and uncover trends that can help the telecom company improve customer retention.

## Project Overview

Customer churn occurs when customers stop doing business with a company. In the telecom industry, retaining existing customers is often more cost-effective than acquiring new ones. This data analysis provides insights into:
* Customer demographics and attributes (Gender, Senior Citizen status, Partner, Dependents).
* Account characteristics (Tenure Months, Contract Type, Paperless Billing, Payment Method, Charges).
* Subscribed services (Internet Service, Tech Support, Online Security, etc.).
* Core drivers leading to customer churn.

---

## Dataset Description

The dataset used in this project is `Telco_customer_churn.xlsx`. It consists of **7,043 rows** and **33 columns**, containing customer-level information from a fictional telecom company in California.

### Key Features Analyzed:
* **CustomerID**: Unique identifier for each customer.
* **Tenure Months**: Number of months the customer has stayed with the company.
* **Monthly Charges**: The amount charged to the customer monthly.
* **Total Charges**: The total amount charged to the customer.
* **Contract**: The contract term of the customer (Month-to-month, One year, Two year).
* **Payment Method**: The customer’s payment method (Electronic check, Mailed check, Bank transfer, Credit card).
* **Churn Label**: Indicates whether the customer left the company or not (Yes or No).

---

## Requirements

To run this project locally, ensure you have Python installed along with the following libraries:

* **pandas** (for data manipulation and loading Excel files)
* **numpy** (for numerical computations)
* **matplotlib** (for static plotting)
* **seaborn** (for statistical data visualizations)
* **openpyxl** (required by pandas to read `.xlsx` files)
