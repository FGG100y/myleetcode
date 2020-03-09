#!/usr/bin/env python
# Input: password string
# Output: security of password
from collections import defaultdict


def psw_length_score(s):
    score = 0
    if len(s) <= 4:
        score += 5
    elif 5 <= len(s) <= 7:
        score += 10
    elif len(s) >= 8:
        score += 25

    return score


def psw_char_diversity(s):
    score = 0
    d = defaultdict(int)
    for c in s:
        if c.islower():
            d['lower'] += 1
        elif c.isupper():
            d['upper'] += 1
        elif c.isdigit():
            d['digit'] += 1
        else:
            d['other'] += 1
    if not (d['lower'] or d['upper']):
        score += 0
    elif (d['lower'] and d['upper']):
        score += 20
    else:
        score += 10
    if not d['digit']:
        score += 0
    elif d['digit'] == 1:
        score += 10
    else:
        score += 20
    if not d['other']:
        score += 0
    elif d['other'] == 1:
        score += 10
    else:
        score += 25
    # bonus
    if all(d.values()):
        score += 5
    elif all([d['digit'], d['other']]) and (d['lower'] or d['upper']):
        score += 3
    elif d['digit'] and (d['lower'] or d['upper']):
        score += 2

    return score


def main():
    score = psw_length_score(s)
    score += psw_char_diversity(s)
    print(score)
    if score >= 90:
        print("VERY_SECURE")
    elif score >= 80:
        print("SECURE")
    elif score >= 70:
        print("VERY_STRONG")
    elif score >= 60:
        print("STRONG")
    elif score >= 50:
        print("AVERAGE")
    elif score >= 25:
        print("WEAK")
    else:
        print("VERY_WEAK")


if __name__ == "__main__":
    s = 'aF1*'*3
    main()
