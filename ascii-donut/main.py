# https://github.com/RandomThings23/donut

from math import sin, cos

def clear_screen():
    import os
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    a = 0
    b = 0

    height = 24
    width  = 80
   
    clear_screen()

    while True:
        z = [0 for _ in range(4 * height * width)]
        screen = [" " for _ in range(height * width)]

        j = 0
        while j < 6.28:
            j += 0.07
            i = 0
            while i < 6.28:
                i += 0.02

                sin_a = sin(a)
                sin_b = sin(b)
                cos_a = cos(a)
                cos_b = cos(b)

                sin_i = sin(i)
                sin_j = sin(j)
                cos_i = cos(i)
                cos_j = cos(j)

                mess = 1 / (sin_i * (cos_j + 2) * sin_a + sin_j * cos_a + 5)
                t = sin_i * (cos_j + 2) * cos_a - sin_j * sin_a

                # 40 is the left screen shift
                x = int(40 + 30 * mess * (cos_i * (cos_j + 2) * cos_b - t * sin_b))
                # 12 is the down screen shift
                y = int(11 + 15 * mess * (cos_i * (cos_j + 2) * sin_b + t * cos_b))
                # all are casted to int, ie floored
                o = int(x + width * y)
				# multiplying by 8 to bring in range 0-11 as 8*(sqrt(2))=11
				# because we have 11 luminance characters
                n = int(8 * ((sin_j * sin_a - sin_i * cos_j * cos_a) * cos_b - sin_i * cos_j * sin_a - sin_j * cos_a - cos_i * cos_j * sin_b))
				# if x,y inside screen and previous z-buffer is < mess 
				# i.e. when z[o] is 0 or the prev point is behind the new point
				# so we change it to the point nearer to the eye/ above prev point 
                if 0 < y < height and 0 < x < width and z[o] < mess:
                    z[o] = mess
                    screen[o] = ".,-~:;=!*#$@"[n if n > 0 else 0]

        # clear screen and print donut
        clear_screen()
        for index, char in enumerate(screen):
            if index % width == 0:
                print()
            else:
                print(char, end='')

        # increments
        a += 0.04
        b += 0.02

if __name__ == "__main__":
    main()