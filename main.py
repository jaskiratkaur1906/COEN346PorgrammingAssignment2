from process import Process
import time
start_time = time.time()


process_list = []

for i in range(Process.NumberOfProcesses):
    p = Process(Process.NumberOfProcesses,Process.process_id[i],Process.arrivalTime[i],Process.burstTime[i],Process.priority[i])
    process_list.append(p)
for i in range(Process.NumberOfProcesses):
    print('--------------------------------')
    process_list[i].print_info()



print("--- %s seconds ---" % (time.time() - start_time))
