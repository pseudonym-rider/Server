from flask import Flask, jsonify, request
from pymongo import MongoClient

conn = MongoClient('192.168.35.213')

db = conn.main_server

collect = db.data

app = Flask(__name__)


@app.route('/join', methods=['POST'])
def join():
    req = request.get_json()
    mem_list = db.member
    id_check = mem_list.find({'IMEI': req['user_id']}).count()

    if id_check != 0:
        return jsonify({"code": 1, "msg": "Failed join"}), 401

    mem_list.insert({
        "user_id": req['user_id'],
        "user_pw": req['user_pw'],
        "user_name": req['user_name'],
        "phone": req['phone'],
        "birth": req['birth'],
        "gender": req['gender'],
        "type": req['type']
    })

    return jsonify({"code": 0, "msg": "Join success"})


@app.route('/login', methods=['POST'])
def login():
    req = request.get_json()
    mem_list = db.member

    result = mem_list.find_one({'user_id': req['user_id'], 'user_pw': req['user_pw']})
    if result is None:
        return jsonify({"code": "1", "msg": "No matching ID or PW exists"}), 401

    del result['_id']
    print(result)
    return jsonify({'code': '0', 'msg': 'login success'}), 200


if __name__ == '__main__':
    app.run()
