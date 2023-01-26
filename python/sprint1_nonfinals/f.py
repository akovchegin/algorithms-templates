def is_palindrome(line: str) -> bool:
    left_pos = 0
    right_pos = len(line)-1
    punctuation = [' ', '.', ',', ':', ';', '?', '!', '\'', '\"']
    while left_pos < right_pos:
        while line[left_pos] in punctuation:
            left_pos += 1
        while line[right_pos] in punctuation:
            right_pos -= 1
        if line[left_pos].lower() != line[right_pos].lower():
            return False
        left_pos += 1
        right_pos -= 1
    return True

print(is_palindrome(input().strip()))
