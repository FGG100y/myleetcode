#!/usr/bin/env python
# 最大公约数之‘辗转相除法’：(detail in zh.wikipedia.org)

# 计算gcd(18,48)时,先将48除以18得到商2、余数12,然后再将18除以12得到商1、余数6,
# 再将12除以6得到商2、余数0,即得到最大公因数6。我们只关心每次除法的余数是否为0
# 为0即表示得到答案。这一算法更正式的描述是这样的：
#   gcd(a, 0) = a
#   gcd(a, b) = gcd(b, a mod b)
# 如果参数都大于0, 那么该算法可以写成更简单的形式：
#   gcd(a, a) = a
#   gcd(a, b) = gcd(a-b, b) if a > b
#   gcd(a, b) = gcd(a, b-a) if a < b


# the first recursive function I wrote ^^, Sun 22 Mar 2020 23:11:14
def gcd(a, b):
    """calculate the greatest common divisor
    :type a: int, positive number
    :type b: int, positive number
    :rtype int
    """
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)


# the more general algorithm, and more efficient one too
def gcd2(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    a = 12
    b = 44
    print(gcd(a, b))
    print()
    print(gcd2(a, b))
