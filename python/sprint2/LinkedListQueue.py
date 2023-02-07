import sys


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.size = 0

    def put(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.size += 1

    def get(self):
        if self.head is None:
            return 'error'
        out_node = self.head.data
        self.head = self.head.next
        self.size -= 1
        return out_node

    def get_size(self):
        return self.size


def read_input():
    num_commands = int(input())
    commands_list = list(sys.stdin.readline().strip() for _ in range(num_commands))
    return commands_list

def main():
    queue = LinkedListQueue()
    execute_command = {
        'put': queue.put,
        'get': queue.get,
        'size': queue.get_size
    }
    commands_list = read_input()
    for command in commands_list:
        command = command.split()
        command_name = command[0]
        command_params = command[1:]
        result = execute_command[command_name](*command_params)
        if result is not None:
            print(result)

if __name__ == '__main__':
    main()