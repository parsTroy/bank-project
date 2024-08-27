import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine, text

# Connect to the SQL Server database
conn_str = ('mssql+pyodbc://localhost/BankDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes')
engine = create_engine(conn_str)

# Query to get customer data
query = """
SELECT CustomerID, Age, Income, CreditScore
FROM Customers
"""

# Read data from SQL Server into a pandas DataFrame
with engine.connect() as connection:
    df = pd.read_sql(query, connection)

# Preprocessing
scaler = StandardScaler()
X = scaler.fit_transform(df[['Age', 'Income', 'CreditScore']])

# K-means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# Visualize the clusters
plt.figure(figsize=(12, 8))
sns.scatterplot(data=df, x='Income', y='CreditScore', hue='Cluster', style='Cluster', palette='deep')
plt.title('Customer Segments')
plt.savefig('../data/customer_segments.png')
plt.close()

# Calculate cluster centers
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
cluster_centers_df = pd.DataFrame(cluster_centers, columns=['Age', 'Income', 'CreditScore'])
cluster_centers_df['Cluster'] = range(len(cluster_centers_df))

# Print cluster characteristics
print("Cluster Characteristics:")
print(cluster_centers_df)

# Update the Customers table with the new cluster assignments
with engine.connect() as connection:
    for _, row in df.iterrows():
        update_query = text("""
        UPDATE Customers
        SET Cluster = :cluster
        WHERE CustomerID = :customer_id
        """)
        connection.execute(update_query, {"cluster": int(row['Cluster']), "customer_id": int(row['CustomerID'])})
    connection.commit()

print("Customer segmentation complete. Results saved to database and visualization saved as 'customer_segments.png'.")