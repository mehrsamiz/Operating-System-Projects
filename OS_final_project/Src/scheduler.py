from queue import Queue
import threading
from .process import Process

class Scheduler(threading.Thread):
    def __init__(self, max_ready_queue_size=20):
        super().__init__()
        self.input_queue = Queue()
        self.ready_queue = Queue(maxsize=max_ready_queue_size)
        self.gen_prior = 0
    
    def add_to_input_queue(self, process):
        self.gen_prior += process.priority
        self.input_queue.put(process)
    
    def run(self):
        while True:
            if not self.input_queue.empty():
                process = self.input_queue.get()
                if not self.ready_queue.full():
                    self.ready_queue.put(process)
                else:
                    # Replacement logic
                    pass
            time.sleep(0.1)