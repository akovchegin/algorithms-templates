import sys


class Stack:
    def __init__(self):
        self.stack = []
        self.max_value = None

    def push(self, value):
        self.stack.append(int(value))
    
    def pop(self):
        if len(self.stack) == 0:
            return 'error'
        else:
            self.stack.pop()
    
    def get_max(self):
        if len(self.stack) == 0:
            return 'None'
        self.max_value = self.stack[0]
        for value in self.stack[1:]:
            if int(value) > self.max_value:
                self.max_value = int(value)
        return self.max_value


def read_input():
    num_commands = int(input())
    command_list = [sys.stdin.readline().strip() for _ in range(num_commands)]
    return command_list

def main():
    command_list = read_input()
    stack = Stack()
    execute_command = {
        'push': stack.push,
        'pop': stack.pop,
        'get_max': stack.get_max
    }
    for idx, cmd in enumerate(command_list):
        result = None
        cmd_name = cmd.split()[0]
        cmd_params = cmd.split()[1:]
        result = execute_command[cmd_name](*cmd_params)
        if result is not None:
            print(result)

if __name__ == '__main__':
    main()
