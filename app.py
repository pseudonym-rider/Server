from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, create_refresh_token, get_jwt_identity, jwt_refresh_token_required
)
import config
import encryption as crypt

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = config.key
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = config.access
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = config.refresh

jwt = JWTManager(app)


@app.route('/join', methods=['POST'])
def join():
    req = request.get_json()
    req['user_pw'] = crypt.encryption(req['user_pw'])

    conn = MongoClient(config.ip)
    db = conn.main_server
    mem_list = db.member

    id_check = mem_list.find({'user_id': req['user_id']}).count()

    if id_check != 0:
        return jsonify({"code": 1, "msg": "Duplicate ID exists"}), 401

    if req['type'] == '2':
        mem_list.insert({
            "user_id": req['user_id'],
            "user_pw": req['user_pw'],
            "user_name": req['user_name'],
            "phone": req['phone'],
            "birth": req['birth'],
            "gender": req['gender'],
            "type": req['type'],
            "license": req['license']
        })
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


@app.route('/auth', methods=['POST'])
def auth():
    req = request.get_json()

    conn = MongoClient(config.ip)
    db = conn.main_server
    mem_list = db.member

    result = mem_list.find_one({'user_id': req['user_id']})
    if result is None :
        return jsonify({"code": "1", "msg": "No matching ID or PW exists"}), 401
    if not crypt.compare(req['user_pw'], result['user_pw']):
        return jsonify({"code": "1", "msg": "No matching ID or PW exists"}), 401

    del result['_id']
    access_token = create_access_token(identity=req['user_id'])
    refresh_token = create_refresh_token(identity=req['user_id'])

    return jsonify(
        code=0,
        msg='login success',
        user_name=result['user_name'],
        type=result['type'],
        access_token=access_token,
        refresh_token=refresh_token
    ), 200


@app.route('/refresh', methods=['GET'])
@jwt_refresh_token_required
def refresh():
    access_token = create_access_token(identity=get_jwt_identity())
    return jsonify(access_token=access_token, user_id=get_jwt_identity())


@app.route('/get_info', methods=['GET'])
@jwt_required
def getInfo():
    conn = MongoClient(config.ip)
    db = conn.main_server
    mem_list = db.member
    
    result = mem_list.find_one({'user_id': get_jwt_identity()})

    return jsonify(
        user_id=result['user_id'],
        user_name=result['user_name'],
        phone=result['phone'],
        birth=result['birth'],
        gender=result['gender'],
        type=result['type']
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.port)
