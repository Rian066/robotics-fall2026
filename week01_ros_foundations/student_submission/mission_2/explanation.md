# Mission 2

## Predictions

{'straight': 'I predict the robot will travel 0.45 meters.', 'rotation': 'I predict its position will stay the same while its direction will turn left about 1.5 radians.', 'curve': 'I predict a right-hand curved path because the robot moves forward while turning right.', 'curve_modified': 'This curve should be tighter because the turning speed is higher, giving it a smaller turning radius.'}

## Prediction Locks

{'straight': '2026-09-12T03:30:52.495910+00:00', 'rotation': '2026-09-12T03:32:32.249067+00:00', 'curve': '2026-09-12T03:33:26.904851+00:00', 'curve_modified': '2026-09-12T03:33:54.654784+00:00'}

## Motion Comparison

My prediction was close to the actual result. The table showed a forward speed of 0.15 m/s and a command time of 3.0 s, matching the predicted straight movement. The evidence source was the motion result table

## Measurement Explanation

The estimated traveled path measures the total distance along the curve. The start-to-end distance measures the straight-line distance between the starting and ending points.

## Safety Explanation

The command guard checks each driving command for unsafe values. The final zero command stops the robot at the end of a trial. The timeout is needed if the program or communication stops while the robot is moving.

## Modified Settings

{'linear_x': 0.12, 'angular_z': 0.6, 'duration': 4.0}
