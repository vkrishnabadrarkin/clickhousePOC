import random
import datetime
import time
# event_date = datetime.datetime(2019, 6, 3)
# total_100_active = []
# for i in range(100):
#         event_datetime = event_date.replace(hour=random.randint(0, 23),minute=random.randint(0, 59))
#         total_100_active.append(int(event_datetime.timestamp()))
# total_100_active.sort()
# print(total_100_active[1:10])
# for _ in total_100_active[1:10]:
#         print(time.ctime(_))
metric_100_active = []
for i in range(10):
        srcBytes = random.randint(2500000,28000000)
        dstBytes = random.randint(2500000,28000000)
        totalBytes = srcBytes + dstBytes
        totalPackets = random.randint(1,100)
        sessionCount = random.randint(100,300)
        rttMax = random.randint(20000,70000)
        rttAvg = (rttMax*2)//3
        metric_100_active.append((srcBytes,dstBytes,totalBytes,totalPackets,sessionCount,rttMax,rttAvg))
print(metric_100_active)
