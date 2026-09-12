# Mission 1

## Command Path Explanation

A proposed command travels on /student_cmd_vel. The guard checks it. Then the approved command travels on /cmd_vel.

## Graph Explanation

A ROS 2 graph shows how nodes and topics communicate. For example, the /scan topic sends data from Gazebo.

## Guided Checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## Scan Observation

I found the range_max field = 3.5, which probably represents the distance it has scanned.

## Tools Explanation

Gazebo is responsible for simulating the robot, while RViz is responsible for displaying the data.
