import sys


class Stack:
    def __init__(self):
        self.stack = []
        self.max_value = None

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if len(self.stack) == 0:
            print('error')
        else:
            self.stack.pop()
    
    def get_max(self):
        if len(self.stack) == 0:
            return None
        max_value = int(self.stack[0])
        for value in self.stack[1:]:
            if int(value) > max_value:
                max_value = int(value)
        return max_value


def read_input():
    num_commands = int(input())
    command_list = [sys.stdin.readline().strip() for _ in range(num_commands)]
    return command_list

def main():
    command_list = read_input()
    stack = Stack()
    for command in command_list:
        if command.startswith('push'):
            stack.push(command.split()[1])
        if command == 'pop':
            stack.pop()
        if command == 'get_max':
            print(stack.get_max())

if __name__ == '__main__':
    main()
