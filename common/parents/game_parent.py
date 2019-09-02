import json

from common.parents.client_parent import client_parent
from common.parents.game_info_parent import game_info_parent


class game_parent():
    def __init__(self, user_id, room_id, turn, game_info: game_info_parent, client: client_parent = None):
        # the user_id
        self.user_id = user_id
        # the room'id
        self.room_id = room_id
        # this game's turn
        self.turn = turn
        # the client this game combine
        self.client = client
        # there need a game_info
        self.game_info = game_info
        # exit pram
        self.exit_pram = False

    def set_client(self, client: client_parent):
        self.client = client

    def close(self):
        """
        a way to exit,it should be used in run
        """
        if self.exit_pram:
            exit()

    def send_to_client(self, message):
        """
        send message to server
        :param message:
        :return:
        """
        self.client.filter(json.loads(message))

    def run(self):
        """
        need to override
        :return:
        """

    def filter(self, data: dict, *args, **kwargs):
        """
        need to override by implement
        :param data:
        """
