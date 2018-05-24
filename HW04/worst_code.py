# Beschreibung des Moduls `ListIsSorted`. Dieses
# Modul schaut, ob eine Liste absteigend
# sortiert angezeigt wird


def ListIsSorted(list: list) -> bool:
    '''
    This function looks if a list is sorted by going
    through every item in the list given by any user
    and then looks if at least the second item was
    reached if the item before is a greater number than
    the actual one.

    list: Liste von Nummern
    return: RÃ¼ckgabewert
    '''
    if len(list) == 0 or len(list) == 1:
        print("Keine Aussage mÃ¶glich")

    if len(list) == 0:  # list has length 0!
        # return simply the list
        return list
    elif len(list) == 1:
        # TODO: maybe a good idea without elif?
        a = []
        for b in list:
            b = int(b)
            if isinstance(b, int):
                a.append(b)
            else:
                # do nothing
                x = 0
        return a
    else:
        sorted = True
        while sorted:
            y = -10e100000
            for x in list:
                if x > y:
                    sorted = True
                    y = x
                    continue
                else:
                    sorted = False
                    y = x
                    break
            break
        return bool(sorted)
    return sorted




def proof(cmpr):
    resultingcmpr = "overwrite this"
    for round in cmpr:
        while round is not cmpr[-1]:
            if round == cmpr[0]:
                continue
            else:
                if round < cmpr[round - 1]:
                    resultingcmpr = True
    return resultingcmpr


if __name__ == "worst_code":
    print("ListIsSorted started")
elif __name__ == "__main__":
    print("ListIsSorted imported")

