#!/usr/bin/python3

""" Lockboxes """


def canUnlockAll(boxes):
    """
    - boxes is a list of lists
    - A key with the same number as a box opens that box
    - You can assume all keys will be positive integers
    - The first box boxes[0] is unlocked
    - Return True if all boxes can be opened, else return False
    """
    newlist = []
    k = len(boxes)
    for i in boxes:
        if len(i) == 0 and i is not boxes[k-1]:
            return False
        for j in i:
            newlist.append(j)
    print(newlist)
    for index, keys in enumerate(boxes):
        if index in newlist or index < k-1:
            return True
        else:
            return False