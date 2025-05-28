class Process:
    def __init__(self, arrival_time, execution_time, priority, starting_deadline, ending_deadline):
        self.arrival_time = arrival_time
        self.execution_time = execution_time
        self.priority = priority
        self.starting_deadline = starting_deadline
        self.ending_deadline = ending_deadline
        self.waiting_time = 0
        if self.starting_deadline + self.execution_time >= self.ending_deadline:
            self.scheduling_time = min(self.ending_deadline - self.execution_time, self.starting_deadline)
        else:
            self.scheduling_time = self.ending_deadline - self.execution_time
        self.missed = False
    
    def __repr__(self):
        return f"Process(arrival={self.arrival_time}, exec={self.execution_time}, prio={self.priority}, start={self.starting_deadline}, end={self.ending_deadline})"