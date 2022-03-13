#import process
import time
start_time = time.time()
for line in range(10000):
    print('hi')

print("--- %s seconds ---" % (time.time() - start_time))