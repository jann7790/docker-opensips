from flask import Flask
import mysql.connector
 
db = mysql.connector.connect(
    host="192.168.112.135",
    user="newuser",
    password="newpassword",
    database="opensips"
)


app = Flask(__name__)
 
 
@app.route('/')
def hello_world():
    return 'Flask Dockerized'


@app.route("/sql")
def home():
    cursor = db.cursor()
    query = "SELECT table_name FROM information_schema.tables"

    cursor.execute(query)
    data = cursor.fetchall()
    
    return str(data)

 
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)