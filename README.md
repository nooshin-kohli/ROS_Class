# ROS_Class
Considering ROS Noetic is installed on your Ubuntu 20.04, we will guide you to configure your workspace. If you haven't installed ROS yet, you can use this link http://wiki.ros.org/noetic/Installation/Ubuntu to do so. 
## Creating catkin workspace
If you have sourced the setup.bash in your .bashrc you can pass the below command.
```
source /opt/ros/noetic/setup.bash
```
Create a folder with an arbitrary name. In my case, It's "catkin_ws".
```
mkdir catkin_ws
```
```
cd catkin_ws
mkdir src
catkin_make
```
After these commands, you should see the build devel and src folder in your catkin workspace.
## Use this Repo
Go to your catkin workspace
```
source devel/setup.bash
cd src
git clone https://github.com/nooshin-kohli/ROS_Class
cd ..
catkin_make
```
After cloning and making you can now use all files. Every time you want to use this repo you have to go to your workspace and 
```
source devel/setup.bash
```

