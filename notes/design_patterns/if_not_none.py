"""
External data often contains missing values (`None`). If passed directly into
your program, every function must check for `None`, making the code longer,
more complex, and more error-prone.
"""

from dataclasses import dataclass, field


@dataclass
class Drone:
    id: str
    gps_location: str | None
    autopilot: bool | None
    waypoints: list[str] | None
    kilometers_flown: int | None


def add_waypoint(drone: Drone, waypoint: str) -> None:
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
# Use None only when "no value" has a distinct meaning
# Otherwise see if True/False, empty list, or 0 is a better default value
@dataclass
class DroneWithDefaults:
    id: str
    gps_location: str | None
    autopilot: bool = False  # sensible default value
    waypoints: list[str] = field(default_factory=list[str])  # sensible default value
    kilometers_flown: int = 0  # sensible default value


# Solution 2 - Use early validation of input data
# This keeps invalid data out of the core of the application


@dataclass
class ReadyDrone:  # Drone but without optional fields
    id: str
    gps_location: str
    autopilot: bool
    waypoints: list[str]
    kilometers_flown: int


def validate_drone(drone: Drone) -> ReadyDrone:
    if drone.gps_location is None:
        raise ValueError("Drone is not at a known location.")

    if drone.autopilot is None:
        raise ValueError("Drone autopilot status is unknown.")

    if drone.waypoints is None:
        raise ValueError("Drone waypoints are unknown.")

    if drone.kilometers_flown is None:
        raise ValueError("Drone kilometers flown is unknown.")

    return ReadyDrone(
        id=drone.id,
        gps_location=drone.gps_location,
        autopilot=drone.autopilot,
        waypoints=drone.waypoints,
        kilometers_flown=drone.kilometers_flown,
    )


# Solution 3 - raise exception in core logic instead of returning None from functions (keep "happy path" code cleaner)
# This tells how the function should behave when it cannot complete its job
class Route:
    pass


class RouteRejected(Exception):
    pass


def assign_route(drone: Drone) -> Route:
    if drone.autopilot is None:
        raise RouteRejected("Drone autopilot status is unknown.")

    return Route()


# TODO: https://www.youtube.com/watch?v=h8ZwhU3PpVw
