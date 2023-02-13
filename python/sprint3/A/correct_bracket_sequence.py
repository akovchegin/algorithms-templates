def read_input():
    return int(input())


def make_sequence(
    seq_length, openning_brackets_num=0, closing_brackets_num=0, preffix=''
):
    if seq_length == 0:
        print(preffix)
    else:
        if openning_brackets_num < (seq_length+len(preffix))/2:
            openning_brackets_num += 1
            make_sequence(
                seq_length-1,
                openning_brackets_num,
                closing_brackets_num,
                preffix+'('
            )
            openning_brackets_num -= 1
        if closing_brackets_num < openning_brackets_num:
            closing_brackets_num += 1
            make_sequence(
                seq_length-1,
                openning_brackets_num,
                closing_brackets_num,
                preffix+')'
            )
            closing_brackets_num -= 1


if __name__ == '__main__':
    seq_length = read_input()
    make_sequence(seq_length*2)
