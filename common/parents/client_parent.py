import json
import threading

from common.constants.event_number import *
from common.constants.game_content import game_dict
from common.constants.name_constants import *
from common.parents.user_parent import user_parent
from common.utils import generate_json


class client_parent():
    def __int__(self, user: user_parent):
        # self user which is the client's user
        self.user = user
        # game main method
        self.game = None

    def get_message(self, *args, **kwargs):
        """
        get message in some way,child need implement it.
        Then send message to filter
        """

    def send_to_server(self, message: str):
        """
        send message in some way,child need implement it.
        :param message: str
        """

    def send_to_game(self, message: str):
        """
        send message to game
        :param message:
        """
        self.game.filter(message)

    def login(self):
        """
        in the beginning,send login information to server
        """
        self.send_to_server(generate_json.generate_login(self.user.name, self.id))

    def filter(self, data: dict, info=None):
        """
        message from method:get_message transfer to filter.Client
        will do something with filter
        :param message: str and from method:get_message
        """
        # print or log data
        print(data)
        # main filter
        if data[CODE] == LOGIN_RESPONSE:
            # login response
            self.login_success(data[LOGIN_NAME], data[LOGIN_ID])
        elif data[CODE] == MATCH_RESPONSE:
            # match response make user
            pass
        elif data[CODE] == ROOM_START:
            # room_start means game start,receive game info and start game
            th = threading.Thread(target=self.game_start, args=(data[MOVE_TURN], data[ROOM], data[GAME]))
            th.daemon = True
            th.start()
        elif data[CODE] == GAME_CODE:
            # game code is send message to game
            self.send_to_game(data[INFO])
        elif data[CODE] == ROOM_CODE:
            # game code is send message to room,but it need to send to server first
            self.send_to_server(json.dumps(data))

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
        self.game = self.game(turn, self.id, room)
        self.game.run()
