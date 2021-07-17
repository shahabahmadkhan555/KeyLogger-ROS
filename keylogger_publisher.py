#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from pynput.keyboard import Listener

pub = rospy.Publisher('keylogger_topic', String, queue_size=10)
rospy.init_node('key_publisher_node', anonymous=True)   #initialising publisher node

#function called each time a key is presssed
def writetofile(key):
    keydata = str(key)
    #function responsible for publishing the pressed key
    pub.publish("pressed key is {}".format(keydata))

#initialising Listener object   
with Listener(on_press = writetofile) as l:
    l.join()
