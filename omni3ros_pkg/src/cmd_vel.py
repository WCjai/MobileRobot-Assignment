#!/usr/bin/env python
import rospy
import roslib
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist 
import numpy as np
import math

#############################################################
#############################################################
class TwistToMotors():
#############################################################
#############################################################

    #############################################################
    def __init__(self):
    #############################################################
        rospy.init_node("twist_to_motors")
        nodename = rospy.get_name()
        rospy.loginfo("%s started" % nodename)
    
        self.w = rospy.get_param("~base_width", 0.2)
    
        self.pub_lmotor = rospy.Publisher('/open_base/left_joint_velocity_controller/command', Float64, queue_size=10)
        self.pub_rmotor = rospy.Publisher('/open_base/right_joint_velocity_controller/command', Float64, queue_size=10)
        self.pub_bmotor = rospy.Publisher('/open_base/back_joint_velocity_controller/command', Float64, queue_size=10)
        rospy.Subscriber('cmd_vel', Twist, self.twistCallback)
    
    
        self.rate = rospy.get_param("~rate", 50)
        self.timeout_ticks = rospy.get_param("~timeout_ticks", 2)
        self.left = 0
        self.right = 0
        
    #############################################################
    def spin(self):
    #############################################################
    
        r = rospy.Rate(self.rate)
        idle = rospy.Rate(10)
        then = rospy.Time.now()
        self.ticks_since_target = self.timeout_ticks
    
        ###### main loop  ######
        while not rospy.is_shutdown():
        
            while not rospy.is_shutdown() and self.ticks_since_target < self.timeout_ticks:
                self.spinOnce()
                r.sleep()
            idle.sleep()
                
    #############################################################
    def spinOnce(self):
    #############################################################
        r = 0.025 
        d = 0.05 
        meh=math.pi/3
        A= np.array([[-d/r, 1/r, 0], [-d/r, -1/(2*r), (-math.sin(meh))/r], [-d/r, -1/(2*r), (math.sin(meh))/r]])
        B= np.array([self.dr,self.dx, self.dy])
        X= A @ B
        self.pub_lmotor.publish(X[0])
        self.pub_rmotor.publish(X[1])
        self.pub_bmotor.publish(X[2])
        self.ticks_since_target += 1

    #############################################################
    def twistCallback(self,msg):
    #############################################################
        # rospy.loginfo("-D- twistCallback: %s" % str(msg))
        self.ticks_since_target = 0
        self.dx = msg.linear.y
        self.dr = msg.angular.z
        self.dy = msg.linear.x
    
#############################################################
#############################################################
if __name__ == '__main__':
    """ main """
    try:
        twistToMotors = TwistToMotors()
        twistToMotors.spin()
    except rospy.ROSInterruptException:
        pass
