import threading
import time
from collections import deque

# Configuration: lane weights and directions
lane_weights = [2, 1, 3, 4]  # weights for north, south, east, west respectively
destination_paths = ["north", "south", "east", "west"]
current_lane = 0
time_slice = 2  # each unit of weight equals this many seconds

# Locks and synchronization primitives
lane_lock = threading.Lock()
start_barrier = threading.Barrier(2)  # to synchronize scheduler and vehicles
tes_l = threading.Lock()  # additional lock to protect path acquisition

# Maps paths to destination direction
lanes_s = {
    "north_to_south": "south", "west_to_south": "south", "east_to_south": "south",
    "east_to_north": "north", "south_to_north": "north", "west_to_north": "north",
    "south_to_east": "east", "west_to_east": "east", "north_to_east": "east",
    "north_to_west": "west", "south_to_west": "west", "east_to_west": "west",
}

# Each route has a unique mutex to prevent collisions
path_locks = {
    "north_to_south": threading.Lock(),
    "north_to_east": threading.Lock(),
    "north_to_west": threading.Lock(),
    "east_to_north": threading.Lock(),
    "east_to_south": threading.Lock(),
    "east_to_west": threading.Lock(),
    "south_to_east": threading.Lock(),
    "south_to_north": threading.Lock(),
    "south_to_west": threading.Lock(),
    "west_to_north": threading.Lock(),
    "west_to_east": threading.Lock(),
    "west_to_south": threading.Lock(),
}

# Maps direction and route to the specific path
route_to_path = {
    "north": {"straight": "north_to_south", "right": "north_to_west", "left": "north_to_east"},
    "east": {"straight": "east_to_west", "right": "east_to_north", "left": "east_to_south"},
    "south": {"straight": "south_to_north", "right": "south_to_east", "left": "south_to_west"},
    "west": {"straight": "west_to_east", "right": "west_to_south", "left": "west_to_north"},
}

# Each destination direction has a queue of waiting vehicles
destination_queue = {dest: deque() for dest in destination_paths}


def lane_scheduler():
    """Controls which direction’s queue can send vehicles using weighted round-robin."""
    global current_lane
    start_barrier.wait()  # Wait for all vehicles to be initialized
    while True:
        with lane_lock:
            active_destination = destination_paths[current_lane]
            weight = lane_weights[current_lane]

        start_time = time.time()
        # Allow vehicles from the current lane to proceed based on weight
        while time.time() - start_time < weight * time_slice:
            if not process_destination(active_destination):
                break

        with lane_lock:
            current_lane = (current_lane + 1) % len(destination_paths)


def process_destination(destination):
    """Processes the vehicles in the queue of the given destination."""
    if not destination_queue[destination]:
        return False

    while destination_queue[destination]:
        vehicle = destination_queue[destination][0]
        if not can_enter_intersection(vehicle):
            break
        destination_queue[destination].popleft()
        vehicle.cross_intersection()
    return True


def can_enter_intersection(vehicle):
    """Checks if the vehicle can safely enter its path in the intersection."""
    with lane_lock:
        if destination_paths[current_lane] != vehicle.destination:
            return False

    path = route_to_path[vehicle.lane][vehicle.route]
    return not path_locks[path].locked()


def enter_intersection(vehicle):
    """Acquires the necessary lock for the vehicle’s path before entering."""
    path = route_to_path[vehicle.lane][vehicle.route]
    tes_l.acquire()
    path_locks[path].acquire()


def exit_intersection(vehicle):
    """Releases the path lock after the vehicle exits the intersection."""
    path = route_to_path[vehicle.lane][vehicle.route]
    path_locks[path].release()
    tes_l.release()


class Vehicle(threading.Thread):
    """Represents a vehicle attempting to cross the intersection."""

    def __init__(self, vehicle_id, lane, route, crossing_time):
        threading.Thread.__init__(self)
        self.vehicle_id = vehicle_id
        self.lane = lane
        self.route = route
        self.crossing_time = crossing_time
        self.destination = self.get_destination()

    def get_destination(self):
        """Determines the destination direction from the lane and route."""
        return route_to_path[self.lane][self.route].split("_")[-1]

    def run(self):
        """Adds the vehicle to the appropriate destination queue."""
        destination_queue[self.destination].append(self)

    def cross_intersection(self):
        """Simulates crossing the intersection safely."""
        while True:
            if can_enter_intersection(self):
                enter_intersection(self)
                print(f"Vehicle {self.vehicle_id} from lane {self.lane} crossing to {self.destination}.")
                time.sleep(self.crossing_time)
                print(f"Vehicle {self.vehicle_id} has crossed to {self.destination}.")
                exit_intersection(self)
                break
            time.sleep(0.1)
