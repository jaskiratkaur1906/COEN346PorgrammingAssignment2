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

