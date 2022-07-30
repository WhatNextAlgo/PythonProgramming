class Stack:
    def __init__(self):
        self.items =[]


    def is_empty(self):
        return self.items == []

    def push(self,data):
        self.items.append(data)


    def pop(self):
        return self.items.pop()


class Queue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()


    def is_empty(self):
        return self.inbox.is_empty() and self.outbox.is_empty()


    def enqueue(self,data):
        self.inbox.push(data)

    def dequeue(self):
        if self.outbox.is_empty():
            while not self.inbox.is_empty():
                dequeued = self.inbox.pop()
                self.outbox.push(dequeued)
        return self.outbox.pop()

a_queue = Queue()
while True:
    print('enqueue <value>')
    print('dequeue')
    print('quit')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'enqueue':
        a_queue.enqueue(int(do[1]))
    elif operation == 'dequeue':
        if a_queue.is_empty():
            print('Queue is empty.')
        else:
            dequeued = a_queue.dequeue()
            print('Dequeued element: ', int(dequeued))
    elif operation == 'quit':
        break