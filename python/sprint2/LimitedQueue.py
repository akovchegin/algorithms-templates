import sys


class MyQueueSized:
    def __init__(self, n):
        self.queue = [None]*n
        self.max_size = n
        self.head = 0
        self.tail = 0
        self.queue_size = 0

    def push(self, data):
        if self.queue_size == self.max_size:
            return 'error'
        self.queue[self.tail] = data
        self.tail = (self.tail+1) % self.max_size
        self.queue_size +=1

    def pop(self):
        if self.queue_size == 0:
            return 'None'
        data = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head+1) % self.max_size
        self.queue_size -= 1
        return data

    def peek(self):
        if self.queue_size == 0:
            return 'None'
        return self.queue[self.head]

    def size(self):
        return self.queue_size


def read_input():
    num_commands = int(input())
    max_size = int(input())
    command_list = [sys.stdin.readline().strip() for _ in range(num_commands)]
    return max_size, command_list

def main():
    in_max_size, in_command_list = read_input()
    my_queue = MyQueueSized(in_max_size)
    execute_command = {
        'push': my_queue.push,
        'pop': my_queue.pop,
        'peek': my_queue.peek,
        'size': my_queue.size
    }
    for command in in_command_list:
        command_name = command.split()[0]
        command_params = command.split()[1:]
        result = execute_command[command_name](*command_params)
        if result is not None:
            print(result)


if __name__ == '__main__':
    main()
