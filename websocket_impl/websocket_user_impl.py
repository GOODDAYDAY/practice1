from common.parents.user_parent import user_parent


class websocket_user_impl(user_parent):
    def __init__(self, user_id: str, name: str):
        # impl parent
        super().__init__(user_id, name)
        # add websocket client
        self.client = None

    def set_client(self, client):
        self.client = client

    def get_client(self):
        return self.client
