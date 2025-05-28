import threading
import time
import matplotlib.pyplot as plt

class Statistics:
    def __init__(self):
        self.lock = threading.Lock()
        self.process_finished = 0
        self.total_score = 0
        self.miss_score = 0
        self.missed_process = 0
        self.completed_processes = []
        self.missed_processes = []
        self.stats_over_time = []
    
    def record_stats(self):
        # Statistics recording logic
        pass
    
    def plot_statistics(self):
        # Plotting logic
        pass