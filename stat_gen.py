import random

def stat_block():
    stats = ['STR','INT','WIS','DEX','CON','CHA']
    block = {}
    for stat in stats:
        block[stat] = stat_gen()

    return block

def stat_gen():
    """ roll 3d6 """
    score = 0
    dice = 1
    while dice < 4:
        score += random.randint(1,6) 
        dice += 1

    return score

def can_adjust(block):
    """ Check whether scores can be adjusted """
    adjustable = []
    if block['STR'] >= 11:
        adjustable.append('STR')
    if block['INT'] >= 11:
        adjustable.append('INT')
    if block['WIS'] >= 11:
        adjustable.append('WIS')

    if len(adjustable) > 0:
        return adjustable
    else:
        return False

if __name__ == "__main__":
    print(stat_block())
