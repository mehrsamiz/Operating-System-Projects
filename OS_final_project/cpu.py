import threading
import time
from .algorithms import select_process

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
                self.current_process = select_process(self.scheduler.ready_queue, self.cpu_id)
                if self.current_process:
                    self.execute_process()
            time.sleep(0.1)
    
    def execute_process(self):
        # Process execution logic
        pass