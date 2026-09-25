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