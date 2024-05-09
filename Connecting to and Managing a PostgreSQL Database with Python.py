import psycopg2

# Database connection parameters
host = "localhost"  # or the appropriate hostname if not local
database = "PythonClass"
user = "postgres"
password = "your password"

# Connection string
conn_string = f"host={host} dbname={database} user={user} password={password}"

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print("Connected to the database.")

    # Create table Python_GroupA
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Python_GroupA (
        ID CHAR(4) PRIMARY KEY,
        Firstname VARCHAR(255),
        Surname VARCHAR(255),
        Position VARCHAR(255),
        Gender CHAR(6),
        RegistrationDate DATE,
        Status VARCHAR(10)
    );
    """)
    print("Table 'Python_GroupA' created successfully.")

    # Insert data into Python_GroupA table
    cursor.execute("""
    INSERT INTO Python_GroupA (ID, Firstname, Surname, Position, Gender, RegistrationDate, Status) 
    VALUES ('0001', 'Farshid', 'Keivanian', 'Teacher', 'Male', '2024-05-04', 'Online')
    ON CONFLICT (ID) DO NOTHING;
    """)
    conn.commit()
    print("Data inserted into 'Python_GroupA' table successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if conn:
        conn.close()
        print("Database connection closed.")
