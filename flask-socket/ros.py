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

def data_emitter(dimensions):
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