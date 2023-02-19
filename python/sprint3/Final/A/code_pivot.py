def __find_pivot(nums, lf, rg):
    mid = (rg + lf) // 2
    if rg - lf == 1:
        return
    if nums[mid] < nums[mid-1]:
        return mid
    if nums[mid] < nums[lf]:
        return __find_pivot(nums, lf, mid)
    else:
        return __find_pivot(nums, mid, rg)

def __find_target(nums, lf, rg, target):
    mid = (rg + lf) // 2
    if nums[mid] == target:
        return mid
    if rg - lf == 1:
        return -1
    if target < nums[mid]:
        return __find_target(nums, lf, mid, target)
    else:
        return __find_target(nums, mid, rg, target)

def broken_search(nums, target) -> int:
    pivot = __find_pivot(nums, 0, len(nums))
    if not pivot:
        return __find_target(nums, 0, len(nums), target)
    if target <= nums[-1]:
        return __find_target(nums, pivot, len(nums), target)
    else:
        return __find_target(nums, 0, pivot, target)

def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


if __name__ == '__main__':
    test()