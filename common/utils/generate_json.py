from common.constants.name_constants import *
from common.constants.event_number import *

import json
import time


def generate_login(name, id):
    temp_ele = {
        CODE: LOGIN,
        LOGIN_ID: id,
        LOGIN_NAME: name,
        TIMESTAMP: int(time.time() / 1000)

    }
    return json.dumps(temp_ele)


def generate_login_response(id, name):
    temp_ele = {
        CODE: LOGIN_RESPONSE,
        LOGIN_ID: id,
        LOGIN_NAME: name,
        TIMESTAMP: int(time.time() / 1000)
    }
    return json.dumps(temp_ele)


def generate_double_login_response(id, name):
    temp_ele = {
        CODE: DOUBLE_LOGIN_RESPONSE,
        LOGIN_ID: id,
        LOGIN_NAME: name,
        TIMESTAMP: int(time.time() / 1000)
    }
    return json.dumps(temp_ele)


def generate_show_data():
    temp_ele = {
        CODE: SHOW_DATA,
        TIMESTAMP: int(time.time() / 1000)
    }
    return json.dumps(temp_ele)


def generate_logout(id, name):
    temp_ele = {
        CODE: LOGOUT,
        LOGIN_ID: id,
        LOGIN_NAME: name,
        TIMESTAMP: int(time.time() / 1000)
    }
    return json.dumps(temp_ele)


def generate_match(id, game):
    temp_ele = {
        CODE: MATCH,
        LOGIN_ID: id,
        GAME: game,
        TIMESTAMP: int(time.time() / 1000)
    }
    return json.dumps(temp_ele)


def generate_match_response(id):
    temp_ele = {
        CODE: MATCH_RESPONSE,
        LOGIN_ID: id,
        TIMESTAMP: int(time.time() / 1000)
    }
    return json.dumps(temp_ele)


def generate_match_withdraw(id):
    temp_ele = {
        CODE: MATCH_WITHDRAW,
        LOGIN_ID: id,
        TIMESTAMP: int(time.time() / 1000)
    }
    return json.dumps(temp_ele)


def generate_match_withdraw_response(id):
    temp_ele = {
        CODE: MATCH_WITHDRAW_RESPONSE,
        LOGIN_ID: id,
        TIMESTAMP: int(time.time() / 1000)
    }
    return json.dumps(temp_ele)


def generate_start(id, turn, room_id, game_id):
    temp_ele = {
        CODE: ROOM_START,
        LOGIN_ID: id,
        MOVE_TURN: turn,
        ROOM: room_id,
        GAME: game_id,
        TIMESTAMP: int(time.time() / 1000)
    }
    return json.dumps(temp_ele)


def generate_game_info(id, info):
    temp_ele = {
        CODE: GAME_CODE,
        LOGIN_ID: id,
        INFO: info,
        TIMESTAMP: int(time.time() / 1000)
    }
    return json.dumps(temp_ele)


def generate_room_info(room_id, info):
    temp_ele = {
        CODE: ROOM_CODE,
        ROOM: room_id,
        INFO: info,
        TIMESTAMP: int(time.time() / 1000)
    }
    return json.dumps(temp_ele)
