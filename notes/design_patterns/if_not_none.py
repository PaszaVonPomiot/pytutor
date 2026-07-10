"""
External data often contains missing values (`None`). If passed directly into
your program, every function must check for `None`, making the code longer,
more complex, and more error-prone.
"""

from dataclasses import dataclass, field


@dataclass
class Drone0:
    id: str
    gps_location: str | None
    autopilot: bool | None
    waypoints: list[str] | None
    kilometers_flown: int | None


def add_waypoint(drone: Drone0, waypoint: str) -> None:
    if drone.gps_location is None:  # excessive None checks
        print("Drone is not at a known location.")
        return

    if drone.autopilot is None:  # excessive None checks
        print("Drone autopilot status is unknown.")
        return

    if drone.waypoints is not None:  # excessive None checks
        drone.waypoints.append(waypoint)
    else:
        drone.waypoints = [waypoint]


# Solution 1 - Use meaningful default values
# Use None only when “no value” has a distinct meaning
@dataclass
class Drone1:
    id: str
    gps_location: str | None
    autopilot: bool = False  # sensible default value
    waypoints: list[str] = field(default_factory=list[str])  # sensible default value
    kilometers_flown: int = 0  # sensible default value


# Solution 2
# TODO: https://www.youtube.com/watch?v=h8ZwhU3PpVw
