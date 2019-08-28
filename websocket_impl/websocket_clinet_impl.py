import _thread as thread

import websocket

from common.parents.client_parent import client_parent
from common.utils import generate_json


class websocket_client_impl(client_parent):
    def __init__(self, name, id, ws_url):
        thread.start_new_thread(self.send_data, ())
        super().__int__(name, id)

        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(
            f"ws://{ws_url}",
            on_message=self.get_message,
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

    def get_message(self, *args, **kwargs):
        """
        get message in some way,child need implement it.
        Then send message to filter
        """
        ws = args[0]
        message = args[1]
        self.filter(message)

    def send_to_server(self, message: str):
        """
        send message in some way,child need implement it.
        :param message: str
        """
        self.ws.send(message)

    def send_data(self):
        while 1:
            name = input("input please:")
            if name == "1":
                self.ws.send(generate_json.generate_show_data())
            elif name == "2":
                self.ws.send(generate_json.generate_logout(self.id, self.name))
            elif name == "3":
                self.ws.send(generate_json.generate_match(self.id, "game1"))
