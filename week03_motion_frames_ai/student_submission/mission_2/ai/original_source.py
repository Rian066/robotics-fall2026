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
