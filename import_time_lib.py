'''
from datetime import datetime
import time

# currentTime = time.clock()
print(time.time())
print(time.process_time())


now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
'''
import time

currentTime = time.ctime()
print("Hello")
pastTime = time.ctime()
for i in range(1, 20):
    print(i)
    time.sleep(1)

# print(currentTime)
