def read_input():
    n = int(input())
    arr = list(map(int, input().strip().split()))
    return n, arr


def level_up(n, arr):
    max = arr[0]
    min = arr[0]
    max_pos = 0
    for i in range(1,len(arr)):
        if arr[i] >= max:
            max = arr[i]
            max_pos = i
        if arr[i] < min:
            min = arr[i]
    if max_pos != n-1:
        return -1
    return max-min


if __name__ == '__main__':
    n, arr = read_input()
    print(level_up(n, arr))