from game.four_stone.game_info import four_stone_info as game_info

import pygame

four_stone_info = game_info()


def draw_block(screen, images_real, x, y):
    """
    draw the block by x and y
    :param screen: screen
    :param images_real: black_broad or white_broad
    :param x: 0~3
    :param y: 0~3
    :return:
    """
    screen.blit(images_real, (four_stone_info.X1 * x, four_stone_info.Y1 * y))


def draw_board(screen, images_real, is_black):
    """
    :param screen: screen
    :param images_real: black_broad or white_broad
    :param num: 0~3
    :param is_black: the number of which is white or black
    """
    for i in range(four_stone_info.SIZE):
        for j in range(four_stone_info.SIZE):
            if (j + i) % 2 == is_black:
                draw_block(screen, images_real, i, j)


def draw_footman(screen, images_real, x, y):
    """
    draw the little footman which is fire or water
    :param screen: screen
    :param images_real: fire or water
    :param x: 0~3
    :param y: 0~3
    """
    screen.blit(images_real, (four_stone_info.X1 * x + int(four_stone_info.X1 / four_stone_info.SIZE / 2),
                              four_stone_info.Y1 * y + int(four_stone_info.Y1 / four_stone_info.SIZE / 2)))


def draw_footman_list(screen, images_real, footman_list):
    """
    draw footman by list which is fire_list or water_list
    :param screen: screen
    :param images_real: fire or water
    :param footman_list: fire_list or water_list
    """
    for footman in footman_list:
        draw_footman(screen, images_real, footman[0], footman[1])


def draw_picture(fire_list, water_list):
    # create a windows
    screen = pygame.display.set_mode((four_stone_info.X, four_stone_info.Y))

    # init the images
    black_images_real = generate_black_images()
    white_images_real = generate_white_images()
    fire_images_real = generate_fire_images()
    water_images_real = generate_water_images()

    # draw backgrand
    draw_board(screen, black_images_real, 1)
    draw_board(screen, white_images_real, 0)

    # draw footman
    draw_footman_list(screen, fire_images_real, fire_list)
    draw_footman_list(screen, water_images_real, water_list)

    pygame.display.update()
    return screen


def generate_black_images():
    white_image_filename = 'game/four_stone/picture/black_block.bmp'
    # 加载图片并转换
    white_images = pygame.image.load(white_image_filename)
    return pygame.transform.scale(white_images, (four_stone_info.X1, four_stone_info.Y1))


def generate_white_images():
    black_image_filename = 'game/four_stone/picture/white_block.bmp'
    # 加载图片并转换
    black_images = pygame.image.load(black_image_filename)
    return pygame.transform.scale(black_images, (four_stone_info.X1, four_stone_info.Y1))


def generate_fire_images():
    fire_image_filename = 'game/four_stone/picture/fire.png'
    # 加载图片并转换
    fire_images = pygame.image.load(fire_image_filename)
    return pygame.transform.scale(fire_images, (four_stone_info.X1 - int(four_stone_info.X1 / four_stone_info.SIZE),
                                                four_stone_info.Y1 - int(four_stone_info.Y1 / four_stone_info.SIZE)))


def generate_water_images():
    water_image_filename = 'game/four_stone/picture/water.png'
    # 加载图片并转换
    water_images = pygame.image.load(water_image_filename)
    return pygame.transform.scale(water_images, (four_stone_info.X1 - int(four_stone_info.X1 / four_stone_info.SIZE),
                                                 four_stone_info.Y1 - int(four_stone_info.Y1 / four_stone_info.SIZE)))
