<<<<<<< HEAD
#!/usr/bin/python
=======
#!/usr/bin/python3
>>>>>>> 0b6d2b446751da70a3cb70616295f0e8b8910c78

import math

def make_a_pond(max_x,max_y,z_func):
    pond = []
<<<<<<< HEAD
    #figure out our ellipse
    #first, our point b is 1/2 max_y, 0 x
=======
>>>>>>> 0b6d2b446751da70a3cb70616295f0e8b8910c78
    for x in range(max_x):
        y_array = []
        for y in range(max_y):
            y_array.append(z_func(x,y))
        pond.append(y_array)

    return pond

<<<<<<< HEAD
def set_depth_factory(width,height,depth):
    def anon(x,y):
        a,b,c = width/2.0,height/2.0,depth
        a_sq = math.pow(a,2)
        b_sq = math.pow(b,2)
        c_sq = math.pow(c,2)

        try:
            z = math.sqrt(c_sq - c_sq * math.pow(x - a,2)/a_sq - c_sq * math.pow(y - b,2) / b_sq)
        except:
            z = 0
        return int(z)

    return anon


def set_depth(x,y):
    #for a 1024 x 
    a,b,c = 1024/2.0,768/2.0,50
    a = math.pow(a,2)
    b = math.pow(b,2)
    c = math.pow(c,2)
    try:
        z = math.sqrt(c - c * math.pow(x - 512,2)/a - c * math.pow(y - 384,2) / b)
    except:
        z = 0

    return int(z)
=======
def set_depth(x,y):
    #for a 1024 x 
    return 42
>>>>>>> 0b6d2b446751da70a3cb70616295f0e8b8910c78

def get_distance(x1,y1,x2,y2):
    return int(
        math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2)))


def main():
    pass

if __name__ == "__main__":
<<<<<<< HEAD
    main()  
=======
    main() 
>>>>>>> 0b6d2b446751da70a3cb70616295f0e8b8910c78
