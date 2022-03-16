import time
import threading

class Scheduler:

    # Initial flag for Q2 (which means Q1 is active) at first
    # Class variable known to all instances of schduler

    #Constructor
    def __init__(self,m_process_list: list):

        self.output_file = open("output_temp.txt", "w")
        self.s_process_list = m_process_list.copy()

        self.scheduler_start_time = time.time()
        self.total_elapsed_time = 0

        self.Q2_expired = True
        self.Q1 = []
        self.Q2 = []


    def add_to_expired(self,process):
        print("Adding to expired queue...")
        if self.Q2_expired:
            self.Q2.append(process)

        else:
            self.Q1.append(process)

    # Used to initialize scheduler before scheduler begins (before t = 1000 ms)
    def s_initialize(self):

        elapsed_time = self.update_time()

        while(elapsed_time < 1000):

                print("Initializing shceduler for t < 1000 ms")

                for process in self.s_process_list:
                    if process.arrival_time < 1000:

                        # Append to expired queue and then pop from the list of processes
                        self.add_to_expired(process)
                        self.s_process_list.pop(0)

                        # Update elapsed time
                        elapsed_time = self.update_time()

                    else:
                        # Processes w/ arrival times greater than 1000 ms will wait
                        elapsed_time = self.update_time()

        while(elapsed_time >= 1000 and elapsed_time < 5000):

            #print("Run shceduler for t >= 1000 ms")

            while len(self.Q1) == 0 and len(self.Q2) != 0:

                #Execute processes in Q2
                #
                #
                # C O D E   H E R E
                #
                #

                #pop() used to simulate that a process has finished executing its time slice in Q2
                print(f"Poped {self.Q2[0].pid}")
                self.Q2.pop(0)


            elapsed_time = self.update_time()

    # Updates the time, call this each time you would like to update the time.
    def update_time(self):

        return (time.time() - self.scheduler_start_time) * 1000

    # Used for debugging not necessary for the assignment
    def print_q2_info(self):


        # When Q2 is empty
        if len(self.Q2) == 0:
            print("Proccesses in Q2 have been popped")
        else:

        # When Q2 is not empty
            print("\nThe process in the expired queue are: ")

            for process in self.Q2:

                print(process.pid)

    # Not complete yet
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
