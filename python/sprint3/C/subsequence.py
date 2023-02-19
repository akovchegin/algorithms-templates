import sys


def read_input():
    seq1 = list(sys.stdin.readline().strip())
    seq2 = list(sys.stdin.readline().strip())
    return seq1, seq2


def is_subsequence(seq1, seq2):
    i,j = 0,0
    for i in range(len(seq2)):
        if seq2[i] == seq1[j]:
            j += 1
        if j == len(seq1):
            return True
        i += 1
    return False
                    

if __name__ == '__main__':
    seq1, seq2 = read_input()
    print(is_subsequence(seq1, seq2))
