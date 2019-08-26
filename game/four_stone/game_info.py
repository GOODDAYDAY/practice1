class four_stone_info():

    def __init__(self):
        # name of game
        self.NAME = "four footman"
        # backgrand size
        self.X = 400
        self.Y = 400
        # backgrand large
        self.SIZE = 4
        # block size
        self.X1 = int(self.X / self.SIZE)
        self.Y1 = int(self.Y / self.SIZE)
        # turn for now
        self.TURN_NOW = 0
        # turn size
        self.TURN_SIZE = 2

        # picture constants
        self.water_footman_list = [[0, 0], [1, 0], [2, 0], [3, 0]]
        self.fire_footman_list = [[0, 3], [1, 3], [2, 3], [3, 3]]

        # army_list
        self.army_list = [self.fire_footman_list, self.water_footman_list]

        # attack_list
        self.attack_water_list = [[1, 0, 0, -1], [-1, 1, 0, 0], [0, 0, 1, -1], [-1, 0, 0, 1]]
        self.attack_fire_list = [[0, 1, 1, -1], [-1, 0, 1, 1], [1, 1, 0, -1], [-1, 1, 1, 0]]
        self.attack_list = [self.attack_water_list, self.attack_fire_list]

    def attack_charge(self, array):
        """
        charge if there has a attack
        :param array: the info of one line or one row
        :return: -1 or 2 or 3
        """
        if array[0] == self.TURN_NOW \
                and array[1] == self.TURN_NOW \
                and array[2] == (self.TURN_NOW + 1) % self.TURN_SIZE \
                and array[3] != (self.TURN_NOW + 1) % self.TURN_SIZE:
            return 2
        if array[0] != (self.TURN_NOW + 1) % self.TURN_SIZE \
                and array[1] == self.TURN_NOW \
                and array[2] == self.TURN_NOW \
                and array[3] == (self.TURN_NOW + 1) % self.TURN_SIZE:
            return 3
        return -1

    def attack(self, position_move):
        """

        :param position_move:
        :return:
        """
        array = []
        for i in range(self.SIZE):
            array.append(self.charge_which_army([position_move[0], i]))
        number = self.attack_charge(array)
        if number > 0:
            self.army_list[(self.TURN_NOW + 1) % self.TURN_SIZE].remove(
                [position_move[0], number])

        array = []
        for i in range(self.SIZE - 1, -1, -1):
            array.append(self.charge_which_army([position_move[0], i]))
        number = self.attack_charge(array)
        if number > 0:
            self.army_list[(self.TURN_NOW + 1) % self.TURN_SIZE].remove(
                [position_move[0], (number + 1) * -1 + self.SIZE])

        array = []
        for i in range(self.SIZE):
            array.append(self.charge_which_army([i, position_move[1]]))
        number = self.attack_charge(array)
        if number > 0:
            self.army_list[(self.TURN_NOW + 1) % self.TURN_SIZE].remove(
                [number, position_move[1]])

        array = []
        for i in range(self.SIZE - 1, -1, -1):
            array.append(self.charge_which_army([i, position_move[1]]))
        number = self.attack_charge(array)
        if number > 0:
            self.army_list[(self.TURN_NOW + 1) % self.TURN_SIZE].remove(
                [(number + 1) * -1 + self.SIZE, position_move[1]])

    def turn_next(self):
        self.TURN_NOW = (self.TURN_NOW + 1) % self.TURN_SIZE

    def charge_which_army(self, position):
        """
        charge which army's footman in this position
        :param position: (x,y)
        :return: 0 or 1 which is turn
        """
        for i in range(self.TURN_SIZE):
            if position in self.army_list[i]:
                return i
        return -1

    def move_footman(self, position_init, position_move):
        """
        check and change position_init to position_move
        :param position_init: the footman's position
        :param position_move: the footman want to go to position
        :return: True or False
        """
        # charge if the right turn
        if self.TURN_NOW != self.charge_which_army(position_init):
            return False
        # charge if the position move is empty
        if -1 != self.charge_which_army(position_move):
            return False
        # charge if the position is right
        if 1 != abs((position_init[0] + position_init[1]) - (position_move[0] + position_move[1])):
            return False

        # move footman
        self.army_list[self.TURN_NOW].remove(position_init)
        self.army_list[self.TURN_NOW].append(position_move)

        # attack
        self.attack(position_move)

        self.turn_next()

        return True

    def is_win(self):
        """
        charg if this turn is win
        :return:
        """
        if len(self.army_list[(self.TURN_NOW + 1) % self.TURN_SIZE]) == 1:
            return True
        return False

    def reset(self):
        """
        reset the footman's position
        """
        self.water_footman_list = [(0, 0), (1, 0), (2, 0), (3, 0)]
        self.fire_footman_list = [(0, 3), (1, 3), (2, 3), (3, 3)]

    # util to find which block mouse click
    def get_which_block(self, postion):
        return int(postion[0] * 4 / self.X), int(postion[1] * 4 / self.Y)
