# _*_ coding: utf-8 _*_

from common.parents.game_parent import game_parent
from common.utils import generate_json
from game.four_stone.map import *
from pygame.locals import *


class four_stone(game_parent):
    def __init__(self, turn, ws, id, room):
        super().__init__(ws, id, room)
        # load game_info
        self.four_stone_info = four_stone_info()
        # the position of click
        self.footman_init_position = None
        self.footman_move_position = None
        # self's turn
        self.turn = turn

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
                    self.send_to_server(generate_json.generate_move(self.id, self.turn, self.footman_init_position,
                                                                    self.footman_move_position, self.room))
                    # delete these two position
                    self.footman_move_position = None
                    self.footman_init_position = None



if __name__ == "__main__":
    # pass
    four_stone(0, 1, 1, 1).run()
