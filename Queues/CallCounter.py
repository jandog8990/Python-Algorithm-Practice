from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        # check that the oldest element is within the 3000 
        while self.queue and self.queue[0] < t-3000:
            # oldest element popped if older than 3000 
            self.queue.popleft()

        # add to the queue
        self.queue.append(t)
        return len(self.queue)

obj = RecentCounter()
param1 = obj.ping(1)
param2 = obj.ping(100)
param3 = obj.ping(3001)
param4 = obj.ping(4000)
print(param1)
print(param2)
print(param3)
print(param4)
