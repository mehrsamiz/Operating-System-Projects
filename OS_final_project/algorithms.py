def select_process(queue, algorithm_num):
    if queue.empty():
        return None
    processes = list(queue.queue)
    
    if algorithm_num == 1:
        return min(processes, key=lambda p: p.scheduling_time + (p.priority/50))
    elif algorithm_num == 2:
        return max(processes, key=lambda p: -p.scheduling_time + p.priority)
    elif algorithm_num == 3:
        return min(processes, key=lambda p: p.execution_time/(p.execution_time+1) - p.scheduling_time)
    return None