#!/usr/bin/env python
import rospy
import roslib
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist 
import numpy as np
import math

rospy.init_node("tt_to_motors")

# Create a publisher which can "talk" to Turtlesim and tell it to move
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
     
# Create a Twist message and add linear x and angular z values
move_cmd = Twist()
move_cmd.linear.x = 0.2
move_cmd.angular.z = 0.0
move_cmd1 = Twist()
move_cmd1.linear.x = 0.0
move_cmd1.angular.z = 0.0
pub.publish(move_cmd)

# Save current time and set publish rate at 10 Hz
rospy.sleep(1.)
pub.publish(move_cmd)
rospy.sleep(2.5)
pub.publish(move_cmd1)

