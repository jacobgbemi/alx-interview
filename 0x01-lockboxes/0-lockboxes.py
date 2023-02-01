#!/usr/bin/python3


def canUnlockAll(boxes):
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
