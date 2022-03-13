from process import Process
from scheduler import Scheduler
import time
start_time = time.time()

process_list = []

for i in range(Process.NumberOfProcesses):
    p = Process(Process.NumberOfProcesses,Process.process_id[i],Process.arrivalTime[i],Process.burstTime[i],Process.priority[i])
    process_list.append(p)
for i in range(Process.NumberOfProcesses):
    print('--------------------------------')
    process_list[i].print_info()


s = Scheduler(process_list)

s.initialize_scheduler()
s.print_q2_info()



print("\n Total program time --- %s seconds ---" % (time.time() - start_time))


