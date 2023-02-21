# ID успешной отправки 82765633

# Изначально у меня была мысль, что "наружу" я выставляю функцию
# broken_search, которая уже в свою очередь вызывает binary_search
# поэтому я подумал, что "спрятать" binary_search будет уместно.

def binary_search(nums, lf, rg, target):
    mid = (rg + lf) // 2
    if nums[mid] == target:
        return mid
    if lf == rg:
        return -1
    if nums[lf] < nums[mid]:
        if target < nums[mid] and target >= nums[lf]:
            return binary_search(nums, lf, mid, target)
        else:
            return binary_search(nums, mid, rg, target)
    else:
        if target <= nums[rg-1] and target >= nums[mid]:
            return binary_search(nums, mid, rg, target)
        else:
            return binary_search(nums, lf, mid, target)


def broken_search(nums, target) -> int:
    return binary_search(nums, 0, len(nums), target)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


if __name__ == '__main__':
    test()
