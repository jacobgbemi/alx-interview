#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    """ FUnction to unlock boxes"""
    seen = set()
    seen.add(0)
    stack = [0]
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in seen:
                seen.add(key)
                stack.append(key)
    return len(seen) == len(boxes)
