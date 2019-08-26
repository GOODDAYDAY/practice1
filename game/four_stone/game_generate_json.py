from common.constants.name_constants import *
from game.four_stone.game_contants import *

import json
import time


def generate_move(id, turn, position_init, position_move, room_id):
    temp_ele = {
        CODE: MOVE,
        LOGIN_ID: id,
        MOVE_TURN: turn,
        MOVE_POSITION_INIT: position_init,
        MOVE_POSITION_MOVE: position_move,
        ROOM: room_id,
        TIMESTAMP: int(time.time() / 1000)
    }
    return json.dumps(temp_ele)


def generate_move_response(position_init, position_move):
    temp_ele = {
        CODE: MOVE_RESPONSE,
        MOVE_POSITION_INIT: position_init,
        MOVE_POSITION_MOVE: position_move,
        TIMESTAMP: int(time.time() / 1000)
    }
    return json.dumps(temp_ele)
