import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

print("Script started")

# Get the current working directory
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")

# Construct the full path to the data directory
data_dir = os.path.join(current_dir, 'data')
print(f"Attempted data directory path: {data_dir}")

# Create the data directory if it doesn't exist
os.makedirs(data_dir, exist_ok=True)
print(f"Data directory created/confirmed: {data_dir}")

# Set random seed for reproducibility
np.random.seed(42)

# Generate customer data
print("Generating customer data...")
num_customers = 1000
customer_data = {
    'customer_id': range(1, num_customers + 1),
    'name': [f'Customer_{i}' for i in range(1, num_customers + 1)],
    'age': np.random.randint(18, 80, num_customers),
    'income': np.random.randint(20000, 200000, num_customers),
    'credit_score': np.random.randint(300, 850, num_customers)
}

customers_df = pd.DataFrame(customer_data)

# Generate loan data
print("Generating loan data...")
num_loans = 1500
loan_data = {
    'loan_id': range(1, num_loans + 1),
    'customer_id': np.random.choice(customers_df['customer_id'], num_loans),
    'loan_amount': np.random.randint(5000, 500000, num_loans),
    'interest_rate': np.random.uniform(0.03, 0.15, num_loans),
    'loan_term': np.random.choice([12, 24, 36, 48, 60], num_loans),
    'loan_status': np.random.choice(['current', 'late', 'default'], num_loans, p=[0.8, 0.15, 0.05])
}

loans_df = pd.DataFrame(loan_data)

# Save data to CSV files
customers_file = os.path.join(data_dir, 'customers.csv')
loans_file = os.path.join(data_dir, 'loans.csv')

print(f"Saving customers data to: {customers_file}")
customers_df.to_csv(customers_file, index=False)
print("Customers data saved successfully")

print(f"Saving loans data to: {loans_file}")
loans_df.to_csv(loans_file, index=False)
print("Loans data saved successfully")

print("Data generation complete. Check the 'data' folder for customers.csv and loans.csv files.")