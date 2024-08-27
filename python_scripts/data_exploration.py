import pandas as pd
import matplotlib.pyplot as plt

# Load the data
customers_df = pd.read_csv('../data/customers.csv')
loans_df = pd.read_csv('../data/loans.csv')

# Display basic information about the datasets
print("Customer Data Info:")
print(customers_df.info())
print("\nLoan Data Info:")
print(loans_df.info())

# Display summary statistics
print("\nCustomer Data Summary:")
print(customers_df.describe())
print("\nLoan Data Summary:")
print(loans_df.describe())

# Visualize age distribution
plt.figure(figsize=(10, 6))
customers_df['age'].hist(bins=20)
plt.title('Age Distribution of Customers')
plt.xlabel('Age')
plt.ylabel('Count')
plt.savefig('../data/age_distribution.png')
plt.close()

# Visualize loan amount distribution
plt.figure(figsize=(10, 6))
loans_df['loan_amount'].hist(bins=20)
plt.title('Loan Amount Distribution')
plt.xlabel('Loan Amount')
plt.ylabel('Count')
plt.savefig('../data/loan_amount_distribution.png')
plt.close()

# Visualize loan status distribution
loan_status_counts = loans_df['loan_status'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(loan_status_counts.values, labels=loan_status_counts.index, autopct='%1.1f%%')
plt.title('Loan Status Distribution')
plt.savefig('../data/loan_status_distribution.png')
plt.close()

print("Data exploration complete. Check the 'data' folder for generated visualizations.")