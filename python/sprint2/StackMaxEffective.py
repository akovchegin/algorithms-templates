import sys


class Stack:
    def __init__(self):
        self.items = []
        self.max_values_list = []

    def push(self, value):
        self.items.append(int(value))
        if not self.max_values_list or self.max_values_list and int(value) >= self.max_values_list[-1]:
            self.max_values_list.append(int(value))

    def pop(self):
        if not self.items:
            return 'error'
        item = self.items.pop()
        if item == self.max_values_list[-1]:
            self.max_values_list.pop()

    def get_max(self):
        if self.max_values_list:
            return self.max_values_list[-1]
        return 'None'


def read_input():
    num_commands = int(input())
    commands_list = list(sys.stdin.readline().strip() for _ in range(num_commands))
    return num_commands, commands_list

def main():
    num_commands, command_list = read_input()
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