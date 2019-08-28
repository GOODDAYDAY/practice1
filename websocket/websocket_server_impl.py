from websocket_server import WebsocketServer

from common.constants.name_constants import *
from common.parents.server_parent import server_parent
from common.utils import generate_json


class websocket_server(server_parent):
    def __init__(self, port, name):
        # thread.start_new_thread(self.send_data_by_hand, ())
        super().__init__(name)

        self.server = WebsocketServer(port)
        self.server.set_fn_client_left(self.client_left)
        self.server.set_fn_message_received(self.get_message)
        self.server.run_forever()

    def send_data_by_hand(self):
        while 1:
            name = input("input please:")
            if name == "1":
                self.server.send_message_to_all("xixixixixi")

    def login(self, data, info=None):
        """
        when a client send login to server,check client and name
        :param client: client's client
        :param name: client's name which is name in game
        :param id: client's old id,if it has one.
        :return:
        """
        # load data from info
        client = info
        name = data[1]
        id = data[2] if len(info) == 3 else None

        # if id exist,it means client want to login again and get its data before.
        if id != None and id in self.user_dict and self.user_dict[id][USER_DICT_TYPE] == USER_DICT_OFFLINE:
            self.user_dict[id][USER_DICT_TYPE] = USER_DICT_ONLINE
            self.server.send_message(client, generate_json.generate_login_response(id, name))
            self.send_data(id)
        # if not exist,give it a new one
        elif not self.check_name_exist(name):
            new_id = self.input_client(client, name)
            self.server.send_message(client, generate_json.generate_login_response(new_id, name))
        # if exist and it is online response double login
        elif self.check_name_exist(name) and self.user_dict[id][USER_DICT_TYPE] == USER_DICT_ONLINE:
            self.server.send_message(client, generate_json.generate_double_login_response(id, name))
        # others do nothing
        else:
            print(f"name : {name} , id : {id} , login unknown error")

    def client_left(self, client, server):
        """
        when clinet left there are two situation
        1.left natural, server need delete its data
        2.left by unknown problem, server need keep its data
        :param client: the client which left
        :param server: self.server
        :return:
        """
        # close connection
        id = self.get_number_by_client(client)
        if id != -1:
            self.close_client(id)
            print(f"client:{id} close")

        # charge if it is left natural
        room_number = self.get_room_by_number(id)
        if room_number == -1 and id != -1:
            self.delete_client(id)
            print(f"client:{id} delete")

    def send_to_one(self, user_id, msg):
        """
        :param user_id: user's id
        :param msg: message
        :return:
        """
        self.server.send_message(self.user_dict[user_id][USER_DICT_CLIENT], msg)
