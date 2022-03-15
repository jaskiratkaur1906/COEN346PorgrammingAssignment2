from process import Process
from scheduler import Scheduler
import time
start_time = time.time()

with open('input.txt', 'r') as file:
    lines = file.readlines()

    # get the time quantum of the program
number_of_processes = int(lines.pop(0))

# dictionary containing the user names and number of processes under each user
process_id = []
# list containing the ready time for each process
arrival_time = []
# list containing the service time for each process
burst_time = []
# list containing the priority of each process
priority = []

for line in lines:

    process_id.append((line.split(" ")[0]))
    arrival_time.append(int(line.split(" ")[1]))
    burst_time.append(int(line.split(" ")[2]))
    priority.append(int(line.split(" ")[3]))

file.close()


process_list = []
for i in range(number_of_processes):
    p = Process(number_of_processes,process_id[i],arrival_time[i],burst_time[i],priority[i])
    process_list.append(p)
for i in range(number_of_processes):
    print('--------------------------------')
    process_list[i].print_info()

Scheduler(process_list)

s = Scheduler(process_list)

s.initialize_scheduler()

s.print_q2_info()


print("\n Total program time --- %s seconds ---" % (time.time() - start_time))


