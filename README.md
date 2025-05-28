# Operating Systems Course

This repository contains assignments and projects from the *Operating Systems* course completed at [SBU].

## Contents

###  OS-Exercise: Traffic Intersection Simulator
A multithreaded Python simulation of a four-way intersection that handles traffic scheduling, avoiding collisions and deadlocks using weighted round-robin scheduling.

- Language: Python
- Concurrency: Threads, Locks
- Features: Safe path management, fairness, deadlock avoidance
- [View Project](./OS-traffic-system)


## OS Final Project - Process Scheduling System


[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

A multi-processor scheduling system that dynamically generates processes and schedules them based on deadlines and priority scores, implementing three different scheduling algorithms.
- [View Project](./OS_final_project)

## Features
- Random process generation with:
  - Arrival time
  - Execution time (1-10 units)
  - Priority score (0-100)
  - Starting deadline (0-6 units after arrival)
  - Ending deadline (0-15 units after starting deadline)
- Input queue and ready queue management with size limitation (20 processes)
- Three CPU threads with different scheduling algorithms:
  1. Combined deadline and priority scheduling
  2. Priority-focused scheduling
  3. Execution-time-aware scheduling
- Statistics collection and visualization
- Thread-safe operations using mutex locks

## Requirements
- Python 3.8+
- Required packages:
  - `threading` (built-in)
  - `time` (built-in)
  - `random` (built-in)
  - `queue` (built-in)
  - `matplotlib` (for visualization)

## Installation
```bash
git clone https://github.com/mehrsamiz/Operating-System-Projects.git
cd Operating-System-Projects/OS-final-project
pip install matplotlib  # Only required if you want visualization
