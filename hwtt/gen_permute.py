#!/usr/bin/env python
# encoding: utf-8
# get exhausive set of all possible orderings we get from permutations,
# produced using recursive funcitons in generator form.


def permute(seq):
    # shuffle any sequence
    if not seq:  # empty seq
        yield seq
    else:
        for i in range(len(seq)):
            # delete current *node
            rest = seq[:i] + seq[i+1:]
            # permute others
            for x in permute(rest):
                # add *note at front
                yield seq[i:i+1] + x
