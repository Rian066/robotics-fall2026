# Mission 2

## Snapshot

{'schema_version': 2, 'captured_at': '2026-09-25T19:14:10.320081+00:00', 'frames': ['odom', 'base_link', 'base_scan', 'rear_camera_link', 'hall_camera'], 'frame_chain': ['hall_camera', 'odom', 'base_link', 'base_scan', 'rear_camera_link'], 'transforms': {'base_scan_to_base_link': {'translation': {'x': -0.032, 'y': 0.0, 'z': 0.172}, 'yaw': 0.0}, 'rear_camera_to_base_link': {'translation': {'x': -0.18, 'y': 0.0, 'z': 0.22}, 'yaw': -3.1415926535795866}, 'hall_camera_to_base_link': {'translation': {'x': -9.599863844574766e-09, 'y': -2.0, 'z': 1.19}, 'yaw': 1.5707963268004606}}, 'point_prompts': {'hall_camera_point': 'Transform point (0.5, 0.0, 0.0) from hall_camera to base_link.'}, 'transformed_points': {'scan_point_in_base': {'x': 0.968, 'y': 0.0}, 'rear_camera_point_in_base': {'x': -1.18, 'y': -1.0206624774663903e-11}, 'hall_camera_point_in_base': {'x': -9.602645810813702e-09, 'y': -1.5}}, 'source': 'live'}

## Frame Context

The rear camera stays fixed because it is physically attached to the robot, so its position and rotation relative to base_link do not change. The hallway camera is fixed in the environment, not on the robot. As the robot moves, its position and orientation relative to the hallway camera change, so the transform to base_link changes.

## Initial Prompt

Write ROS 2 Python code that converts a point detected by the hallway camera into the robot's base_link frame.


## Initial Output

To convert a point from the hallway camera frame to the robot's `base_link` frame, use ROS 2 `tf2`. Create a `tf2_ros.Buffer` and `TransformListener`, then look up the transform between the two frames and transform the point.

```python
import rclpy
from rclpy.node import Node
import tf2_ros
from geometry_msgs.msg import PointStamped

class PointTransformer(Node):
    def __init__(self):
        super().__init__('point_transformer')

        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(
            self.tf_buffer, self
        )

    def transform_point(self, point):
        try:
            transform = self.tf_buffer.lookup_transform(
                'base_link',
                'hallway_camera',
                rclpy.time.Time()
            )

            transformed = tf2_ros.do_transform_point(
                point, transform
            )

            return transformed

        except Exception as e:
            self.get_logger().error(f'Transform failed: {e}')
            return None


def main():
    rclpy.init()
    node = PointTransformer()

    point = PointStamped()
    point.header.frame_id = 'hallway_camera'
    point.point.x = 1.0
    point.point.y = 0.0
    point.point.z = 0.0

    result = node.transform_point(point)

    if result:
        print(result)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
```

## Initial Source

import rclpy
from rclpy.node import Node
import tf2_ros
from geometry_msgs.msg import PointStamped
from tf2_geometry_msgs import do_transform_point

class PointTransformer(Node):
def **init**(self):
super().**init**('point_transformer')
self.tf_buffer = tf2_ros.Buffer()
self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)

def transform_point(self, point):
    try:
        transform = self.tf_buffer.lookup_transform(
            'base_link',
            'hallway_camera',
            rclpy.time.Time()
        )
        return do_transform_point(point, transform)
    except Exception as e:
        self.get_logger().error(f'Transform failed: {e}')
        return None

def main():
rclpy.init()
node = PointTransformer()

point = PointStamped()
point.header.frame_id = 'hallway_camera'
point.point.x = 1.0
point.point.y = 0.0
point.point.z = 0.0

result = node.transform_point(point)

if result:
    print(result)

node.destroy_node()
rclpy.shutdown()

if **name** == '**main**':
main()


## Initial Analysis

The AI assumed the camera and robot frame names. It did not properly explain timestamps or what to do if the TF transform was unavailable. It also did not need to use any robot motion topics.


## Improved Changes

The improved prompt clearly specifies hall_camera as the source and base_link as the target. It uses the point's timestamp and the TF buffer instead of hard-coded offsets. If the transform is unavailable, it returns None without moving the robot.


## Live Pending

True

## Synthesis

The first AI response made assumptions about the frames and timestamps. The improved prompt makes these details clear. A wrong transform could make the robot think a person is in the wrong location. The rotated-coordinate test checks this. If TF is unavailable, the robot should not move.


## Live Issue

The live camera verification could not complete. Also, my laptop overheating and laggy and can't continue this.
