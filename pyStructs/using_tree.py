from structs.tree import ExpressionTree


def build_expression_tree(tokens):
    """Return an ExpressionTree based upon by a tokenized expression"""
    S = []
    for t in tokens:
        if t in "=-*x/":
            S.append(t)
        elif t not in "()":
            S.append(ExpressionTree(t))
        elif t == ")":
            right = S.pop()
            op = S.pop()
            left = S.pop()
            S.append(ExpressionTree(op, left, right))
    return S.pop()


if __name__ == "__main__":
    tokens = "((3+1)*3)/((9-5)+2)"
    expr_tree = build_expression_tree(tokens)
    if 2 != expr_tree.evaluate():
        print("Oops, Wrong answer!")
