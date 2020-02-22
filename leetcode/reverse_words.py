#!/usr/bin/env python


def rwords(s):
    """reverse the words in string

    rtype: None
    """
    s = s[::-1]
    rws = [w[::-1] for w in s.split()]
    print("".join(rws))


def rwords_1space(s):
    """reverse the words in string, seperate by only one space between words
    """
    # replace all non-alphabetic chars with Spaces
    words_mult_spaces = [char if char.isalpha() else ' ' for char in s]
    # reverse the whole stings
    rws_spaces = "".join(words_mult_spaces[::-1])
    # strip the Spaces
    print(" ".join([w[::-1].strip() for w in rws_spaces.split()]))


if __name__ == "__main__":
    s1 = 'asdf dadgdd ADbdgDD'
    s2 = 'ASD#$%,sfd  ,FGE#gggd'

    print(s1)
    print('--'*10)
    rwords(s1)
    rwords_1space(s1)

    print()
    print(s2)
    print('--'*10)
    rwords(s2)
    rwords_1space(s2)
