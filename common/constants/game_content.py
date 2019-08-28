"""
1.constant is a dict of {id : method}
2.method will return a tuple of (TURN_SIZE,game,game_room)
3.server will choose the method and create the game and game_room
"""

MATCH_SIZE = 0
GAME_BODY = 1
GAME_ROOM = 2
GAME_BODY_INFO = 3


# four_stone
def get_four_stone():
    """
    load game info
    :return: (TURN_SIZE,game,game_room,game_info)
    """
    from game.four_stone.game import four_stone
    from game.four_stone.game_info import four_stone_info
    from game.four_stone.room import four_stone_room
    return (2, four_stone, four_stone_room, four_stone_info)


game_dict = {"game1": get_four_stone}
