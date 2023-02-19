import sys
import time


def read_input():
    arr = []
    with open('/var/tmp/input.txt', 'r') as reader:
        n = int(reader.readline().strip())
        for line in reader:
            arr.append(list(map(int, line.strip().split())))
    return n, arr

        
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
    time_start = time.time()
#    sorted_arr = merge_sort(arr)
    sorted_arr = sorted(arr)
    time_mid = time.time()
    result = [sorted_arr[0]]


    for i in range(1,len(sorted_arr)):
        if sorted_arr[i][-1] > result[-1][-1]:
            if sorted_arr[i][0] > result[-1][-1]:
                result.append(sorted_arr[i])
            else:
                result[-1][-1] = sorted_arr[i][-1]
    time_end = time.time()
    print(time_mid-time_start, time_end-time_mid)
    return result

if __name__ == '__main__':
    n, arr = read_input()
    result = get_flowerbeds(n, arr)
    time_start = time.time()
    for item in result:
        print(*item)
    time_end = time.time()
    print(time_end-time_start)
