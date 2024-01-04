#103744658
import string
from typing import List


def expand(sum: str) -> str:
    stack: List[str] = []
    num: str = ''
    alphabet: str = ''

    for i in range(len(sum)):
        curent = sum[i]
        if curent in string.digits:
            num += curent
        elif curent == ']':
            prev_num, prev_result = stack.pop()
            alphabet = prev_result + alphabet * prev_num
        elif curent == '[':
            stack.append((int(num), alphabet))
            num = ''
            alphabet = ''
        else:
            alphabet += curent
    
    return alphabet


if __name__ == '__main__':
    score = input()
    print(expand(score))
