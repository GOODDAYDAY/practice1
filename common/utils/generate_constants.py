import random


def generate_id():
    return "".join(random.sample('zyxwvutsrqponmlkjihgfedcba1234567890', 16))


def generate_dice(dice, num):
    return random.choices(range(1, dice + 1), k=num)


def generate_dice_result(dice, num, limit):
    num = 0
    for i in generate_dice(dice, num):
        if i >= limit:
            num += 1
    return num
