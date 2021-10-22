# MobileRobot-Assignment
Mobile Robotics (18MHE458T) Assignment by <b>JAYACHANDRAN(RA1911038010019)</b>

## System Requirement 
* Ubuntu 20.04
* ROS-Noetic
### [Note]: This repo uses https://github.com/YugAjmera/omni3ros_pkg repo's modifed simulation. For more Documentation check that repository 
<br /> <b>And give a vist to there paper as well: </b>
```
@inproceedings{mishra2019ego,
  title={Ego-Centric framework for a three-wheel omni-drive Telepresence robot},
  author={Mishra, Ruchik and Ajmera, Yug and Mishra, Nikhil and Javed, Arshad},
  booktitle={2019 IEEE International Conference on Advanced Robotics and its Social Impacts (ARSO)},
  pages={281--286},
  year={2019},
  organization={IEEE}
}
```

<br /> For <b>kinematic equation</b> refer this video:
<br /><b>https://www.youtube.com/watch?v=NcOT9hOsceE</b>

## Getstart with Workspace
Clone the repo in <b>`~/your_workspace_name/src`</b> by
- `git clone https://github.com/WCjai/MobileRobot-Assignment.git`
<br /> then use these cmd 
<br /> `sudo apt-get install ros-neotic-gazebo-config`
<br /> `sudo apt-get install ros-noetic-velocity-controllers`
<br />Then use <b>`catkin_make`</b> to complile


## Bringup simulation
* To bringup simulation use this cmd
<br />- `roslaunch omni3ros_pkg velocity_controller.launch`

<br /> In that it launches your simulation with kinematic code and transform between <b>Ground_plane(ie Global frame)</b> and <b>open_base (ie your_robot)</b>. You can find the code for kinematic and transform in <b>`~/your_workspace/src/omni3ros_pkg/src`</b> in which <b>cmd_vel.py</b> for kinematic and <b>odom_pub.py</b> for transform.
 
 ## Waypoint
 * To make the robot move autonomusly to point to point use this cmd:
 <br />`rosrun omni3ros_pkg waypoint1.py`
 * To enter coustom waypoint, go to  this directory <b>`~/your_workspace/src/omni3ros_pkg/src`</b> and open <b>waypoint1.py</b>, Then go to <b>line 30</b> and enter your x and y coordinates. You can add more than 5 waypoint simply by adding new set to the array  

