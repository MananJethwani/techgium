#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Int16MultiArray
import time
imu_raw=Float32MultiArray()
imu_raw.data=[0,0,0,0,0,0]
jerk=Int16MultiArray() #[jerk x,y,z, jerk_flags x,y,z]
jerk.data=[0,0,0,0,0,0]
def imu_cb(msg):
    global imu_raw
    imu_raw=msg #[acc x,y,z,vel x,y,z]

prev_acc_x=0.0
curr_acc_x=0.0
curr_time=0
prev_time=0

jerk_x=0.0
jerk_y=0.0
jerk_z=0.0

x_threshold=0.0
y_threshold=0.0
z_threshold=0.0

def imu_control():
    global curr_time
    global curr_acc_x
    global prev_time
    global prev_acc_x
    global jerk_x
    global jerk_y
    global jerk_y
    global x_threshold
    global y_threshold
    global z_threshold
    global jerk
    time_step=10
    rospy.Subscriber("/raw/imu",Float32MultiArray,imu_cb)
    # rate=rospy.Rate(10)
    jerk_pub=rospy.Publisher("/jerk_data",Int16MultiArray,queue_size=10)
    while not rospy.is_shutdown():
        curr_time=time.time()
        prev_acc_x=imu_raw.data[0]
        if(curr_time-prev_time>=time_step):
            curr_acc_x=imu_raw.data[0]
            jerk_x=abs((curr_acc_x-prev_acc_x)/time_step)
            if(jerk_x>=x_threshold):
                jerk.data[0]=jerk_x
                jerk.data[3]=1
            else:
                jerk.data[3]=0
            if(jerk_y>=y_threshold):
                jerk.data[1]=jerk_y
                jerk.data[4]=1
            else:
                jerk.data[4]=0

            if(jerk_z>=z_threshold):
                jerk.data[2]=jerk_z
                jerk.data[5]=0
            else:
                jerk.data[5]=0

        jerk_pub.publish(jerk)
        # rate.sleep()

if __name__=="__main__":
    rospy.init_node("jerk_detection_node")
    imu_control()
    
    