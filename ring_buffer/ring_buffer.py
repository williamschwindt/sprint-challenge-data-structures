class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None for el in range(0, self.capacity)]
        self.curr = 0

    def append(self, item):
        #add item at the index of self.curr and increment curr
        self.buffer[self.curr] = item
        self.curr += 1
        
        #reset curr if its at capacity
        if self.curr == self.capacity:
            self.curr = 0

    def get(self):
        arr = []
        for el in self.buffer:
            if el is not None:
                arr.append(el)
        return arr