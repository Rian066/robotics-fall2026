# Mission 3

## Data To Command

front_distance() finds the nearest valid LiDAR distance ahead, and decide_velocity() either moves forward or returns 0.0 to stop.

## Missing Data Safety

The robot stops because without a valid measurement, it cannot safely know whether the path is clear.

## System Layers

The functions choose the safe speed, the ROS node publishes it to /student_cmd_vel, and the command guard ensures the movement command stays safe.
