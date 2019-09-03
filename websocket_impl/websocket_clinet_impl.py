import _thread as thread
import json

import websocket

from common.parents.client_parent import client_parent
from common.utils import generate_json
from websocket_impl.websocket_user_impl import websocket_user_impl
from websocket_impl.websocket_windows import generate_windows


class websocket_client_impl(client_parent):
    def __init__(self):
        # get windows
        self.windows = generate_windows()
        # get base info
        id, name, ws_url = self.windows.login_windows()
        thread.start_new_thread(self.choose_game, ())
        # create user
        user = websocket_user_impl(id, name)
        super().__int__(user)

        # create websocket client
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
        self.ws.send(generate_json.generate_login(self.user.get_name(), self.user.get_user_id()))
        print("login send")

    def get_message(self, message):
        """
        get message in some way,child need implement it.
        Then send message to filter
        """
        # ws = args[0]
        # message = args[1]
        self.filter(json.loads(message))

    def send_to_server(self, message: str):
        """
        send message in some way,child need implement it.
        :param message: str
        """
        self.ws.send(message)

    def choose_game(self):
        """
        the function to choose which game to play
        """
        game_id = self.windows.match_window()
        self.match(game_id)
