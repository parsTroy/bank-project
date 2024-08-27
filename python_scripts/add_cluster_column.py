import pyodbc

conn_str = ('Driver={ODBC Driver 17 for SQL Server};'
            'Server=localhost;'
            'Database=BankDB;'
            'Trusted_Connection=yes;')

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    # Check if Cluster column exists
    cursor.execute("""
    IF NOT EXISTS (
        SELECT * FROM INFORMATION_SCHEMA.COLUMNS 
        WHERE TABLE_NAME = 'Customers' AND COLUMN_NAME = 'Cluster'
    )
    BEGIN
        ALTER TABLE Customers ADD Cluster INT
    END
    """)
    
    conn.commit()
    print("Cluster column added successfully (if it didn't exist already).")
    
    conn.close()
except pyodbc.Error as e:
    print(f"An error occurred: {e}")