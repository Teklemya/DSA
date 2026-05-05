from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        

    def next(self, val: int) -> float:
        self.queue.append(val)
        #we check if the queue size if > size if so remove else
        if len(self.queue) > self.size:
            #add to the queue and divide by len
            self.queue.popleft()
        return sum(self.queue) / len(self.queue) 
        #else popleft

'''
U - Givena stream of ints and window size, caluclate the moving average of all interges in the 
    silding window

    I will be initally given the size of 3 for example i will compute the average of the next 3
    numbers upcoming 

    now when i do avearge it can be a float, now when i do the compute i can use a queue
    the reason being the one that came in first should leave wgen the queue size is > size

'''


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)