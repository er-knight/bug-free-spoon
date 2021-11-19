# https://www.cs.princeton.edu/courses/archive/fall10/cos126/assignments/loops.html
# python 3.6.9

from typing import List

def rgb_to_cmyk(rgb: List[int]) -> List[float]:

    red, green, blue = rgb

    white   = max([red / 255, green / 255, blue / 255])

    cyan    = (white - red / 255) / white
    magenta = (white - green / 255) / white
    yellow  = (white - blue / 255) / white
    black   = (1 - white)

    return [cyan, magenta, yellow, black]

if __name__ == "__main__":

    rgb = (75, 0, 130) # indigo

    cyan, magenta, yellow, black = rgb_to_cmyk(rgb)

    print(f"cyan    = {cyan}")
    print(f"magenta = {magenta}")
    print(f"yellow  = {yellow}")
    print(f"black   = {black}")

    # cyan    = 0.423076923076923
    # magenta = 1.0
    # yellow  = 0.0
    # black   = 0.4901960784313726

# https://docs.python.org/3/library/colorsys.html
