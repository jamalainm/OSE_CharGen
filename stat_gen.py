import random

def roll_ability():
    """ 3d6 """
    stat = 0
    dice = 1
    while dice < 4:
        stat += random.randint(1,6)
        dice += 1

    return stat

if __name__ == "__main__":
    print(roll_ability())
