from flask import Flask, jsonify, request
from pymongo import MongoClient

conn = MongoClient('192.168.0.5')

db = conn.main_server

collect = db.data

app = Flask(__name__)


@app.route('/join', methods=['POST'])
def join():
    req = request.get_json()
    mem_list = db.member

    mem_list.insert({
        "user_id": req['user_id'],
        "user_name": req['user_name'],
        "phone": req['phone'],
        "birth": req['birth'],
        "gender": req['gender'],
        "type": req['type'],
        "IMEI": req['IMEI']
    })

    return jsonify({"code": 0, "msg": "Join success"})

if __name__ == '__main__':
    app.run()
