def get_longest_word(line: str) -> str:
    words_list = line.split()
    longest_word = words_list[0]
    for i in range(1,len(words_list)):
        if len(words_list[i]) > len(longest_word):
            longest_word = words_list[i]
    return longest_word

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))
