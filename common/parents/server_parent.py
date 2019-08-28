import copy

from common.constants.event_number import *
from common.constants.game_content import game_dict, MATCH_SIZE, GAME_ROOM, GAME_BODY_INFO
from common.constants.name_constants import *
from common.parents.room_parent import room_parent
from common.parents.user_parent import user_parent
from common.utils import generate_constants
from common.utils import generate_json


class server_parent():
    def __init__(self, server_name):
        # dict for storing user info
        self.user_dict = {}
        # dict for room list
        self.room_dict: {str: room_parent} = {}
        # server's name
        self.name = server_name
        # game's match dict
        self.match_dict = {}

    def get_room_by_number(self, user_id):
        """
        get room number by id
        :param user_id: client's id
        :return:
        """
        for room_id, room in self.room_dict.items():
            if room.is_in_room(user_id):
                return room_id
        return None

    def check_name_exist(self, name):
        """
        check if name is exist
        :param name: name
        :return: true or false
        """
        for user_id, user in self.user_dict.items():
            if user.name == name:
                return True
        return False

    def input_user(self, user: user_parent):
        """
        input clinet into user_dict
        :param client:
        :return:
        """
        id = generate_constants.generate_id()
        self.user_dict[id] = user
        return id

    def close_client(self, id):
        """
        close and delete client
        :param id: the id of user_dict
        :return:
        """
        self.user_dict[id][USER_DICT_TYPE] = USER_DICT_OFFLINE
        # self.user_dict[id][USER_DICT_CLIENT].close()

    def delete_client(self, number):
        """
        delete client
        :param number:the number of user_dict
        :return:
        """
        del self.user_dict[number]

    def send_to_one(self, user_id, msg):
        """
        need to override,every way to communicate with others is different
        :param user_id: user's id
        :param msg: message
        :return:
        """

    def send_to_room(self, room_id, data, info=None):
        """
        send data to room by room_number
        """
        self.room_dict[room_id].filter(data)

    def send_to_room_client(self, room_number, msg):
        """
        message's way :
        room -> server -> client
        send message to all client in one room
        :param room_number: the room's number
        :param msg: the message to user
        :return:
        """
        for i in self.room_dict[room_number].user_list:
            self.send_to_one(i, msg)

    def show_data(self):
        """
        show user_dict and room_dict
        :return:
        """
        print(f"user_dict info")
        for k, v in self.user_dict.items():
            print(f"k:{k},v:{v}")
        print()
        print(f"room_dict info")
        for k, v in self.room_dict.items():
            print(f"k:{k},v:{v}")

    def login(self, data: dict, *args, **kwargs):
        """
        need child to override,every way to communicate has a different way to login
        """

    def insert_room(self, user_list: list, game_id: str) -> room_parent:
        """
        generate room and load user_list
        """
        room_id = generate_constants.generate_id()
        room = game_dict[game_id][GAME_ROOM]
        room = room(room_id, game_id, user_list, game_dict[game_id][GAME_ROOM], game_dict[game_id][GAME_BODY_INFO],
                    self)
        self.room_dict[room_id] = room
        return room

    def logout(self, id, *args, **kwargs):
        """
        client logout,but not leave room
        :param id: client's id
        :param name: client's name
        :return:
        """
        # not in room del its data
        if not self.get_room_by_number(id):
            del self.user_dict[id]
        # in room means it leave by something wrong,so just turn it to offline
        else:
            self.user_dict[id][USER_DICT_TYPE] = USER_DICT_OFFLINE

    def send_data(self, id):
        """
        need override, which send all data to client.
        It can solve login again client
        :param id:
        :return:
        """

    def match(self, data, *args, **kwargs):
        """
        in the future server will send game and game info to client.
        :param data:{
            CODE: MATCH_WITHDRAW,
            LOGIN_ID: id,
            TIMESTAMP: int(time.time() / 1000)
        }
        """
        # add user to different match by game
        if data[GAME] not in self.match_dict:
            self.match_dict[data[GAME]] = []
        else:
            self.match_dict[data[GAME]].append(data[LOGIN_ID])

        # send MATCH_RESPONSE to client
        self.send_to_one(data[LOGIN_ID], generate_json.generate_match_response(data[LOGIN_ID]))

        if len(self.match_dict[data[GAME]]) == game_dict[data[GAME]][MATCH_SIZE]:
            # match success and get them and recover match_dict
            user_id_list = copy.deepcopy(self.match_dict[data[GAME]])
            self.match_dict[data[GAME]] = []

            room = self.insert_room(user_id_list, data[GAME])
            room.room_start()

    def get_message(self, *args, **kwargs) -> dict:
        """
        get message in some way,child need implement it
        """

    def filter(self, data: dict, *args, **kwargs):
        """
        message from method:get_message transfer to filter.Server will do something with filter
        :param message: str and from method:get_message
        :param message:
        """
        print(data)
        if data[CODE] == LOGIN:
            self.login(data, args, kwargs)
        elif data[CODE] == SHOW_DATA:
            self.show_data()
        elif data[CODE] == LOGOUT:
            self.logout(data[LOGIN_ID], args, kwargs)
        elif data[CODE] == MATCH:
            self.match(data, args, kwargs)
        elif data[CODE] == ROOM_CODE:
            self.send_to_one_room(data[ROOM], info)
