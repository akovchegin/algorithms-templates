keypad = {
    '2':'abc',
    '3':'def',
    '4':'ghi',
    '5':'jkl',
    '6':'mno',
    '7':'pqrs',
    '8':'tuv',
    '9':'wxyz'
}


def read_input():
    return [keypad[num] for num in input()]


def make_combinations(length, arr, combination='', result=[]):
    if length == 0:
        return result.append(combination)
    for char in arr[len(combination)]:
        make_combinations(length-1, arr, combination+char, result)
    return result


if __name__ == '__main__':
    arr = read_input()
    result = make_combinations(len(arr), arr)
    print(' '.join(result))