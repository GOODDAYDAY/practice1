from common.parents.client_parent import client_parent


class game_parent():
    def __init__(self, game_id, room_id, client: client_parent = None):
        self.game_id = game_id
        self.room_id = room_id
        self.client = client
        # there need a game_info
        # self.game_info = game_info

    def set_client(self, client: client_parent):
        self.client = client

    def close(self):
        exit()

    def send_to_client(self, message):
        """
        send message to server
        :param message:
        :return:
        """
        self.client.filter(message)

    def run(self):
        """
        need to override
        :return:
        """

    def game_message_filter(self, data: dict):
        """
        charge which action to do with different data
        :param data:
        """

    def filter(self, data: dict, *args, **kwargs):
        """
        need to override by implement
        :param data:
        """
