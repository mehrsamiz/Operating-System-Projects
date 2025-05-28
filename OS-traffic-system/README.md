# Traffic Intersection Simulator – OS Assignment

This Python project simulates a four-way intersection using **multithreading**, designed for the **Operating Systems course**. It handles vehicle movements from all directions using **weighted round-robin scheduling** and ensures safe concurrent execution without collisions or deadlocks.

---

## 🚦 Project Structure

- `traffic_system.py` – Core traffic simulation logic.
- `example_scenario.py` – A test scenario with 10 vehicles.
- `README.md` – Documentation for the project.

---

## 🧠 Key Concepts

- Python threads and mutex locks (`threading`)
- Barrier synchronization
- Weighted round-robin scheduling
- Deadlock and collision avoidance
- Fair access across multiple directions

---

## ▶️ How to Run

1. Make sure you have Python 3 installed.
2. Clone this repo or download the files.
3. Run the scenario:

```bash
python example_scenario.py
