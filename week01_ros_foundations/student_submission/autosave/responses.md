# Week 1: Discovering a Robot Through ROS 2

## Student

- Name: Rian M Alif
- Email: rian.alif58@login.cuny.edu

## final.architecture_evidence

My node is reactive because it responds directly to current LiDAR readings. A hybrid system would also need planning and higher-level decisions.

## final.course_reflection

This activity showed me how programming can control a robot. I liked seeing how simple Python code could make a robot move or stop.

It also helped me understand that robotics is not only about writing code. Sensors, communication, timing, and safety are also important. Even a small error can cause the robot to behave incorrectly.

The safety part stood out to me the most. A robot should stop when it does not have enough information instead of taking a risk. This activity made me more interested in learning about robotics and how software can control real machines.

## final.hardware_next

Before using it on a real robot, I would test different obstacles, distances, bad sensor data, delays, and emergency stops.

## final.middleware_debugging

I can use the ROS graph to check the nodes, topics, publishers, and subscribers and find where the command is not getting through.

## final.system_synthesis

Robotics software can be difficult because many different parts have to work together. A robot uses sensors, software, communication, and motors at the same time. If one part gives bad information or stops working, the robot may make a wrong or unsafe move.

In this activity, I built a reactive system. This means the robot reacts to what its sensor sees right now. The front_distance() function looks at the LiDAR readings and finds the closest valid object in front of the robot. Then decide_velocity() decides if the robot should move or stop. If the path is clear, the robot moves slowly. If an object is too close, it stops. This system is simple and fast, but it cannot plan ahead or remember what happened before.

ROS 2 helped connect the different parts of the system. The LiDAR sensor sends distance readings through /scan. The obstacle_guard node receives those readings. My functions use the readings to decide the robot's speed. The node then sends the movement command through /student_cmd_vel. A command guard can also check the command before the robot moves. This gives us several connections between the sensor, ROS node, decision code, command guard, and robot.

Sensor problems and timing are also important for safety. If the robot gets no valid LiDAR reading, my code tells it to stop instead of assuming the path is clear. The tests also showed that invalid or old sensor data caused the speed to become 0.0. This is safer because the robot should not keep moving when it does not know what is in front of it.

Overall, this activity showed me that even a simple robot needs many different parts working together correctly. The sensor needs to collect good information, the program needs to understand that information, and ROS 2 needs to send the data to the correct places. The robot also needs safety systems in case something goes wrong. The command guard is an important safety layer because it can limit unsafe movement commands before they reach the robot. This showed me that robotics is not only about making a robot move, but also about making sure it moves safely and correctly.

## final.timing_evidence

The invalid sensor test stood out most. It showed me that the robot should stop when it cannot trust its sensor data.

## mission_1.command_path_explanation

A proposed command travels on /student_cmd_vel. The guard checks it. Then the approved command travels on /cmd_vel.

## mission_1.graph_explanation

A ROS 2 graph shows how nodes and topics communicate. For example, the /scan topic sends data from Gazebo.

## mission_1.guided_checks

{'bridge_info': True, 'command_topics': True, 'guard_info': True, 'node_list': True, 'scan_info': True, 'scan_message': True}

## mission_1.scan_observation

I found the range_max field = 3.5, which probably represents the distance it has scanned.

## mission_1.tools_explanation

Gazebo is responsible for simulating the robot, while RViz is responsible for displaying the data.

## mission_2.measurement_explanation

The estimated traveled path measures the total distance along the curve. The start-to-end distance measures the straight-line distance between the starting and ending points.

## mission_2.modified_settings

{'linear_x': 0.12, 'angular_z': 0.6, 'duration': 4.0}

## mission_2.motion_comparison

My prediction was close to the actual result. The table showed a forward speed of 0.15 m/s and a command time of 3.0 s, matching the predicted straight movement. The evidence source was the motion result table

## mission_2.prediction_locks

{'curve': '2026-09-12T03:33:26.904851+00:00', 'curve_modified': '2026-09-12T03:33:54.654784+00:00', 'rotation': '2026-09-12T03:32:32.249067+00:00', 'straight': '2026-09-12T03:30:52.495910+00:00'}

## mission_2.predictions

{'curve': 'I predict a right-hand curved path because the robot moves forward while turning right.', 'curve_modified': 'This curve should be tighter because the turning speed is higher, giving it a smaller turning radius.', 'rotation': 'I predict its position will stay the same while its direction will turn left about 1.5 radians.', 'straight': 'I predict the robot will travel 0.45 meters.'}

## mission_2.safety_explanation

The command guard checks each driving command for unsafe values. The final zero command stops the robot at the end of a trial. The timeout is needed if the program or communication stops while the robot is moving.

## mission_3.data_to_command

front_distance() finds the nearest valid LiDAR distance ahead, and decide_velocity() either moves forward or returns 0.0 to stop.

## mission_3.missing_data_safety

The robot stops because without a valid measurement, it cannot safely know whether the path is clear.

## mission_3.system_layers

The functions choose the safe speed, the ROS node publishes it to /student_cmd_vel, and the command guard ensures the movement command stays safe.

## part_1.activity

{'sensor': {'normal': True, 'changed': True}, 'timing': {'normal': True, 'changed': True}, 'hardware': {'normal': True, 'changed': True}}

## part_2.activity

{'reactive': {'normal': True, 'changed': True}, 'behavior': {'normal': True, 'changed': True}, 'deliberative': {'normal': True, 'changed': True}, 'hybrid': {'normal': True, 'changed': True}, 'safety': {'normal': True, 'changed': True}}

## part_3.activity

{'middleware': {'single': True, 'multiple': True}, 'communication': {'topic': True, 'service': True}, 'failure': {'healthy': True, 'sensor': True, 'type': True, 'visualization': True}, 'inspection': {'nodes': True, 'node_info': True, 'topics': True, 'topic_info': True, 'echo': True, 'services': True, 'broken': True}}
