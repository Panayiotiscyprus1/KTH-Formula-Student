#!/usr/bin/env python
import rospy
from std_msgs.msg import Int64, Float32

def callback(data):
    q=0.15
    rospy.loginfo(str(data.data/q))
    pub = rospy.Publisher('/kthfs/result', Float32, queue_size=10)
    rospy.init_node('nodeB', anonymous=False)
    pub.publish(data.data/q)
    
def listener():
    rospy.init_node('nodeB', anonymous=False)
    rospy.Subscriber("charalambous", Int64, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()