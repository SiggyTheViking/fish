#! /usr/bin/env python3

#tristan Trueblood - tristantrueblood@Gmail.com
#Fish depth map generator
#revision-002

#TODO:
##Change pond datastructure to numpy(?)
##Introduce variable interference on depth/slope(?) [introduce averaging?]

try:
    import random
    import math
except ImportError as e:
    raise Exception(e)

def generate_pond(wid, hei, minpd, maxpd,dpu=.25,peaks=50,seed=None):
    '''Takes width, height, minimum and max peak depth, slope of peaks, number of peaks, and seed.'''
    random.seed(seed)

    #Now that the pond exists, time to generate the peaks
    #   I'm taking the fancy approach; a gaussian generation of peak height
    #   so they come out averaging. A simple randomint between min/max suffices.
    peak = []
    if minpd > maxpd:   raise Exception('Minimum peak depth is larger than maximum; halting.')
    diff = maxpd - minpd
    for p in xrange(peaks):
        posx = int(random.gauss(.5,.22) * wid)  #tweak numbers until sufficient
        posy = int(random.gauss(.5,.15) * hei)  #x, being generally wider, has more variation
        depz = int(random.gauss(.5,.2) * diff + minpd + (random.gauss(.5,.4)*2))
        peak.append( ((posx,posy),depz) )  #format; tuple of pos,depth

    #Construct the data structure; [x][y] = depth !!! and calculate depth
    pond = []
    for x in xrange(wid):
        pondy = []
        for y in xrange(hei):
            max_d = 0
            sec_d = 0
            for p in peak:
            #Breakdown; determine distance between peak and current pixel
            #multiply distance by slope, to get drop over distance
            #get all heights, and the highest stays
                (px,py),pd = p
                dist = math.sqrt(math.pow(px-x, 2) + math.pow(py-y, 2))+(random.gauss(.5,.4)*2)
                d = int(pd-(dist*dpu))
                if d > max_d:
                    sec_d = max_d
                    max_d = d
                elif d > sec_d: sec_d = d
            pondy.append(int((max_d+sec_d)/2)) #set depth
        pond.append(pondy)
    return pond

def land_inate_ize(pond,maxh,dpu,seed=None):
    random.seed(seed)
    minh = maxh/16+1
    diff = maxh - minh

    sizex = len(pond)
    sizey = len(pond[0])
    for x in xrange(sizex):
        for y in xrange(sizey):
            #find shortest length
            if sizex - x < x:   shortx = sizex-x
            else:   shortx = x
            if sizey - y < y:   shorty = sizey-y
            else:   shorty = y
            if shorty < shortx: short = shorty
            else:   short = shortx
            del(shorty, shortx)

            #calculate dropoff
            h = int(maxh-(short*dpu)+(random.gauss(.5,.5)*1.773))
            if pond[x][y] - h < 0:  pond[x][y] = 0

    return pond
            

def debug_pygame(flag=False):
    widt = 1280#640#1280
    heit = 800#400#800
    mind = 25
    maxd = 50
    import pygame as pg
    #colour initialization
    ur = 5
    lr = 0
    ug = 155
    lg = 8
    ub = 199
    lb = 54
    incrementr = int((ur-lr)/maxd)
    incrementg = int((ug-lg)/maxd)
    incrementb = int((ub-lb)/maxd)
    screen = pg.display.set_mode((widt, heit))
    #generate pond
    pond = generate_pond(widt,heit,mind,maxd,seed='raging derp',peaks=75)
    print('pond initialized!')
    if flag:    pond = land_inate_ize(pond,maxd,.8,seed='raging derp')
    print('pond generated!')
    for x in xrange(len(pond)):
        for y in xrange(len(pond[x])):
            depth = abs(pond[x][y]-maxd)
            if depth == 50:  colour = (25,75,25)
            else:   colour = (depth*incrementr+lr,depth*incrementg+lg,depth*incrementb+lb)
            pond[x][y] = colour
    running = True
    print('beginning run!')
    while running:
        for x in xrange(len(pond)):
            for y in xrange(len(pond[x])):
                screen.set_at((x,y),pond[x][y])

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        pg.display.flip()
