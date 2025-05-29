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
        self.gen_prior = 0
    
    def record_stats(self):
        prev = None
        while self.process_finished <= 100:
            if self.process_finished % 20 == 0 and self.process_finished != 0 and prev != self.process_finished:
                avg_waiting_time = sum(p.waiting_time for p in self.completed_processes) / len(self.completed_processes) if self.completed_processes else 0
                avg_score_hit = 1 - (self.miss_score/self.gen_prior) if self.gen_prior else 0
                hit_rate = self.process_finished / (self.process_finished + self.missed_process) if (self.process_finished + self.missed_process) else 0
                
                self.stats_over_time.append((
                    self.process_finished,
                    hit_rate,
                    self.total_score,
                    avg_waiting_time,
                    self.missed_process,
                    avg_score_hit,
                    self.miss_score
                ))
                prev = self.process_finished
                
                print("\n--- STATISTICS ---")
                print(f"Number of missed processes: {self.missed_process}")
                print(f"Number of finished processes: {self.process_finished}")
                print(f"Total score so far: {self.total_score}")
                print(f"Average waiting time: {avg_waiting_time:.2f} seconds\n")
            time.sleep(1)
    
    def plot_statistics(self):
        if not self.stats_over_time:
            return
            
        processes, hit_rates, scores, avg_waits, missed_counts, av_hit, miscore = zip(*self.stats_over_time)
        
        plt.figure(figsize=(12, 6))
        plots = [
            ("Hit Rate", hit_rates),
            ("Total Score", scores),
            ("Avg Waiting Time", avg_waits),
            ("Missed Processes", missed_counts),
            ("Score Hit Rate", av_hit),
            ("Miss Score", miscore)
        ]
        
        for i, (title, data) in enumerate(plots, 1):
            plt.subplot(3, 2, i)
            plt.plot(processes, data, marker='o')
            plt.title(title)
            plt.xlabel("Processes Finished")
            plt.ylabel(title)
        
        plt.tight_layout()
        plt.show()
