import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure the data directory exists
data_dir = os.path.join(os.getcwd(), 'data')
os.makedirs(data_dir, exist_ok=True)

try:
    # Load the data
    customers_df = pd.read_csv(os.path.join(data_dir, 'customers.csv'))
    loans_df = pd.read_csv(os.path.join(data_dir, 'loans.csv'))

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
    plt.savefig(os.path.join(data_dir, 'age_distribution.png'))
    plt.close()
    print("Age distribution plot saved.")

    # Visualize loan amount distribution
    plt.figure(figsize=(10, 6))
    loans_df['loan_amount'].hist(bins=20)
    plt.title('Loan Amount Distribution')
    plt.xlabel('Loan Amount')
    plt.ylabel('Count')
    plt.savefig(os.path.join(data_dir, 'loan_amount_distribution.png'))
    plt.close()
    print("Loan amount distribution plot saved.")

    # Visualize loan status distribution
    loan_status_counts = loans_df['loan_status'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(loan_status_counts.values, labels=loan_status_counts.index, autopct='%1.1f%%')
    plt.title('Loan Status Distribution')
    plt.savefig(os.path.join(data_dir, 'loan_status_distribution.png'))
    plt.close()
    print("Loan status distribution plot saved.")

    print("Data exploration complete. Check the 'data' folder for generated visualizations.")

except Exception as e:
    print(f"An error occurred: {str(e)}")