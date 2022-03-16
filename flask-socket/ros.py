# from ros_workspace.src.scripts.test import control
import rospy
from sensor_msgs.msg import LaserScan
data_segment=[-1,-1,-1,-1,-1,-1,-1,-1]
segments=[0,0,0,0,0,0,-1,0]
laser_data = LaserScan()

# def laser_cb(msg):
#     global data_segment
#     itr_var=int((len(msg.ranges))/8)
#     data_segment[0]=min(min(msg.ranges[1076:1147]),min(msg.ranges[0:71]))
#     prev=71
#     for i in range(1,8):
#         temp=itr_var*(i)
#         data_segment[i]=min(msg.ranges[prev+2:temp])
#         prev=temp

# rospy.Subscriber("/scan",LaserScan,laser_cb)

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
<<<<<<< HEAD
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
=======
    global laser_data
    global data_segment
    global segments
    # if not rospy.is_shutdown():
    #     for i in range(8):
    #         if(data_segment[i]<0.2 and data_segment[i]>-1):
    #             segments[i]=1
    #         else:
    #             segments[i]=0
    return segments
    # frame = {
    #     "a1": 1,   #0-2 0-->green 1--> yellow 2-->red
    #     "b1": 1,
    #     "c1": 1,
    #     "d1": 1,
    #     "e1": 1,
    #     "f1": 1,
    #     "g1": 1,
    #     "h1": 1,
    #     "a2": 1,
    #     "b2": 1,
    #     "c2": 1,
    #     "d2": 1,
    #     "e2": 1,
    #     "f2": 1,
    #     "g2": 1,
    #     "h2": 1,
    #     "building_height": 20.5, # 0-100 in meter
    #     "active_height": 10.3,   #1-100 in meter
    #     "speed":10,              #0-50 in cm/sec
    #     "distance":20,           #0-40 in meter
    #     "iteration":100,         #0-100
    #     "longitude": 743,        
    #     "latitude": 475,
    #     "acceleration": 1.5,     #0-50
    #     "jerk": 7
    # }
    # return control()
    # randFrame = {
    #     "a1": random.randint(0, 2),   #0-2 0-->green 1--> yellow 2-->red
    #     "b1": random.randint(0, 2),
    #     "c1": random.randint(0, 2),
    #     "d1": random.randint(0, 2),
    #     "e1": random.randint(0, 2),
    #     "f1": random.randint(0, 2),
    #     "g1": random.randint(0, 2),
    #     "h1": random.randint(0, 2),
    #     "quad": random.randint(0, 7),  # quadrant from 0 to 7
    #     "building_height": random.uniform(0, 100), # 0-100 in meter
    #     "active_height": random.uniform(1, 100),   #1-100 in meter
    #     "speed":random.uniform(0, 50),              #0-50 in cm/sec
    #     "distance":random.uniform(0, 40),           #0-40 in meter
    #     "iteration":random.randint(0, 100),         #0-100
    #     "longitude": random.randint(0, 800),        
    #     "latitude": random.randint(0, 800),
    #     "acceleration": random.uniform(0, 50),     #0-50
    #     "jerk": random.randint(0, 20)
    # }
    # return {"data": randFrame}
>>>>>>> test
