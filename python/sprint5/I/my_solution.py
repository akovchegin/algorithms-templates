def read_input():
    n = int(input())
    return [i for i in range(1, n+1)]


def count_trees(arr):
    if len(arr) <= 1:
        return 1
    trees_num = 0
    for i in range(len(arr)):
        left_num = count_trees(arr[:i])
        right_num = count_trees(arr[i+1:])
        trees_num += left_num * right_num
    return trees_num


if __name__ == '__main__':
    arr = read_input()
    print(count_trees(arr))
