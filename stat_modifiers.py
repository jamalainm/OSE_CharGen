modifiers = [-3, -2, -1, 0, 1, 2, 3]

def stat_tier(stat):
    """ Return bonuses for stats """
    tier = 0
    if stat <= 3:
        tier = 0
    elif stat <= 5:
        tier = 1
    elif stat <= 8:
        tier = 2
    elif stat <= 12:
        tier = 3
    elif stat <= 15:
        tier = 4
    elif stat <= 17:
        tier = 5
    elif stat <= 18:
        tier = 6

    return [stat, tier]

