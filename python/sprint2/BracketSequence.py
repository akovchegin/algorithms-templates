import sys


MATCHING_BRACKET = {
    '(': ')',
    '{': '}',
    '[': ']'
}


class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes:
            node = Node(nodes.pop(0))
            self.head = node
            prev_node = None
            for item in nodes:
                node.next = Node(item)
                node.prev = prev_node
                prev_node = node
                node = node.next
            node.prev = prev_node

    def remove_node(self, node):
        if self.head is None:
            raise LookupError('Trying to remove element from empty list')

        if self.head.data == node.data:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return

        current_node = self.head.next
        while current_node.data != node.data and current_node.next is not None:
            current_node = current_node.next

        current_node.prev.next = current_node.next
        if current_node.next is not None:
            current_node.next.prev = current_node.prev

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return " ".join(nodes)


def is_correct_bracket_seq(l_list):
    if l_list.head is None:
        return True
    removed_count = -1
    while l_list.head is not None and removed_count != 0:
        l_list, removed_count = remove_matching_brackets(l_list)
    if l_list.head is None:
        return True
    return False

def read_input():
    in_str = sys.stdin.readline().strip()
    l_list = LinkedList([*in_str])
    return l_list

def remove_matching_brackets(l_list):
    current_node = l_list.head
    removed_count = 0
    while current_node is not None and current_node.next is not None:
        if current_node.data in MATCHING_BRACKET and current_node.next.data == MATCHING_BRACKET[current_node.data]:
            l_list.remove_node(current_node.next)
            l_list.remove_node(current_node)
            removed_count += 1
        current_node = current_node.next
    return l_list, removed_count

def main():
    l_list = read_input()
    return is_correct_bracket_seq(l_list)

if __name__ == '__main__':
    result = main()
    print(result)