# Mission 3

## Specification

The robot will move through four forward arcs, turning +45°, -45°, +45°, and -45°, each with a radius of 0.30 m. I will use a safe forward speed and keep the turning speed within the limits. The robot will stop after each arc and send a final stop command at the end. The motion is successful if all four arcs are close to a 0.30 m radius and 45° turn, and the robot finishes facing its original direction.

## Saved Specification

The robot will move through four forward arcs, turning +45°, -45°, +45°, and -45°, each with a radius of 0.30 m. I will use a safe forward speed and keep the turning speed within the limits. The robot will stop after each arc and send a final stop command at the end. The motion is successful if all four arcs are close to a 0.30 m radius and 45° turn, and the robot finishes facing its original direction.

## Assigned Pattern

alternating_arcs

## Original Prompt

Create the alternating_arcs pattern with four forward arcs: +45°, -45°, +45°, -45°. Each arc should have a 0.30 m radius. Use safe speeds within the course limits and finish facing the starting direction. Only implement build_pattern using the existing Segment class. Raise ValueError for an unknown pattern.

## Original Output

I will use a forward speed of 0.15 m/s. For an arc radius of 0.30 m, angular speed is calculated using ω = v/R. This gives ω = 0.15/0.30 = 0.50 rad/s.

A 45° turn is π/4 radians, so the duration of each arc is (π/4)/0.50, which is about 1.571 seconds. Positive angular velocity turns left and negative angular velocity turns right.

The pattern therefore uses four segments with angular velocities +0.50, -0.50, +0.50, and -0.50 rad/s. All segments use a forward speed of 0.15 m/s and a duration of about 1.571 seconds. These values are within the course speed and time limits. The positive and negative turns cancel, so the robot should finish facing its initial direction.

The wrapper is responsible for repeatedly publishing each segment and sending the final zero-velocity command, so build_pattern only needs to return the segment list.

I would test that there are four segments, all linear speeds are 0.15 m/s, the angular speeds alternate between +0.50 and -0.50 rad/s, each duration is about 1.571 seconds, each radius is 0.30 m, and an unknown pattern name raises ValueError.

## Original Source

import math

def build_pattern(pattern_name: str) -> list[Segment]:
    if pattern_name != "alternating_arcs":
        raise ValueError("Unknown pattern name")

    speed = 0.15
    radius = 0.30
    angular_speed = speed / radius
    duration = (math.pi / 4) / angular_speed

    return [
        Segment(speed, angular_speed, duration),
        Segment(speed, -angular_speed, duration),
        Segment(speed, angular_speed, duration),
        Segment(speed, -angular_speed, duration),
    ]

## Assumptions

The AI assumed the robot uses meters, seconds, and radians. It assumed positive turning is left and negative turning is right. It also assumed the robot follows the commanded speed for the full duration.

## Problems

I did not find major errors. I checked the speeds, 45° turns, 0.30 m radius, timing, and segment order to make sure they matched the requirements.

## Test Plan

Pattern test: Check that the robot makes four arcs in the order left, right, left, right.

Velocity test: Check that all speeds stay within 0.22 m/s and 0.80 rad/s.

Stop test: Check that the robot sends a final zero command and stops after the last arc.

## Modifications

I replaced the unfinished code with four arc segments. I used 0.15 m/s forward speed and ±0.50 rad/s turning speed to make a 0.30 m radius. Each arc lasts about 1.57 seconds for a 45° turn. I also added `ValueError` for an unknown pattern name. The pattern and speed tests will check these changes.

## Live Pending

True

## Evidence Analysis

The tests show that my pattern uses valid speeds, positive durations, and the correct type of motion. The 7 course tests passed. These tests do not prove the robot will move perfectly in the real world. An additional live robot test would help confirm the actual path.

## Ai Disclosure

I used ChatGPT to help create the ROS 2 code and tests. I personally reviewed the speeds, turn directions, durations, and code errors. I also ran the tests and fixed the problems I found.

## Live Issue

My PC is heating up and laggy. I can't do this now.
