#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64, String, Int32, Int32MultiArray, MultiArrayLayout, MultiArrayDimension

def handle(data):
    # print(data)
    pass


if __name__ == '__main__':
    rospy.init_node("sub_node")
    # rospy.loginfo("Hello from python node")
    # rospy.logwarn("This is a warning!!!!")
    # rospy.logerr("This is an error!!")


    # rospy.sleep(1.0)
    # rospy.loginfo("End of program")

    # rate = rospy.Rate(1000)
    
    rospy.Subscriber("/data", String, handle)
    while not rospy.is_shutdown():
        pass
        # rospy.loginfo("in the loop")
        # pub_test.publish("dataaaa")
        # rate.sleep()
    else:
        rospy.loginfo("END")
    rospy.spin()