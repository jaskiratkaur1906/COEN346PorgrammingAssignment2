 # This is a sample Python script.

class Process:

    #Constructor
    def __init__(self,total_processes,pid,arrival_time,burst_time,priority):
        self.number_of_processes = total_processes
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.time_remaining = burst_time
        self.execution_time_completed = 0


 #Set functions


    def set_pid(self):
        self.pid = input("Enter process PID: ")

    def set_arrival_time(self):
            self.arrival_time = int(input("Enter process arrival time: "))

    def set_burst_time(self):
        self.burst_time = int(input("Enter process burst time: "))

    def set_priority(self):
            self.priority = int(input("Enter process priority: "))


 # Get functions
    def get_id(self):
        return self.pid

    def get_arrival_time(self):
        return self.arrival_time

    def get_burst_time(self):
        return self.burst_time

    def get_priority(self):
        return self.priority

    # Print function
    def print_info(self):
        print("process id is: " + self.get_id())
        print("process arrival time is: " + str(self.get_arrival_time()))
        print("process burst time is: " + str(self.get_burst_time()))
        print("process priority is: " +  str(self.get_priority()))
