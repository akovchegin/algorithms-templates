def __binary_search(nums, lf, rg, target):
    mid = (rg + lf) // 2
    if nums[mid] == target:
        return mid
    if lf == rg:
        return -1
    if nums[lf] < nums[mid]:
        if target < nums[mid] and target >= nums[lf]:
            return __binary_search(nums, lf, mid, target)
        else:
            return __binary_search(nums, mid, rg, target)
    else:
        if target <= nums[rg-1] and target >= nums[mid]:
            return __binary_search(nums, mid, rg, target)
        else:
            return __binary_search(nums, lf, mid, target)


def broken_search(nums, target) -> int:
    return __binary_search(nums, 0, len(nums), target)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


if __name__ == '__main__':
    test()