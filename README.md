# MobileRobot-Assignment
Mobile Robotics (18MHE458T) Assignment by <b>JAYACHANDRAN(RA1911038010019)</b>
## System Requirement 
* Ubuntu 20.04
* ROS-Noetic

## Getstart with Workspace
Clone the repo in <b>`~/your_workspace_name/src`</b> by
- `git clone https://github.com/WCjai/MobileRobot-Assignment.git`

<br />Then use <b>`catkin_make`</b> to complile

## Bringup simulation
* To bringup simulation use this cmd
<br />- `roslaunch omni3ros_pkg velocity_controller.launch`

<br /> In that it launches your simulation with kinematic code and transform between <b>Ground_plane(ie Global frame)</b> and <b>open_base (your_robot)</b>. You can find the code for kinematic and transform in <b>`~/your_workspace/src/omni3ros_pkg/src`</b> in which <b>cmd_vel.py</b> for kinematic and <b>odom_pub.py</b> for transform.
 
 ## Waypoint
 * To make the robot move autonomusly to point to point use this cmd:
 <br />`rosrun omni3ros_pkg waypoint1.py`
 * To enter coustom waypoint, go to  this directory <b>`~/your_workspace/src/omni3ros_pkg/src`</b> and open <b>waypoint1.py</b>, Then go to <b>line 30</b> and enter your x and y coordinates. You can add more than 5 waypoint simply by adding new set to the array  

