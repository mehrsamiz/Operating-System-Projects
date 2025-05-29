import threading
import time
from algorithms import select_process

class CPU(threading.Thread):
    def __init__(self, cpu_id, scheduler, stats):
        super().__init__()
        self.cpu_id = cpu_id
        self.scheduler = scheduler
        self.stats = stats
        self.current_process = None
    
    def run(self):
        while True:
            if self.current_process is None:
                self.execute_process()
            time.sleep(0.1)
    
    def execute_process(self):
        with self.stats.lock:
            self.current_process = select_process(self.scheduler.ready_queue, self.cpu_id)
            if self.current_process:
                self.scheduler.ready_queue.queue.remove(self.current_process)
                self.current_process.waiting_time = time.time() - self.current_process.arrival_time
                c_time = time.time()
        
        print(f"CPU {self.cpu_id} is running {self.current_process}")
        
        while time.time() - c_time <= self.current_process.execution_time:
            if time.time() - starting_point > self.current_process.ending_deadline:
                with self.stats.lock:
                    self.stats.missed.append(self.current_process)
                    self.stats.miss_score += self.current_process.priority
                    self.stats.missed_process += 1
                    self.current_process.missed = True
                print(f"CPU {self.cpu_id} missed {self.current_process}")
                break
        
        if not self.current_process.missed:
            print(f"CPU {self.cpu_id} finished {self.current_process}")
            with self.stats.lock:
                self.stats.process_finished += 1
                self.stats.total_score += self.current_process.priority
        
        with self.stats.lock:
            self.stats.completed_processes.append(self.current_process)
        self.current_process = None
