import json

from flask import Flask, request, jsonify

from user_database import UserDatabase, UserNotFoundError
from death_database import DeathDatabase
from born_database import BornDatabase
from marriage_database import MarriageDatabase
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
death_db = DeathDatabase()
born_db = BornDatabase()
user_db = UserDatabase()
marriage_db = MarriageDatabase()


def check_password(request_data):
    return user_db.check_password(request_data['user_id'], request_data['password'])


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_info(user_id):
    if not check_password(json.loads(request.data)):
        return {'status': 'error', 'message': 'wrong user or password'}
    try:
        return {'status': 'ok', 'role': user_db.get_user_role(user_id)}
    except UserNotFoundError:
        return {'status': 'error', 'message': 'wrong user or password'}


@app.route('/users/auth', methods=['POST'])
def auth():
    data = json.loads(request.data)
    if not user_db.check_password(data['user_id'], data['password']):
        return {'status': 'error', 'message': 'wrong user or password'}
    try:
        return {'status': 'ok', 'role': user_db.get_user_role(data['user_id'])}
    except UserNotFoundError:
        return {'status': 'error', 'message': 'wrong user or password'}



@app.route('/death', methods=['GET'])
def get_death():
    result = [{'id': id_, 'date': date, 'place': place, 'description': description, 'fio': fio, }
              for id_, date, place, description, fio in death_db.get_death()]
    return jsonify(result)


@app.route('/born', methods=['GET'])
def get_born():
    result = [
        {'id': id_, 'fio': fio, 'date': date, 'gender': gender, 'id_parents': id_parents, 'death_date': death_date}
        for id_, fio, date, gender, id_parents, death_date in born_db.get_born()]
    return jsonify(result)


@app.route('/marriage', methods=['GET'])
def get_marriage():
    result = [{'id': id_, 'fio_husband': fio_husband, 'fio_wife': fio_wife, 'date': date, 'date_divorce': date_divorce,
               'id_husband': id_husband, 'id_wife': id_wife}
              for id_, fio_husband, fio_wife, date, date_divorce, id_husband, id_wife in marriage_db.get_marriage()]
    return jsonify(result)


@app.route('/marriage/<string:key>/<string:value>/get', methods=['GET'])
def get_marriage_key(key, value):
    result = [{'id': id_, 'fio_husband': fio_husband, 'fio_wife': fio_wife, 'date': date, 'date_divorce': date_divorce}
              for id_, fio_husband, fio_wife, date, date_divorce in marriage_db.get_marriage_key(key, value)]
    return jsonify(result)


@app.route('/death/<string:key>/<string:value>/get', methods=['GET'])
def get_death_key(key, value):
    result = [{'id': id_, 'date': date, 'place': place, 'description': description, 'fio': fio}
              for id_, date, place, description, fio in death_db.get_death_key(key, value)]
    return jsonify(result)


@app.route('/born/<string:key>/<string:value>/get', methods=['GET'])
def get_born_key(key, value):
    result = [
        {'id': id_, 'fio': fio, 'date': date, 'gender': gender, 'id_parents': id_parents, 'death_date': death_date}
        for id_, fio, date, gender, id_parents, death_date in born_db.get_born_key(key, value)]
    return jsonify(result)


@app.route('/death', methods=['POST'])
def add_new_death() -> bool:
    if not request.is_json:
        return {"status": "error", "message": "no json sent"}
    data = json.loads(request.data)
    death_db.add_new_death(data['id'], data['date'], data['place'], data['description'])
    return {"status": "ok"}


@app.route('/born', methods=['POST'])
def add_new_born() -> bool:
    if not request.is_json:
        return {"status": "error", "message": "no json sent"}
    data = json.loads(request.data)
    born_db.add_new_born(data['fio'], data['date'], data['gender'], data['id_parents'])
    return {"status": "ok"}


@app.route('/marriage', methods=['POST'])
def add_new_marriage() -> bool:
    if not request.is_json:
        return {"status": "error", "message": "no json sent"}
    data = json.loads(request.data)
    marriage_db.add_new_marriage(data['id_husband'], data['id_wife'], data['date'])
    return {"status": "ok"}


@app.route('/death/<int:death_id>/delete', methods=['DELETE'])
def delete_death(death_id) -> bool:
    death_db.delete_death(death_id)
    return {"status": "ok"}


@app.route('/born/<int:born_id>/delete', methods=['DELETE'])
def delete_born(born_id) -> bool:
    born_db.delete_born(born_id)
    return {"status": "ok"}


@app.route('/marriage/<int:marriage_id>/delete', methods=['DELETE'])
def delete_marriage(marriage_id) -> bool:
    marriage_db.delete_marriage(marriage_id)
    return {"status": "ok"}


@app.route('/death/<int:death_id>/edit', methods=['POST'])
def edit_death(death_id):
    if not request.is_json:
        return {"status": "error", "message": "no json sent"}
    data = json.loads(request.data)
    death_db.edit_death(death_id, data['date'], data['place'], data['description'])
    return {"status": "ok"}


@app.route('/born/<int:born_id>/edit', methods=['POST'])
def edit_born(born_id):
    if not request.is_json:
        return {"status": "error", "message": "no json sent"}
    data = json.loads(request.data)
    born_db.edit_born(born_id, data['fio'], data['date'], data['gender'], data['id_parents'])
    return {"status": "ok"}


@app.route('/marriage/<int:marriage_id>/edit', methods=['POST'])
def edit_marriage(marriage_id):
    if not request.is_json:
        return {"status": "error", "message": "no json sent"}
    data = json.loads(request.data)
    marriage_db.edit_marriage(marriage_id, data['id_husband'], data['id_wife'], data['date'])
    return {"status": "ok"}


@app.route('/marriage/<int:marriage_id>/edit/divorce', methods=['POST'])
def edit_marriage_push_divorce(marriage_id):
    if not request.is_json:
        return {"status": "error", "message": "no json sent"}
    data = json.loads(request.data)
    marriage_db.edit_marriage_push_divorce(marriage_id, data['date_divorce'])
    return {"status": "ok"}


if __name__ == '__main__':
    app.run()
