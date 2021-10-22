#! /usr/bin/env python
import rospy
import tf
from nav_msgs.msg import Odometry
from std_msgs.msg import Header
from gazebo_msgs.srv import GetModelState, GetModelStateRequest

rospy.init_node('odom_pub')

odom_pub=rospy.Publisher ('/odom', Odometry, queue_size=50)
odom_broadcaster = tf.TransformBroadcaster()

rospy.wait_for_service ('/gazebo/get_model_state')
get_model_srv = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)

odom=Odometry()
header = Header()
header.frame_id='/odom'

model = GetModelStateRequest()
model.model_name='open_base'

r = rospy.Rate(20)
current_time = rospy.Time.now()
last_time = rospy.Time.now()

while not rospy.is_shutdown():
    current_time = rospy.Time.now()
    result = get_model_srv(model)
    odom_quat = [ 0.     ,    0.   ,     result.pose.orientation.z, result.pose.orientation.w]
    odom_broadcaster.sendTransform(
        (result.pose.position.x, result.pose.position.y, 0.),
        odom_quat,
        current_time,
        "origin_link",
        "odom"
    )
    odom.header.frame_id = "odom"

    odom.pose.pose = result.pose
    odom.twist.twist = result.twist
    odom.child_frame_id = "origin_link"
    header.stamp = rospy.Time.now()
    odom.header = header

    odom_pub.publish (odom)
    last_time = current_time

    r.sleep()
