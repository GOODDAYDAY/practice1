from common.constants.name_constants import *
from common.parents.room_parent import room_parent
from game.four_stone import game_contants
from game.four_stone import game_generate_json


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
        if data[INFO][ACTION] == game_contants.MOVE:
            # room_start means game start,send start and turn message to client
            if self.game_info.move_footman(
                    data[INFO][MOVE_TURN], data[INFO][MOVE_POSITION_INIT], data[INFO][MOVE_POSITION_MOVE]
            ):
                for user_id in self.user_list:
                    self.send_to_server(
                        game_generate_json.generate_move_response(
                            user_id, data[INFO][MOVE_TURN], data[INFO][MOVE_POSITION_INIT],
                            data[INFO][MOVE_POSITION_MOVE], self.room_id
                        )
                    )
