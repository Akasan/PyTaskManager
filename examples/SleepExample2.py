from PyTaskManager import TaskManager
import time

with TaskManager("Job1") as tm1:
    for i in range(5):
        with TaskManager("Job2") as tm2:
            time.sleep(0.5)
            TaskManager.pause_track()
            print("Not tracked area")
            TaskManager.restart_track()

    time.sleep(1.0)

TaskManager.summary()