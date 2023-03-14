# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:  
        def __init__(self, value, left=None, right=None):  
            self.value = value  
            self.right = right  
            self.left = left


def check_tree(root, root_parent=None):
    if not root:
        return True
    if (root.left and
            (root.left.value >= root.value
                or root_parent and root.left.value <= root_parent.value < root.value)):
        return False
    if (root.right and
            (root.right.value <= root.value
            or root_parent and root.value < root_parent.value <= root.right.value)):
         return False
    return check_tree(root.left, root) and check_tree(root.right, root)


def solution(root) -> bool:
    return check_tree(root)

def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)

if __name__ == '__main__':
    test()