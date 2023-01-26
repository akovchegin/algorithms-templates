from typing import List, Tuple

def moving_average(arr: List[int], window_size: int) -> List[float]:
#    res = [0]*(len(arr)-window_size+1)
#    current_sum = sum(arr[0:window_size])
#    for i in range(0, len(arr)-window_size):
#        res[i] = current_sum/window_size
#        current_sum -= arr[i]
#        current_sum += arr[i+window_size]
#    res[-1] = current_sum/window_size
#    return res
    res = []
    current_sum = sum(arr[0:window_size])
    res.append(current_sum/window_size)
    for i in range(len(arr)-window_size):
        current_sum -= arr[i]
        current_sum += arr[i+window_size]
        res.append(current_sum/window_size)
    return res


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size

arr, window_size = read_input()
print(" ".join(map(str, moving_average(arr, window_size))))
