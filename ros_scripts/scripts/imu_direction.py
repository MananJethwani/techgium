#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Int16MultiArray
import math
imu_raw=Float32MultiArray()
imu_direction=Int16MultiArray()
imu_raw.data=[0,0,0,1,0,0]
imu_direction.data=[0,0,0,0,0,0,0,0]
angle=0

step_angle=45
def imu_cb(msg):
    global imu_raw
    imu_raw=msg

def imu_control():
    global angle 
    global imu_raw
    direction_pub=rospy.Publisher("/direction_data",Int16MultiArray,queue_size=10)
    # rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        angle = (math.atan(abs(imu_raw.data[4])/abs(imu_raw.data[3])))*(180/3.141) #angle in degrees
        if(imu_raw.data[3]>0 and imu_raw.data[4]>0):
            angle=angle
        elif(imu_raw.data[3]<0 and imu_raw.data[4]>0):
            angle=angle+90
        elif(imu_raw.data[3]<0 and imu_raw.data[4]<0):
            angle=angle+180
        elif(imu_raw.data[3]>0 and imu_raw.data[4]<0):
            angle=angle+270

        for i in range(8):
            prev_angle=step_angle*i
            curr_angle=step_angle*(i+1)
            if(angle>prev_angle and angle<curr_angle):
                imu_direction.data[i]=1
            else:
                imu_direction.data[i]=0
        direction_pub.publish(imu_direction)
        # rate.sleep()

if __name__=="__main__":
    rospy.Subscriber("/raw/imu",Float32MultiArray,imu_cb)
    rospy.init_node("imu_direction_node")
    imu_control()
    