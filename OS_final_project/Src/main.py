import threading
from .generator import generate_process, timing
from .scheduler import Scheduler
from .cpu import CPU
from .stats import Statistics

def main():
    stats = Statistics()
    scheduler = Scheduler()
    cpus = [CPU(i, scheduler, stats) for i in range(1, 4)]
    
    # Start all components
    scheduler.start()
    for cpu in cpus:
        cpu.start()
    
    # Start process generator
    generator_thread = threading.Thread(target=generate_and_add_processes, args=(scheduler,))
    generator_thread.start()
    
    # Start statistics recording
    stats_thread = threading.Thread(target=stats.record_stats)
    stats_thread.start()
    
    # Wait for completion
    generator_thread.join()
    stats_thread.join()
    scheduler.join()
    for cpu in cpus:
        cpu.join()
    
    stats.plot_statistics()

if __name__ == "__main__":
    main()