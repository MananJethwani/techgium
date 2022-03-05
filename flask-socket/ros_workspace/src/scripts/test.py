#!/usr/bin/env python3
from glob import glob
from telnetlib import SGA
import rospy
from sensor_msgs.msg import LaserScan
data_segment=[-1,-1,-1,-1,-1,-1,-1,-1]
segments=[0,0,0,0,0,0,0,0]
laser_data=LaserScan()
def laser_cb(msg):
    global data_segment
    itr_var=int((len(msg.ranges))/8)
    data_segment[0]=min(min(msg.ranges[1076:1147]),min(msg.ranges[0:71]))
    prev=71
    for i in range(1,8):
        temp=itr_var*(i)
        data_segment[i]=min(msg.ranges[prev+2:temp])
        prev=temp

def control():
    global laser_data
    global data_segment
    global segments
    rospy.Subscriber("/scan",LaserScan,laser_cb)
    while not rospy.is_shutdown():
        for i in range(8):
            if(data_segment[i]<0.2 and data_segment[i]>-1):
                segments[i]=1
            else:
                segments[i]=0
        print(segments)
           
if __name__=="__main__":
    rospy.init_node("laser_scan_crane")
    control()