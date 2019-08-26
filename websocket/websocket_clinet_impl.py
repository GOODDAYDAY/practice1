from common.parents.client_parent import client_parent
from common.utils import generate_json
import json
import threading
import websocket



class websocket_client_impl(client_parent):
    def __init__(self, name, id, ws_url):
        # thread.start_new_thread(self.send_data, ())
        super().__int__(name, id, ws_url)

        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(
            f"ws://{ws_url}",
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open)
        self.ws.run_forever()

    def on_error(self, error):
        print(error)

    def on_close(self):
        print("### closed ###")

    def on_open(self):
        """
        when open run login
        :param ws:
        :return:
        """
        self.ws.send(generate_json.generate_login(self.name, self.id))
        print("login send")


    def send_data(self):
        while 1:
            name = input("input please:")
            if name == "1":
                self.ws.send(generate_json.generate_show_data())
            elif name == "2":
                self.ws.send(generate_json.generate_logout(self.id, self.name))
            elif name == "3":
                self.ws.send(generate_json.generate_match(self.id))

    def get_number_by_client(self, client):
        """
        find client's id from user_dict by client
        :param client:
        :return:
        """
        for id, ele in self.user_dict.items():
            if ele[USER_DICT_CLIENT] == client:
                return id
        return -1
