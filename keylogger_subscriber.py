#!/usr/bin/env python
import rospy
from std_msgs.msg import String
#function for printing the message on terminal
def callback(data):
    rospy.loginfo("%s", data.data)
    
def listener():
    rospy.init_node('key_subscriber_node', anonymous=True)    #initialising subscriber node
    rospy.Subscriber("keylogger_topic", String, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
   
if __name__ == '__main__':
    listener()
