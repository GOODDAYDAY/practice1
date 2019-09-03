import json

from websocket_server import WebsocketServer

from common.constants.name_constants import *
from common.parents.server_parent import server_parent
from common.utils import generate_json
from websocket_impl.websocket_user_impl import websocket_user_impl


class websocket_server_impl(server_parent):
    def __init__(self, port, name):
        super().__init__(name)

        self.server = WebsocketServer(port)
        self.server.set_fn_client_left(self.client_left)
        self.server.set_fn_message_received(self.get_message)
        self.server.run_forever()

    def get_message(self, client, server, message):
        """
        get message in some way,child need implement it
        """
        # client = args[0]
        # server = args[1]
        # message = args[2]
        self.filter(json.loads(message), client)

    def login(self, data: dict, *args, **kwargs):
        """
        when a client send login to server,check client and name
        :param data : {
            CODE: LOGIN,
            LOGIN_ID: id,
            INFO :{
                LOGIN_NAME: name
            }
            TIMESTAMP: int(time.time() / 1000)
        }
        :return:
        """
        # load data from info
        client = args[0][0]
        id = data[LOGIN_ID]
        name = data[INFO][LOGIN_NAME]

        # if id exist,it means client want to login again and get its data before.
        # TODO password is nessary
        if id != None and id in self.user_dict:
            # switch to login
            self.user_dict[id].switch_type_login()
            # set client
            self.user_dict[id].set_client(client)
            # send response to client
            self.send_to_client(id, generate_json.generate_login_response(
                self.user_dict[id].get_user_id(),
                self.user_dict[id].get_name()))
        # if not exist,give it a new one
        else:
            # new websocket user
            user = websocket_user_impl(id, name)
            # set client
            user.set_client(client)
            # input to user
            id, name = self.input_user(user)
            # send to client
            self.send_to_client(id, generate_json.generate_login_response(id, name))

    def client_left(self, client, server):
        """
        when clinet left there are two situation
        1.left natural, server need delete its data
        2.left by unknown problem, server need keep its data
        :param client: the client which left
        :param server: self.server
        :return:
        """
        # TODO  rewrite
        # close connection
        # id = self.get_number_by_client(client)
        if id != -1:
            self.close_client(id)
            print(f"client:{id} close")

        # charge if it is left natural
        room_number = self.get_room_by_number(id)
        if room_number == -1 and id != -1:
            self.delete_client(id)
            print(f"client:{id} delete")

    def send_to_client(self, user_id: str, msg: str):
        """
        :param user_id: user's id
        :param msg: message
        :return:
        """
        self.server.send_message(self.user_dict[user_id].get_client(), msg)
