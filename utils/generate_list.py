import random

def generate_list():
    list = []
    length = random.randint(1, 5)

    for j in range(1, length + 1):
        item = random.randint(1, 100)
        list.append(item)

    return list

def generate_2d_list():
    external_length = random.randint(1, 5)
    external_list = []

    for i in range(1, external_length + 1):
        new_list = generate_list()
        external_list.append(new_list)

    return external_list
