import time
import threading

class Scheduler:

    scheduler_start_time = time.time()
    q2_expired = True

    #Constructor
    def __init__(self,m_process_list: list):

        self.output_file = open("output_temp.txt", "w")
        self.s_process_list = m_process_list.copy()
        self.Q1 = []
        self.Q2 = []


    def add_to_expired(self,process):
        print("Adding to expired queue...")
        if Scheduler.q2_expired:
            self.Q2.append(process)

    # Used to initialize scheduler before shceduler begins (before t = 1 s)
    def initialize_scheduler(self):

        elapsed_time = time.time() - Scheduler.scheduler_start_time
        elapsed_time = elapsed_time * 1000

        if(elapsed_time < 1000):

                print("Initalizing shceduler")

                for process in self.s_process_list:
                    if process.arrival_time < 1000:
                        print(f"Proces {process.pid} is less than 1000 ms ")
                        self.add_to_expired(process)

                    else:
                        print(f"Proces {process.pid} is greater than 1000 ms ")

    def print_q2_info(self):

        print("\nThe process in the expired queue are: ")

        for process in self.Q2:

            print(process.pid)

    def bubble_sort(self,Q2):
            n = len(Q2)

            for i in range(n):

                already_sorted = True

                for j in range(n - i - 1):
                    if Q2[j].get_priority() > Q2[j + 1].get_priority():
                        # If the item you're looking at is greater than its
                        # adjacent value, then swap them
                        Q2[j], Q2[j + 1] = Q2[j + 1], Q2[j]

                        # Since you had to swap two elements,
                        # set the `already_sorted` flag to `False` so the
                        # algorithm doesn't finish prematurely
                        already_sorted = False

                # If there were no swaps during the last iteration,
                # the array is already sorted, and you can terminate
                if already_sorted:
                    break
