import json
import time

from common.constants.event_number import *
from common.constants.name_constants import *


def generate_basic_json(code, login_id, info: dict = None):
    temp_ele = {
        CODE: code,
        LOGIN_ID: login_id,
        INFO: info,
        TIMESTAMP: int(time.time())
    }
    return json.dumps(temp_ele)


def generate_login(name, id):
    info = {
        LOGIN_NAME: name
    }
    return generate_basic_json(LOGIN, id, info)


def generate_login_response(id, name):
    info = {
        LOGIN_NAME: name
    }
    return generate_basic_json(LOGIN_RESPONSE, id, info)


def generate_double_login_response(id, name):
    info = {
        LOGIN_NAME: name
    }
    return generate_basic_json(DOUBLE_LOGIN_RESPONSE, id, info)


def generate_show_data(id):
    return generate_basic_json(SHOW_DATA, id)


def generate_logout(id, name):
    info = {
        LOGIN_NAME: name
    }
    return generate_basic_json(LOGOUT, id, info)


def generate_match(id, game_id):
    info = {
        GAME_ID: game_id
    }
    return generate_basic_json(MATCH, id, info)


def generate_match_response(id):
    return generate_basic_json(MATCH_RESPONSE, id)


def generate_match_withdraw(id):
    # TODO add this logic
    return generate_basic_json(MATCH_WITHDRAW, id)


def generate_match_withdraw_response(id):
    return generate_basic_json(MATCH_WITHDRAW_RESPONSE, id)


def generate_start(id, turn, room_id, game_id):
    info = {
        MOVE_TURN: turn,
        ROOM: room_id,
        GAME_ID: game_id
    }
    return generate_basic_json(ROOM_START, id, info)


def generate_game_info(id, info):
    return generate_basic_json(GAME_CODE, id, info)


def generate_room_info(room_id, info):
    return generate_basic_json(ROOM_CODE, room_id, info)
