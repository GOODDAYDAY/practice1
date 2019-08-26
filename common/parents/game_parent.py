from common.parents.client_parent import client_parent


class game_parent():
    def __init__(self, id, room, client: client_parent = None):
        self.id = id
        self.room = room
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

    def filter(self, message, info=None):
        """
        need to override by implement
        :param message:
        """
