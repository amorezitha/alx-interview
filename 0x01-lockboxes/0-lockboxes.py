#!/usr/bin/python3
"""Write a method that determines if all the boxes can be opened."""

def canUnlockAll(boxes):
    """ A  method that determines if all the boxes can be opened.
    Parameters:
    boxes (List[List[int]]): The list of lists representing the boxes
            and their keys.
    Returns:
    bool: True if all boxes can be unlock, else False"""
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
            if boxes_checked is False:
                return boxes_checked
            return True
