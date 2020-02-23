#!/usr/bin/env python
# encryt rules:
# lowercase letters -> numbers
# uppercase letters -> X -> x, then move forward alphabaticly -> y
# others did not change


def upper2lower(char):
    if char == 'Z':
        return 'a'
    else:
        target = ord(char) + 32 + 1
        return chr(target)


def lower2num(char):
    if char in 'abc':
        return '2'
    elif char in 'def':
        return '3'
    elif char in 'ghi':
        return '4'
    elif char in 'jkl':
        return '5'
    elif char in 'mno':
        return '6'
    elif char in 'pqrs':
        return '7'
    elif char in 'tuv':
        return '8'
    elif char in 'wxyz':
        return '9'


def decryt_psw(s):
    psw = ''
    for c in s:
        if c.isupper():
            psw += upper2lower(c)
        elif c.islower():
            psw += lower2num(c)
        else:
            psw += str(c)
    return psw


if __name__ == "__main__":
    s = 'YUANzhi1987'
    print(decryt_psw(s))
