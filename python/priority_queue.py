"""
1. A priority queue can be created
pqueue = PriorityQueue()

2. It can have an item and a priority added to it
i.e. pqueue.add(item, priority)
# usually this is pqueue.add(priority, item)

3. Return the highest priority item and remove it from the queue
i.e. item = pqueue.pop()
"""

from queue import PriorityQueue
from typing import Any 

pqueue: PriorityQueue[Any] = PriorityQueue()

pqueue.put((1, "Television"))
pqueue.put((4, "Books"))
pqueue.put((5, "Travel"))
pqueue.put((10, "Cooking"))

def find_highest(queue_example: PriorityQueue[Any]) -> Any:
    if not queue_example.empty():
        return queue_example.get()[1]
    else:
        raise ValueError

print(find_highest(pqueue))
print(pqueue)