import json
import threading

from common.constants.event_number import *
from common.constants.game_content import game_dict, GAME_BODY_INFO, GAME_BODY
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

    def send_to_game(self, message: dict):
        """
        send message to game
        :param message:
        """
        self.game.filter(message)

    def login(self):
        """
        in the beginning,send login information to server
        """
        self.send_to_server(generate_json.generate_login(self.user.get_name(), self.user.get_user_id()))

    def charge_data(self, data: dict):
        """
        charge if the data input is right for this client
        :param data:
        """
        if data[LOGIN_ID] != self.user.get_user_id():
            return False
        return True

    def filter(self, data: dict, info=None):
        """
        message from method:get_message transfer to filter.Client
        will do something with filter
        :param message: str and from method:get_message
        """
        # print or log data
        print(data)
        # charge if id is right
        if not self.charge_data(data):
            return
        # main filter
        if data[CODE] == LOGIN_RESPONSE:
            # login response
            self.login_success(data[INFO][LOGIN_NAME], data[LOGIN_ID])
        elif data[CODE] == MATCH_RESPONSE:
            # match response make user
            pass
        elif data[CODE] == ROOM_START:
            # room_start means game start,receive game info and start game
            th = threading.Thread(
                target=self.game_start,
                args=(data[INFO][MOVE_TURN], data[INFO][ROOM], data[INFO][GAME_ID]))
            th.daemon = True
            th.start()
        elif data[CODE] == GAME_CODE:
            # game code is send message to game
            self.send_to_game(data)
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
        self.user.user_id = id
        self.user.name = name
        self.user.switch_type_login()

    def game_start(self, turn: int, room: str, game: str):
        """
        the method to start a new game
        :return:
        """
        # run the init method and load the game
        content = game_dict[game]()
        self.game = content[GAME_BODY]
        # run the game
        self.game = self.game(self.user.get_user_id(), room, turn, content[GAME_BODY_INFO], self)
        self.game.run()
