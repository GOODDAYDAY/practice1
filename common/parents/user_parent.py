class user_parent():
    def __init__(self, user_id: str, name: str):
        # user's id
        self.user_id = user_id
        # user's type
        self.type = False
        # user's name
        self.name = name

    def get_name(self):
        """
        return self name
        """
        return self.name

    def get_type(self):
        """
        return self type
        """
        return self.type

    def get_user_id(self):
        """
        return self user_id
        """
        return self.user_id

    def switch_type(self):
        self.type = not self.type
        return self.type

    def switch_type_login(self):
        self.type = True

    def swich_type_logout(self):
        self.type = False
