from common.parents.game_info_parent import game_info_parent
from common.parents.server_parent import server_parent
from common.utils.generate_json import generate_start


class room_parent():
    def __init__(self, room_id: str, game_id: str, user_list: list, game_info: game_info_parent, server: server_parent):
        # load user_list to room
        self.user_list = user_list
        # load game info,room can send game_info to clients sync
        self.game_info = game_info
        # load server,so that room can send message to server
        self.server = server
        # self room id
        self.room_id = room_id
        # self game id
        self.game_id = game_id

    def send_to_server(self, message: str):
        """
        send message to server
        """
        self.server.filter(message)

    def room_start(self):
        """
        users are enough,room start and send message to server
        """
        # init game_info
        self.game_info = self.game_info()
        # send to server to all client
        for id, turn in self.distribute_turn():
            self.send_to_server(generate_start(id, turn, self.room_id, self.game_id))

    def room_end(self):
        """
        game end and send message to server
        """
        # delete the game_info
        del self.game_info
        # send data to server

    def distribute_turn(self) -> list:
        """
        need room_impl to implement it, it distribute id and its turn
        :return: [[id,turn],[id,turn],[id,turn]]
        """

    def is_in_room(self, user_id: str):
        """
        check if it is in room
        :param user_id: str which is user_id
        :return: True or False
        """
        return user_id in self.user_list
