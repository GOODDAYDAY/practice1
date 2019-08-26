from common.constants.event_number import *
from common.constants.game_content import game_dict
from common.constants.name_constants import *
from common.parents.game_parent import game_parent
from common.utils import generate_json

import threading
import json


class client_parent():
    def __int__(self, name, id, game: game_parent):
        # self name which is the name in game
        self.name = name
        # self id which is the id before
        self.id = id
        # if it is login
        self.is_login = False
        # game main method
        self.game = None
        # game room
        self.room = None

    def get_message(self):
        """
        get message in some way,child need implement it.
        Then send message to filter
        """

    def filter(self, message: str, info=None):
        """
        message from method:get_message transfer to filter.Client
        will do something with filter
        :param message: str and from method:get_message
        """
        data = json.loads(message)
        print(data)
        if data[CODE] == LOGIN_RESPONSE:
            self.login_success(data[LOGIN_NAME], data[LOGIN_ID])
        elif data[CODE] == ROOM_START:
            th = threading.Thread(target=self.game_start, args=(data[MOVE_TURN], data[ROOM], data[GAME]))
            th.daemon = True
            th.start()

        elif data[CODE] == GAME_CODE:
            self.game.filter(data[INFO])

    def login_success(self, name, id):
        """
        when receive login success
        :param name:
        :param id:
        :return:
        """
        self.name = name
        self.id = id
        self.is_login = True

    def game_start(self, turn: int, room: str, game: str):
        """
        the method to start a new game
        :return:
        """
        # run the init method and load the game
        self.game = game_dict[game]()[1]
        # run the game
        self.game = self.game(turn, self.ws, self.id, room)
        self.game.run()
