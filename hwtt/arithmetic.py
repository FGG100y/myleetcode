#!/usr/bin/env python
# encoding: utf-8
# input: 'int' '+' 'int'
# output: result


def arithmetic():
    """simple calculator
    :type s: str
    :rype int
    """
    # only for '+'/'-' operations
    print("Enter arithmatic expression, or 'q' to quit")
    while 1:
        s = input(">> ")
        if s == 'q':
            break
        s = s.split()
        i1 = int(s[0])
        i2 = int(s[2])
        if i1 > 100 or i2 > 100:
            break
        op = s[1]
        if '+' in op and len(op) == 1:
            #  return  i1 + i2
            print(i1 + i2)
        elif '-' in op and len(op) == 1:
            #  return  i1 - i2
            print(i1 - i2)
        else:
            #  return 0
            print(0)


if __name__ == '__main__':
    print(arithmetic())
