class MyQueue(object):
    def __init__(self):
        self.new_top = []
        self.old_top = []

    def peek(self):
        if len(self.old_top) == 0:
            while len(self.new_top) != 0:
                self.old_top.append(self.new_top.pop())
        return self.old_top[-1]

    def pop(self):
        if len(self.old_top) == 0:
            while len(self.new_top) != 0:
                self.old_top.append(self.new_top.pop())
        return self.old_top.pop()

    def put(self, value):
        self.new_top.append(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
