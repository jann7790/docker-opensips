from flask import Flask, request, jsonify
import mysql.connector
import os





db = mysql.connector.connect(
    host=os.environ['SQL_IP'],
    user="newuser",
    password="newpassword",
    database="opensips"
)



app = Flask(__name__)
sip_ip = os.environ['HOST_IP']




@app.route('/store/app/set_push_id/', methods=['POST'])
def set_push_id():
    response_data ={
    "success": 1,
    "message": "Firebase token updated successfully"
    }

    return response_data




@app.route('/verify/', methods=['POST'])
def verify():
    phone = request.form.get('phone')
    code = request.form.get('code')

    # Perform any necessary verification logic here
    # ...

    # Replace the following lines with your actual implementation
    success = 1  # Replace with the actual success value
    message = 'Verification successful'  # Replace with the actual message
    response_data = {
    "status": 1,
    "token": "example_token",
    "data": [
        {
        "reg_line": "1",
        "li_name": "John",
        "num": "123456",
        "uid": "user123",
        "pwd": "password123",
        "ip": sip_ip,
        "unit": "unit123",
        "unit_name": "Community A",
        "is_guard": 1,
        "nfc_code": "nfc123"
        },
        {
        "reg_line": "2",
        "li_name": "Jane",
        "num": "789012",
        "uid": "user456",
        "pwd": "password456",
        "ip": sip_ip,
        "unit": "unit456",
        "unit_name": "Community B",
        "is_guard": 0,
        "nfc_code": "nfc456"
        }
    ]
    }

    print(response_data)
    return jsonify(response_data)




@app.route('/reqpin/', methods=['POST'])
def send_phone():
    print(request.form)
    phone = request.form.get('phone')
    device_token = request.form.get('deviceToken')

    is_community = "0"  # Replace with the logic to determine the value of is_community

    data = {
        'phone': phone,
        'is_community': is_community
    }

    getFromsql = 1
    success = 1
    if success == 1:
        message = "已發送驗證碼"
    elif success == -1:
        message = "驗證碼已發送，請５分鐘後再發送"
    elif success == -2:
        message = "簡訊發送失敗，請稍後再發送驗證碼"
    elif success == -3:
        message = "該帳號已使用過，欲重新使用請聯絡電信商再次開通。"
    else:
        message = "號碼不存在資料庫中"

    print('rturn success: ' + str(success) + ' message: ' + message)

    return jsonify({
        'status': success,
        'message': 'Send phone success: ' + message,
        'data': 'this si data'
    })





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
    app.run(debug=True, host='0.0.0.0', port=80)