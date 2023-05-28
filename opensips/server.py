from flask import Flask, request, jsonify
import os
# from opensipscli import cli, defaults, version
# from opensipscli import args
# import mysql.connector

app = Flask(__name__)
sip_ip = os.environ['HOST_IP']



# db = mysql.connector.connect(
#     host="127.0.0.1",
#     user="newuser",
#     password="newpassword",
#     database="opensips"
# )


# @app.route("/sql")
# def home():
#     cursor = db.cursor()
#     query = "SELECT table_name FROM information_schema.tables"

#     cursor.execute(query)
#     data = cursor.fetchall()
    
#     return str(data)





@app.route('/canmsg/<path:subpath>', methods=['GET'])
def canmsg(subpath):
    print(subpath)
    print(request.form)
    response_data =    {
    "status": 1,
    "unit_CAN": [
        {
        "id": "001",
        "name": "CommunityCan1",
        "content": "This is the content of CommunityCan1."
        },
        {
        "id": "002",
        "name": "CommunityCan2",
        "content": "This is the content of CommunityCan2."
        },
        {
        "id": "003",
        "name": "CommunityCan3",
        "content": "This is the content of CommunityCan3."
        }
    ]
    }

    return jsonify(response_data)




@app.route('/getall/', methods=['POST'])
def getall():
    print(request.form)
    response_data = {
    "status": 1,
    "data": [
        {
        "num": "123456789",
        "li_name": "John Doe",
        "unit": "Unit 1"
        },
        {
        "num": "987654321",
        "li_name": "Jane Smith",
        "unit": "Unit 2"
        }
    ]
    }

    return jsonify(response_data)


@app.route('/store/s_wid/', methods=['POST'])
def s_wid():
    print(request.form)
    response_data = {
      "web_index_list": [
    {
      "store": "Example Store 1",
      "lat": "37.123456",
      "lon": "-122.987654",
      "photo": "example1.jpg",
      "web_id": "store1",
      "address": "123 Example Street",
      "owner": "John Doe",
      "subtype": "1",
      "phone": "123-456-7890",
      "intro": "Welcome to Example Store 1",
      "business_hours": "9 AM - 6 PM",
      "good_news": "New arrivals just in!",
      "internet_phone": "example1.sip",
      "shopping_link": "https://examplestore1.com"
    },
    {
      "store": "Example Store 2",
      "lat": "38.987654",
      "lon": "-121.123456",
      "photo": "example2.jpg",
      "web_id": "store2",
      "address": "456 Sample Avenue",
      "owner": "Jane Smith",
      "subtype": "2",
      "phone": "987-654-3210",
      "intro": "Discover the best deals at Example Store 2",
      "business_hours": "10 AM - 8 PM",
      "good_news": "Limited time offer: 50% off",
      "internet_phone": "example2.sip",
      "shopping_link": "https://examplestore2.com"
    }
    ]
    }

    return jsonify(response_data)


@app.route('/adtab_download/', methods=['POST'])
def adtab_download():
    print(request.form)
    response_data =    {
    "status": 1,
    "data": [
        {
        "num": "001",
        "li_name": "John Doe",
        "unit": "A123"
        },
        {
        "num": "002",
        "li_name": "Jane Smith",
        "unit": "B456"
        },
        {
        "num": "003",
        "li_name": "Alice Johnson",
        "unit": "C789"
        }
    ]
    }

    return jsonify(response_data)

@app.route('/store/get_type_info/', methods=['GET'])
def get_type_info():
    print(request.form)
 
    response_data = {
    "type_info": {
        "parent_types": [
        {
            "id": "1",
            "name": "this is name ",
            "icon": "https://variety.com/wp-content/uploads/2023/04/Twitter-Logo-Doge-Dogecoin.png"
        },
        {
            "id": "2",
            "name": "Category 2",
            "icon": "https://variety.com/wp-content/uploads/2023/04/Twitter-Logo-Doge-Dogecoin.png"
        }
        ],
        "subtypes_map": {
        "1": [
            {
            "id": "11",
            "pid": "1",
            "name": "Subcategory 1-1",
            "icon": "https://variety.com/wp-content/uploads/2023/04/Twitter-Logo-Doge-Dogecoin.png"
            },
            {
            "id": "12",
            "pid": "1",
            "name": "Subcategory 1-2",
            "icon": "https://variety.com/wp-content/uploads/2023/04/Twitter-Logo-Doge-Dogecoin.png"
            }
        ],
        "2": [
            {
            "id": "21",
            "pid": "2",
            "name": "Subcategory 2-1",
            "icon": "https://variety.com/wp-content/uploads/2023/04/Twitter-Logo-Doge-Dogecoin.png"
            },
            {
            "id": "22",
            "pid": "2",
            "name": "Subcategory 2-2",
            "icon": "https://variety.com/wp-content/uploads/2023/04/Twitter-Logo-Doge-Dogecoin.png"
            }
        ]
        }
    }
    }

    return response_data

@app.route('/ad/search_ad/', methods=['POST'])
def serach_ad():
    print(request.form)
    response_data = {
    "status": 1,
    "errormsg": "",
    "message": "",
    "data": [
        {
        "store_url": "https://twitter.com/store1",
        "board_type": 1,
        "image_url": "https://cdni.blockcast.it/wp-content/uploads/2023/04/04141000/Doge-450x300.webp",
        "due_date": "2023-06-30",
        "type": 1,
        "id": "ad1"
        },
        {
        "store_url": "https://google.com/",
        "board_type": 2,
        "image_url": "https://variety.com/wp-content/uploads/2023/04/Twitter-Logo-Doge-Dogecoin.png?w=640",
        "due_date": "2023-07-15",
        "type": 2,
        "id": "ad2"
        }
    ]
    }

    return response_data


@app.route('/check/', methods=['POST'])
def loginCheck():
    print(request.form)
    response_data = {
    "status": 1,
    "nfc_code": "nfc123",
    "valids": {
        "1": 1,
        "2": 0,
        "3": 1,
        "4": 0,
        "5": 1
    }
    }


    return response_data




@app.route('/store/app/set_push_id/', methods=['POST'])
def set_push_id():
    print(request.form)
    response_data ={
    "success": 1,
    "message": "Firebase token updated successfully"
    }

    return response_data




@app.route('/verify/', methods=['POST'])
def verify():
    print(request.form)
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
        "num": "1000",
        "uid": "1000",
        "pwd": "123456",
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


    return jsonify({
        'status': success,
        'message': 'Send phone success: ' + message,
        'data': 'this is data'
    })





@app.route('/')
def hello_world():
    return 'Flask Dockerized'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)