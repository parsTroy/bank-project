import pyodbc

conn_str = ('Driver={ODBC Driver 17 for SQL Server};'
            'Server=localhost;'
            'Database=master;'
            'Trusted_Connection=yes;')

try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    
    # Check if BankDB exists
    cursor.execute("SELECT name FROM sys.databases WHERE name = 'BankDB'")
    if cursor.fetchone():
        print("BankDB exists.")
    else:
        print("BankDB does not exist. You need to create it.")
    
    conn.close()
except pyodbc.Error as e:
    print(f"An error occurred: {e}")