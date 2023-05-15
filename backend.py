import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="newuser",
    password="newpassword",
    database="opensips"
)

# flush privileges
# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute a simple query
query = "SELECT table_name FROM information_schema.tables"
cursor.execute(query)

# Fetch all rows from the result set
rows = cursor.fetchall()

# Display the data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
