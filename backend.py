import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="user",
    password="user",
    database="opensips"
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute a simple query
query = "SELECT * FROM your_table"
cursor.execute(query)

# Fetch all rows from the result set
rows = cursor.fetchall()

# Display the data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
