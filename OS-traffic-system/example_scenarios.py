from traffic_system import Vehicle, lane_scheduler, start_barrier
import threading

def scenario_based_traffic():
    scenario = [
        {"vehicle_id": 1, "lane": "north", "route": "straight", "crossing_time": 2},
        {"vehicle_id": 2, "lane": "east", "route": "right", "crossing_time": 1},
        {"vehicle_id": 3, "lane": "south", "route": "left", "crossing_time": 3},
        {"vehicle_id": 4, "lane": "west", "route": "straight", "crossing_time": 2},
        {"vehicle_id": 5, "lane": "north", "route": "right", "crossing_time": 1},
        {"vehicle_id": 6, "lane": "east", "route": "left", "crossing_time": 3},
        {"vehicle_id": 7, "lane": "south", "route": "right", "crossing_time": 1},
        {"vehicle_id": 8, "lane": "west", "route": "left", "crossing_time": 2},
        {"vehicle_id": 9, "lane": "north", "route": "left", "crossing_time": 3},
        {"vehicle_id": 10, "lane": "east", "route": "straight", "crossing_time": 2}
    ]
    threads = []
    for vehicle_info in scenario:
        vehicle = Vehicle(
            vehicle_id=vehicle_info["vehicle_id"],
            lane=vehicle_info["lane"],
            route=vehicle_info["route"],
            crossing_time=vehicle_info["crossing_time"],
        )
        threads.append(vehicle)
        vehicle.start()
    start_barrier.wait()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    scheduler_thread = threading.Thread(target=lane_scheduler)
    traffic_thread = threading.Thread(target=scenario_based_traffic)
    scheduler_thread.start()
    traffic_thread.start()
    traffic_thread.join()
    scheduler_thread.join()
