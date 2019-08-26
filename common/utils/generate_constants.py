import random

def generate_id():
    return "".join(random.sample('zyxwvutsrqponmlkjihgfedcba1234567890', 16))

def generate_dice(num):
    return random.choices([1,2,3,4,5,6],k=num)