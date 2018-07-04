#!/usr/bin/python3

def diamond(height):
    """Return a string resembling a diamond of specified height (measured in lines).
    height must be an even integer.
    """
    if height%2 != 0:
        height += 1
    half = int(height / 2)
    mydiamond = ("")
    for w in range(0,half):
        for i in range(0,height):
            if i < (half - 1 - w):
                mydiamond += " "
            if i >= (half - 1 - w) and i < (half):
                mydiamond += "/"
            if i >= (half) and i <= (half + w):
                mydiamond += "\\"
        mydiamond += "\n"
    for w in range(0,half):
        for i in range(0,height):
            if i <= (w - 1):
                mydiamond += " "
            if i > (w - 1) and i <= (half - 1):
                mydiamond += "\\"
            if i > (half - 1) and i <= (height - w - 1):
                mydiamond += "/"
        mydiamond += "\n"
    return mydiamond
