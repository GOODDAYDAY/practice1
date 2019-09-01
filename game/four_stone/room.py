from common.constants.event_number import *
from common.constants.name_constants import *
from common.parents.room_parent import room_parent


class four_stone_room(room_parent):
    def __init__(self, room_id: str, game_id: str, user_list: list, server):
        super().__init__(room_id, game_id, user_list, server)

    def distribute_turn(self) -> list:
        """
        need room_impl to implement it, it distribute id and its turn
        :return: [[id,turn],[id,turn],[id,turn]]
        """
        return [[self.user_list[i], i] for i in range(len(self.user_list))]

    def filter(self, data: dict, *args, **kwargs):
        """
        the filter in room,and filer feature is ACTION
        """
        # print or log data
        print(data)
        # main filter
        if data[ACTION] == ROOM_START:
            # room_start means game start,send start and turn message to client
            pass
        elif data[ACTION] == GAME_CODE:
            # game code is send message to game
            pass
        elif data[ACTION] == ROOM_CODE:
            # game code is send message to room,but it need to send to server first
            pass
