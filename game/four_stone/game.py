# _*_ coding: utf-8 _*_

from pygame.locals import *

from common.parents.game_parent import game_parent
from game.four_stone import game_generate_json
from game.four_stone.map import *


class four_stone(game_parent):
    def __init__(self, user_id, turn, ws, id, room):
        super().__init__(ws, id, room)
        # load game_info
        self.four_stone_info = four_stone_info()
        # the position of click
        self.footman_init_position = None
        self.footman_move_position = None
        # self's turn
        self.turn = turn
        # self's userId
        self.user_id = user_id

    def run(self):
        """
        main method of this game
        :return:
        """
        # init pygame,ready for hardware
        pygame.init()
        # set window's tittle
        pygame.display.set_caption(self.four_stone_info.NAME)
        # draw the map
        draw_picture(self.four_stone_info.fire_footman_list, self.four_stone_info.water_footman_list)
        # main circle
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    # exit when receive the exit info
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # when mouse click down, record the position
                    x, y = self.four_stone_info.get_which_block(event.pos)
                    self.footman_init_position = (x, y)
                elif event.type == pygame.MOUSEBUTTONUP:
                    # when mouse click up,record the position and send them to server
                    x, y = self.four_stone_info.get_which_block(event.pos)
                    self.footman_move_position = (x, y)

                    # send message
                    self.send_to_client(game_generate_json.generate_move(
                        self.user_id, self.turn, self.footman_init_position,
                        self.footman_move_position, self.room_id))

                    # delete these two position
                    self.footman_move_position = None
                    self.footman_init_position = None
