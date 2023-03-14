# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:  
        def __init__(self, value, left=None, right=None):  
            self.value = value  
            self.right = right  
            self.left = left


def find_max(root, max_value):
    if not root:
        return max_value[0]
    if root.left and root.left.value > max_value[0]:
        max_value[0] = root.left.value
    if root.right and root.right.value > max_value[0]:
        max_value[0] = root.right.value
    find_max(root.right, max_value)
    find_max(root.left, max_value)


def solution(root) -> int:
    max_value = [root.value]
    find_max(root, max_value)
    return max_value[0]

def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3

if __name__ == '__main__':
    test()