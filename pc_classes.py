cleric = {
        'name' : 'cleric',
        'req' : False,
        'prime' : ['WIS'],
        'HD' : 6,
        'armor' : ['any'],
        'weapons' : ['blunt'],
        'lang' : ['alignment','common'],
        'saves' : {'D' : 11, 'W' : 12, 'P' : 14, 'B' : 16, 'S' : 15},
        'xp' : 1500,
        'skills' : [
            'Turn Undead (2d6): 1=7, 2=9, 2*=11'
            'Must carry holy symbol',
            'Deity disfavor',
            'Magical research',
            ],
        }

dwarf = {
        'name' : 'dwarf',
        'req' : {'CON' : 9},
        'prime' : ['STR'],
        'HD' : 8,
        'armor' : ['any'],
        'weapons' : ['small','normal'],
        'lang' : [
            'alignment','common','dwarvish','gnomish','goblin','kobold'
            ],
        'saves' : {'D' : 8, 'W' : 9, 'P' : 10, 'B' : 13, 'S' : 12},
        'xp' : 2200,
        'skills' : [
            '33% detect room traps'
            '33% detect construction tricks',
            '60ft infravision',
            '33% listen at doors',
            ],
        }

elf = {
        'name' : 'elf',
        'req' : {'INT' : 9},
        'prime' : ['STR','INT'],
        'HD' : 6,
        'armor' : ['any'],
        'weapons' : ['any'],
        'lang' : [
            'alignment','common','elvish','gnoll','hobgoblin','orcish'
            ],
        'saves' : {'D' : 12, 'W' : 13, 'P' : 13, 'B' : 15, 'S' : 15},
        'xp' : 4000,
        'skills' : [
            'Spell casting',
            'Magical Research',
            'Use magical item',
            '33% detect secret doors'
            'Immune to ghoul paralysis',
            '60ft infravision',
            '33% listen at doors',
            ],
        }

fighter = {
        'name' : 'fighter',
        'req' : False,
        'prime' : ['STR'],
        'HD' : 8,
        'armor' : ['any'],
        'weapons' : ['any'],
        'lang' : ['alignment','common'],
        'saves' : {'D' : 12, 'W' : 13, 'P' : 14, 'B' : 15, 'S' : 16},
        'xp' : 2000,
        'skills' : False,
        }

halfling = {
        'name' : 'halfling',
        'req' : {'CON' : 9, 'DEX' : 9},
        'prime' : ['DEX','STR'],
        'HD' : 6,
        'armor' : ['any appropriate to size'],
        'weapons' : ['any appropriate to size'],
        'lang' : ['alignment','common','halfling'],
        'saves' : {'D' : 8, 'W' : 9, 'P' : 10, 'B' : 13, 'S' : 12},
        'xp' : 2000,
        'skills' : [
            '+2 AC vs Large',
            'HS 90% in woods', 
            'HS 33% in dungeons'
            '+1 initiative*',
            '33% listen at doors',
            '+1 missile',
            ],
        }

mage = {
        'name' : 'mage',
        'req' : False,
        'prime' : ['INT'],
        'HD' : 4,
        'armor' : [],
        'weapons' : ['dagger'],
        'lang' : ['alignment','common'],
        'saves' : {'D' : 13, 'W' : 14, 'P' : 13, 'B' : 16, 'S' : 15},
        'xp' : 2500,
        'skills' : ['Magical Research','Spell casting', 'Use Magic Item'],
        }

thief = {
        'name' : 'thief',
        'req' : False,
        'prime' : ['DEX'],
        'HD' : 4,
        'armor' : ['leather','no shields'],
        'weapons' : ['any'],
        'lang' : ['alignment','common'],
        'saves' : {'D' : 13, 'W' : 14, 'P' : 13, 'B' : 16, 'S' : 15},
        'xp' : 1200,
        'skills' : {"CS":87, "TR":10, "HN":[1-2], 
            "HS":10, "MS":20, "OL":15, "PP":20},
        }

pc_classes = [cleric, dwarf, elf, fighter, halfling, mage, thief]
