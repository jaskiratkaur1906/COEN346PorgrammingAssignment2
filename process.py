 # This is a sample Python script.

class Process:

    # open input.txt and read file content
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    # get the Number of Processes of the program
    NumberOfProcesses = int(lines.pop(0))

    # list containing the process id for each process
    process_id = []
    # list containing the Arrival Time for each process
    arrivalTime = []
    # list containing the Burst time for each process
    burstTime = []
    # list containing the Priority for each process
    priority = []

    # store the user _name and number of processes as well as each process' ready time and service time in their respective variables
    for line in lines:
        process_id.append(str(line.split()[0]))
        arrivalTime.append(int(str(line.split()[1])))
        burstTime.append(int(str(line.split()[2])))
        priority.append(int(str(line.split()[3])))

    # close the file
    file.close()



    #Constructor
    def __init__(self,total_processes,pid,arrival_time,burst_time,priority):
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





