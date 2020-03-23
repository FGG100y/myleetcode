#!/usr/bin/env python
# General version of convert between the counting systems, such 10 to 17, 26...
# E.g., if counting system were to convert from 26th to 10th, then the 26th
# counting system was using lowercase characters for representation;
# other system, said 17th, 20th, etc, using number plus uppercase characters if
# needed.


def str2num(s, csys, lookup):
    # other counting system to 10th
    num = 0
    for i, c in enumerate(reversed(s)):
        num += lookup[c]*(csys**i)
    return num


def num2str(n, csys, lookup):
    # 10th to other counting system
    s = ''
    while n > 0:
        s += lookup[n % csys]
        n //= csys
    #  return reversed(s)
    return s[::-1]


def mapping(csys=26):
    """maps char to the corresponding num,
    26th using lowercase chars, others using number+uppercase
    """
    uppers = list(map(chr, range(65, 65+csys-1)))
    lowers = [c.lower() for c in uppers]
    if csys == 26:
        lookup = dict(zip(lowers, range(1, len(uppers)+1)))
    else:
        to_tenth = [i for i in range(1, 10)] + uppers[:csys-9]
        lookup = dict((char, idx+1) for idx, char in enumerate(to_tenth))
    lookup2 = dict((v, k) for k, v in lookup.items())

    return lookup, lookup2


def convert_systems(s, csys=26):
    lookup, lookup2 = mapping(csys=csys)
    # str2num
    if isinstance(s, str):
        return str2num(s, csys, lookup)
    elif isinstance(s, int):
        return num2str(s, csys, lookup2)


if __name__ == "__main__":
    print(convert_systems(104680767, csys=26))
    #  print(convert_systems('huawei', csys=26))
    #  print(convert_systems('FF', csys=17))
    print(convert_systems('G', csys=17))
