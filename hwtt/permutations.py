"""
permutation-type operations for squences
"""


def permute(lst):
    """shuffle any sequence"""
    # empty sequence
    if not lst:
        return [lst]
    else:
        result = []
        for i in range(len(lst)):
            # keep out the current node
            rest = lst[:i] + lst[i+1:]
            # permute the rest
            for x in permute(rest):
                # add node to the front
                result.append(lst[i:i+1] + x)
        return result


def subset(lst, size):
    if size == 0 or not lst:
        return [lst[:0]]
    else:
        result = []
        for i in range(len(lst)):
            pick = lst[i:i+1]
            rest = lst[:i] + lst[i+1:]
            for x in subset(rest, size-1):
                result.append(pick + x)
        return result


def combo(lst, size):
    """
    permute the sequence but only keep valid subsets with given size and the
    elements of sequence subset are not all the same('he' == 'eh', keep only
    one of them)
    """
    if size == 0 or not lst:
        return [lst[:0]]
    else:
        result = []
        # if and only if there is enough left
        for i in range(0, (len(lst) - size) + 1):
            pick = lst[i:i+1]
            rest = lst[i+1:]
            for x in combo(rest, size-1):
                result.append(pick + x)
        return result


if __name__ == "__main__":
    seq = [2, 4, 5]
    strs = "help"
    print(permute(seq))
    print(permute(strs))
    print()
    print(combo(seq, 2))
    print(combo(strs, 2))
