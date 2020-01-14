class Queue:

    def __init__(self):
        self.queue = list()

    def add_to_q(self, data_val):
        if data_val not in self.queue:
            self.queue.insert(0, data_val)
            return (True, "IT'S RIGHT")
        return False

    def size(self):
        return len(self.queue)

    def removefromq(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements in Queue!")


TheQueue = Queue()
TheQueue.add_to_q("Mon")
TheQueue.add_to_q("Tue")
TheQueue.add_to_q("Wed")
print(TheQueue.queue)
print(TheQueue.removefromq())
print(TheQueue.removefromq())
