from collections import deque 

class Queue():
    def __init__(self, list):
        self.list = list
    def enqueue(self, num):
        self.list.append(num)
        return self.list
    def dequeue(self):
        self.list.pop(0)
        return self.list

my_list = Queue([1, 5, 2, 47, 19, 92, 0])
print(my_list.dequeue())
