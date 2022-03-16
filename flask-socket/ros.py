import random

speed=0
distance=0
itr=0
arrow=0
d_height=0
l_height=0
counter=1
jerk_var=0;
val=0
def data_emitter(dimensions):
    global speed
    global counter
    global d_height
    global l_height
    global itr
    global distance
    global arrow
    global val
    global jerk_var

    if(counter<=18):
        distance+=0.17222
    if(counter<=8):
        l_height+=0.375
    if(counter>22 and counter<=48):
        distance-=0.11923
    if(counter<14):
        speed+=2.85
        d_height+=0.3571
    if(counter==14):
        speed=0
    if(counter>14 and counter<18):
        speed+=7.5
        d_height-=0.25
    if(counter==18):
        speed=0
    if(counter>22 and counter<=30):
        speed+=3.5
        d_height+=0.35
    if(counter>=28 and counter<=48):
        d_height-=0.32

    if(counter>44 and counter<48):
        speed-=1.6
    if(counter==48):
        speed=0
    if(counter>14 and counter<18):
        jerk_var=1
    if(counter==18):
        jerk_var=0
    if(counter<18):
        arrow=7
    if(counter>32 and counter<=48):
        arrow=3
    if(counter>6 and counter<8):
        val=1
    if(counter>8 and counter<10):
        val=2
    if(counter==10):
        val=0
    counter+=1
    if(counter>=30):
        itr=1
        
    randFrame = {
        "a1": 0,   #0-2 0-->green 1--> yellow 2-->red
        "b1": 0,
        "c1": 0,
        "d1": 0,
        "e1": 0,
        "f1": val,
        "g1": val,
        "h1": 0,
        "quad": arrow,  # quadrant from 0 to 7
        "building_height": l_height, # 0-100 in meter
        "active_height": d_height,   #1-100 in meter
        "speed": speed,
        "speed_x":random.uniform(0, 50),              #0-50 in cm/sec
        "speed_y":random.uniform(0, 50),
        "speed_z":random.uniform(0, 50),
        "distance":distance,           #0-40 in meter
        "iteration":itr,         #0-100
        "longitude": random.randint(0, 800),        
        "latitude": random.randint(0, 800),
        "acceleration_x": random.uniform(0, 50),     #0-50
        "acceleration_y": random.uniform(0, 50),
        "acceleration_z": random.uniform(0, 50),
        "jerk_warning": 5,
        "collision_warning": 2,
        "nodes": 9,
        "jerk_x": random.randint(0, 20),
        "jerk_y": random.randint(0, 20),
        "jerk_z": random.randint(0, 20),
        "jerk": jerk_var
    }
    return {"data": randFrame};