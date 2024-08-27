import pyodbc

connection_strings = [
    'Driver={ODBC Driver 17 for SQL Server};Server=localhost;Database=master;Trusted_Connection=yes;',
    'Driver={ODBC Driver 17 for SQL Server};Server=(local);Database=master;Trusted_Connection=yes;',
    'Driver={ODBC Driver 17 for SQL Server};Server=127.0.0.1;Database=master;Trusted_Connection=yes;',
    'Driver={SQL Server};Server=localhost;Database=master;Trusted_Connection=yes;',
    'Driver={SQL Server};Server=(local);Database=master;Trusted_Connection=yes;',
    'Driver={SQL Server};Server=127.0.0.1;Database=master;Trusted_Connection=yes;'
]

for conn_str in connection_strings:
    print(f"\nTrying connection string: {conn_str}")
    try:
        conn = pyodbc.connect(conn_str, timeout=5)
        print("Connection successful!")
        conn.close()
        break
    except pyodbc.Error as e:
        print(f"Connection failed: {e}")