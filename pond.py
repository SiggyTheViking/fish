#!/usr/bin/python3

import math

def make_a_pond(max_x,max_y,z_func):
    pond = []
    for x in range(max_x):
        y_array = []
        for y in range(max_y):
            y_array.append(z_func(x,y))
        pond.append(y_array)

    return pond

def set_depth(x,y):
    #for a 1024 x 
    return 42

def get_distance(x1,y1,x2,y2):
    return int(
        math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2)))


def main():
    pass

if __name__ == "__main__":
    main() 
