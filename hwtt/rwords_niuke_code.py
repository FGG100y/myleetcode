import sys


def reverse_words():
    s = sys.stdin.readline().strip()
    # replace all non-alphabetic chars with Spaces
    words_mult_spaces = [char if char.isalpha() else ' ' for char in s]
    # reverse the whole stings
    rws_spaces = "".join(words_mult_spaces[::-1])
    # strip the Spaces
    print(" ".join([w[::-1].strip() for w in rws_spaces.split()]))


if __name__ == "__main__":
    try:
        # 看清楚题目要求输入多少cases，才决定是否需要while循环
        #  while 1:
        reverse_words()
    except Exception:
        pass
