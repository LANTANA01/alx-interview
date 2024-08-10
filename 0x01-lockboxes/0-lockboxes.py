#!/usr/bin/python3
""" A method that determines if all the boxes can be opened. """

def canUnlockAll(boxes):
    """
    implementing lockboxes opening method.
    i have n number of locked boxes in front of me.
    Each box is numbered sequentially from 0 to n - 1 and
    each box may contain keys to the other boxes.
    """
    total_boxes = len(boxes)
    setofkeys = [0]
    counter = 0
    index = 0

    while index < len(setofkeys):
        setkey = setofkeys[index]
        for key in boxes[setkey]:
            if 0 < key < total_boxes and key not in setofkeys:
                setofkeys.append(key)
                counter += 1
        index += 1

    return counter == total_boxes - 1
