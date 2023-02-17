import sys


def read_input():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().strip().split())))
    return n, arr


def compare_borders(value1, value2):
    if value1[-1] > value2[-1]:
        return [value1]
    if value1[-1] < value2[0]:
        return [value1, value2]
    return [[value1[0], value2[-1]]]
        
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:len(arr)])

    i,j,k = 0,0,0
    merged_arr = [-1] * (len(left) + len(right))
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_arr[k] = left[i]
            i += 1
        else: 
            merged_arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        merged_arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        merged_arr[k] = right[j]
        j += 1
        k += 1
    return merged_arr

def get_flowerbeds(n, arr):
    sorted_arr = merge_sort(arr)
    result = [sorted_arr[0]]
    for i in range(1,len(sorted_arr)):
        last_item = result.pop()
        result += compare_borders(last_item, sorted_arr[i])
    return result

if __name__ == '__main__':
    n, arr = read_input()
    result = get_flowerbeds(n, arr)
    for item in result:
        print(' '.join(map(str, item)))
