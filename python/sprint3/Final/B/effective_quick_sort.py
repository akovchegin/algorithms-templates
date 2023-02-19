import sys


def read_input():
    n = int(input())
    arr = [
        sys.stdin.readline().strip().split() for _ in range(n) 
    ]
    return n, arr

def __sort(arr, left, right, key, direction=1):
    if right - left == 1:
        return
    i = left
    j = right-1
    pivot = int(arr[(left+right)//2][key])
    while i < j:
        if (
            int(arr[i][key])*direction > pivot*direction 
            and int(arr[j][key])*direction <= pivot*direction
        ):
            arr[i], arr[j] = arr[j], arr[i]
        if int(arr[i][key])*direction <= pivot*direction:
            i += 1
        if int(arr[j][key])*direction > pivot*direction:
            j -= 1
    __sort(arr, left, i, key,direction)
    __sort(arr, i, right, key,direction)


def sort_results(arr):
    __sort(arr, 0, len(arr),1,-1)
    print(*arr)


if __name__ == '__main__':
    n, arr = read_input()
    result = sort_results(arr)
#    for position in result:
#        print(position[0])