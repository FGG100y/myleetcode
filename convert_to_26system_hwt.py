# 某种场景下，开发人员决定使用字母表示一个正整数，该方法利用英文的小写字母表示，
# 映射规则很简单，按字母顺序每一个字母都代表一个值，如下所示列表的部分内容：
#  a 1
#  b 2
#  c 3
#  ...
#  z 26
#  aa 27
#  ab 28
#  ...
#  huawei 104680767
#  ...
#
# 编写一个程序，输入为字符串时，输出对应的数值；输入是数字时，输出对应字符串.


def str2num(s, lookup):
    # 26进制转换10进制
    num = 0
    for i, c in enumerate(reversed(s)):
        num += lookup[c]**i
    return num


def num2str(n, lookup):
    # 10进制转换26进制
    s = ''
    while n > 0:
        s += lookup[n % 26]
        n //= 26
    #  return reversed(s)
    return s[::-1]


def convert_to_26sys(s):
    lookup = dict(zip(list(map(chr, range(97, 122))), range(1, 26)))
    lookup2 = dict((v, k) for k, v in lookup.items())
    # str2num
    if isinstance(s, str):
        return str2num(s, lookup)
    elif isinstance(s, int):
        return num2str(s, lookup2)


if __name__ == "__main__":
    print(convert_to_26sys(104680767))
