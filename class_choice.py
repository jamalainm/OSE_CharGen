# from pc_classes import pc_classes
# from stat_gen import stat_block

def select_available_classes(pc_classes, stats):
    available_classes = []
    for pc_class in pc_classes:
        if pc_class['req'] == False:
            available_classes.append(pc_class)
        else:
            available = True
            requirements = pc_class['req'].keys()
            for req in requirements:
                if stats[req] < pc_class['req'][req]:
                    available = False
            if available == True:
                available_classes.append(pc_class)

    return available_classes

if __name__ == "__main__":
    stats = stat_block()
    available_classes = list_available_classes(pc_classes,stats)
    print(stats)
    for pc_class in available_classes:
        print(pc_class['name'])
