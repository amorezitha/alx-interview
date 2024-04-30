#!/usr/bin/python3
"""Write a method that determines if all the boxes can be opened."""

def canUnlockAll(boxes):
    """ A  method that determines if all the boxes can be opened.
    Returns:
    bool: True if all boxes can be unlock, else False"""

    # Look to the unlocked boxes
    unlocked_box = [0]
    for i in unlocked_box:
        for j in boxes[i]:
            if j < len(boxes):
                if j not in unlocked_box:
                    unlocked_box.append(j)

    # Look the the length of the open box and all the boxes
    if len(boxes) == len(unlocked_box):
        return True
    else:
        return False
