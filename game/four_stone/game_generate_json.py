from common.constants.event_number import *
from common.constants.name_constants import *
from common.utils.generate_json import generate_basic_json
from game.four_stone.game_contants import *


def generate_move(id, turn, position_init, position_move, room_id):
    info = {
        ACTION: MOVE,
        MOVE_TURN: turn,
        MOVE_POSITION_INIT: position_init,
        MOVE_POSITION_MOVE: position_move,
        ROOM: room_id
    }
    return generate_basic_json(ROOM_CODE, id, info)


def generate_move_response(id, position_init, position_move):
    info = {
        ACTION: MOVE_RESPONSE,
        MOVE_POSITION_INIT: position_init,
        MOVE_POSITION_MOVE: position_move
    }
    return generate_basic_json(ROOM_CODE, id, info)
