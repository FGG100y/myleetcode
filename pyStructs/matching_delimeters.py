"""Matching delimeters in arithmetic expressions
"""


from arraybased_stack.array_stack import ArrayStack


def is_matched(expr):
    """Return True if all delimeters are properly match; False otherwise"""
    lefty = "({["
    righty = ")}]"
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            # nothing to match
            if S.is_empty():
                return False
            # mismatched
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()


if __name__ == "__main__":
    expr = "(2*3)/4*(2+2)}"
    print(is_matched(expr))
