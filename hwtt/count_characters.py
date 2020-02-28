#!/usr/bin/env python
# count the letters/blank/digits/others in a string


def count_letters(s):
    return len([1 for c in s if c.isalpha()])


def count_digits(s):
    return len([1 for c in s if c.isdigit()])


def count_space(s):
    return len([1 for c in s if c.isspace()])


def count_characters(s):
    letters = count_letters(s)
    digits = count_digits(s)
    space = count_space(s)
    others = len(s) - (letters + digits + space)
    print(letters)
    print(space)
    print(digits)
    print(others)


def count_characters2(s):
    lt, dg, sp, ot = 0, 0, 0, 0
    for c in s:
        if c.isalpha():
            lt += 1
        elif c.isdigit():
            dg += 1
        elif c.isspace():
            sp += 1
        else:
            ot += 1
    print(lt)
    print(sp)
    print(dg)
    print(ot)


if __name__ == "__main__":
    #  try:
    #      while 1:
    #          s = input()
    #          count_characters(s)
    #  except:
    #      pass
    s = '1qazxsw23 edcvfr45tgbn hy67uj m,ki89ol.\\/;p0-=\\]['
    count_characters(s)
