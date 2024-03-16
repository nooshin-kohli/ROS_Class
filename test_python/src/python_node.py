#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64, String, Int32, Int32MultiArray, MultiArrayLayout, MultiArrayDimension
pub_test = rospy.Publisher('/data', String, queue_size=10)


if __name__ == '__main__':
    rospy.init_node("test_node")
    rospy.loginfo("Hello from python node")
    rospy.logwarn("This is a warning!!!!")
    rospy.logerr("This is an error!!")


    rospy.sleep(1.0)
    rospy.loginfo("End of program")

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        #rospy.loginfo("in the loop")
        pub_test.publish("dataaaa")
        rate.sleep()
    else:
        rospy.loginfo("END")