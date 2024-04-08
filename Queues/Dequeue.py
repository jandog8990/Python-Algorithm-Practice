# using double ended queue from collections
from collections import deque

# init
queue = deque()
queue = deque([1,2,3])

# add elems to queue
queue.append(4)
queue.append(5)
print(queue)

# dequeuing/removing elems
queue.popleft() #1
queue.pop() # 5

# check elems at front/end
print(queue[0])
print(queue[-1])

print(len(queue))

