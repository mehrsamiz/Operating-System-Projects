import random
import time
from .process import Process

starting_point = time.time()

def timing():
    return round(time.time() - starting_point, 1)

def generate_process(num_processes=10):
    processes = []
    for _ in range(num_processes):
        arrival_time = timing()
        execution_time = random.randint(1, 10)
        priority = random.randint(0, 100)
        starting_deadline = arrival_time + random.randint(0, 6)
        ending_deadline = starting_deadline + random.randint(0, 15)
        processes.append(Process(arrival_time, execution_time, priority, starting_deadline, ending_deadline))
        time.sleep(0.01)
    return processes